/**
 * CheatCode - Problem Matching Engine
 * Author: brindoxx
 * Description: Normalizes titles, executes exact/fuzzy lookup against Striver's sheet,
 * and provides dynamic smart fallback URLs for LeetCode & GeeksforGeeks.
 */

(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.CheatCodeMatcher = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {

  // Normalize string for indexing and lookup
  function normalizeTitle(rawTitle) {
    if (!rawTitle || typeof rawTitle !== 'string') return { displayName: '', key: '', coreKey: '' };
    
    let clean = rawTitle
      .replace(/&amp;/g, '&')
      .replace(/&quot;/g, '"')
      .replace(/&#39;/g, "'")
      .replace(/&lt;/g, '<')
      .replace(/&gt;/g, '>');

    // Remove common prefixes: "1. ", "Step 1.2: ", "Q3. ", "01 - ", "Day 1: "
    clean = clean.replace(/^(step\s*\d+(\.\d+)?[:\-]?\s*)/i, '');
    clean = clean.replace(/^(day\s*\d+[:\-]?\s*)/i, '');
    clean = clean.replace(/^(q\s*\d+[\.\:\-]?\s*)/i, '');
    clean = clean.replace(/^(\d+[\.\:\-]\s*)/, '');
    clean = clean.replace(/^([ivxlcdm]+[\.\:\-]\s*)/i, '');

    // Remove common suffixes: "[Medium]", "(Leetcode)", "(GFG)", "Tutorial", "Editorial"
    clean = clean.replace(/\s*(\(|\[)(leetcode|gfg|codechef|interviewbit|easy|medium|hard|editorial)(\)|\])/gi, '');
    clean = clean.replace(/\s*\|\s*takeuforward.*$/i, '');

    // Strip punctuation and reduce whitespace
    const alphaKey = clean
      .toLowerCase()
      .replace(/['’]/g, '')
      .replace(/[^a-z0-9]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();

    // Core key removes common generic filler words like "problem", "algorithm", "implementation"
    const coreKey = alphaKey
      .replace(/\b(problem|problems|algorithm|algorithms|approach|method)\b/g, '')
      .replace(/\s+/g, ' ')
      .trim();

    return {
      displayName: clean.trim(),
      key: alphaKey,
      coreKey: coreKey || alphaKey
    };
  }

  function numberWordVariations(text) {
    const vars = [text];
    const mappings = [
      [/\b2\b/g, 'two'],
      [/\btwo\b/g, '2'],
      [/\b3\b/g, 'three'],
      [/\bthree\b/g, '3'],
      [/\b4\b/g, 'four'],
      [/\bfour\b/g, '4'],
      [/\b1\b/g, 'one'],
      [/\bone\b/g, '1'],
      [/\bll\b/g, 'linked list'],
      [/\blinked list\b/g, 'll'],
      [/\bll\b/g, 'list'],
      [/\blist\b/g, 'll'],
      [/\blinked list\b/g, 'list'],
      [/\blist\b/g, 'linked list'],
      [/\bbs\b/g, 'binary search'],
      [/\bbinary search\b/g, 'bs'],
      [/\bbt\b/g, 'binary tree'],
      [/\bbinary tree\b/g, 'bt'],
      [/\bbst\b/g, 'binary search tree'],
      [/\bbinary search tree\b/g, 'bst']
    ];

    for (const [regex, replacement] of mappings) {
      if (regex.test(text)) {
        vars.push(text.replace(regex, replacement));
      }
    }
    return vars;
  }

  class Matcher {
    constructor(problemsList = []) {
      this.problems = problemsList;
      this.exactIndex = new Map();
      this.tokenIndex = [];
      this.buildIndex();
    }

    setProblems(problemsList) {
      this.problems = problemsList;
      this.buildIndex();
    }

    buildIndex() {
      this.exactIndex.clear();
      this.tokenIndex = [];

      for (const p of this.problems) {
        const norm = normalizeTitle(p.title);
        if (!norm.key) continue;

        const entry = {
          ...p,
          cleanTitle: norm.displayName,
          normKey: norm.key,
          coreKey: norm.coreKey,
          tokens: new Set(norm.coreKey.split(' ').filter(t => t.length > 1))
        };

        const keysToIndex = [
          ...numberWordVariations(norm.key),
          ...numberWordVariations(norm.coreKey)
        ];

        for (const k of keysToIndex) {
          if (!this.exactIndex.has(k)) {
            this.exactIndex.set(k, entry);
          }
        }

        this.tokenIndex.push(entry);
      }
    }

    find(rawTitle) {
      const norm = normalizeTitle(rawTitle);
      if (!norm.key) return null;

      // 1. Exact Match via full key or core key or variations
      const queryVariations = [
        ...numberWordVariations(norm.key),
        ...numberWordVariations(norm.coreKey)
      ];

      for (const q of queryVariations) {
        if (this.exactIndex.has(q)) {
          return {
            ...this.exactIndex.get(q),
            isFallback: false,
            matchType: 'exact'
          };
        }
      }

      // 2. Substring matching (ranked by minimal length delta to avoid matching "Two Sum IV" for "Two Sum")
      let bestSubMatch = null;
      let minLengthDelta = Infinity;

      for (const entry of this.tokenIndex) {
        const matchFound = 
          entry.coreKey.includes(norm.coreKey) || 
          norm.coreKey.includes(entry.coreKey) ||
          entry.normKey.includes(norm.key) ||
          norm.key.includes(entry.normKey);

        if (matchFound) {
          const delta = Math.abs(entry.normKey.length - norm.key.length);
          if (delta < minLengthDelta) {
            minLengthDelta = delta;
            bestSubMatch = entry;
          }
        }
      }

      if (bestSubMatch && minLengthDelta <= 15) {
        return {
          ...bestSubMatch,
          isFallback: false,
          matchType: 'substring'
        };
      }

      // 3. Token Overlap / Fuzzy Match
      const searchTokens = norm.coreKey.split(' ').filter(t => t.length > 2);
      let bestTokenMatch = null;
      let highestScore = 0;

      if (searchTokens.length > 0) {
        for (const entry of this.tokenIndex) {
          let commonCount = 0;
          for (const token of searchTokens) {
            if (entry.tokens.has(token)) commonCount++;
          }
          const score = (2 * commonCount) / (searchTokens.length + entry.tokens.size);
          if (score > highestScore && score >= 0.6) {
            highestScore = score;
            bestTokenMatch = entry;
          }
        }
      }

      if (bestTokenMatch) {
        return {
          ...bestTokenMatch,
          isFallback: false,
          matchType: 'fuzzy',
          score: highestScore
        };
      }

      // 4. Smart Fallback: Generate real search URLs if not found in database
      const fallbackTitle = norm.displayName || rawTitle;
      return {
        title: fallbackTitle,
        topic: 'DSA Practice',
        difficulty: 'Practice',
        leetcode: `https://leetcode.com/problemset/?search=${encodeURIComponent(fallbackTitle)}`,
        gfg: `https://www.geeksforgeeks.org/search/?q=${encodeURIComponent(fallbackTitle)}`,
        isFallback: true,
        matchType: 'fallback'
      };
    }
  }

  return {
    normalizeTitle,
    Matcher
  };
});
