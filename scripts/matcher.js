/**
 * CheatCode - Problem Matching Engine
 * Author: brindoxx
 * Description: Normalizes titles, executes exact/fuzzy lookup against Striver's sheet,
 * and ensures only direct, canonical LeetCode & GeeksforGeeks problem links are provided.
 */

(function (root, factory) {
  if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.CheatCodeMatcher = factory();
  }
})(typeof self !== 'undefined' ? self : this, function () {

  // Validates if URL is an actual direct practice problem link (not a search or problemset list page)
  function isValidDirectProblemUrl(url, platform) {
    if (!url || typeof url !== 'string') return false;
    const clean = url.trim();
    if (!clean.startsWith('http://') && !clean.startsWith('https://')) return false;

    if (platform === 'leetcode') {
      if (clean.includes('/problemset') || clean.includes('/search')) return false;
      return clean.includes('leetcode.com/problems/');
    }

    if (platform === 'gfg') {
      if (clean.includes('/search/?') || clean.includes('/search?')) return false;
      return clean.includes('geeksforgeeks.org/problems/') || clean.includes('practice.geeksforgeeks.org/problems/');
    }

    return true;
  }

  // Extracts problem slug from LeetCode or GFG canonical URL
  function extractProblemSlug(url) {
    if (!url || typeof url !== 'string') return null;
    try {
      const u = new URL(url);
      if (u.pathname.includes('/problems/')) {
        const parts = u.pathname.split('/problems/')[1].split('/').filter(Boolean);
        if (parts[0]) {
          // Remove trailing numeric identifiers like overlapping-intervals--170633
          return parts[0].replace(/--?\d+$/, '').replace(/[-_]+/g, ' ').trim();
        }
      }
    } catch (e) {}
    return null;
  }

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

    // Remove common suffixes and badge tags: "[Medium]", "(Leetcode)", "Core", "FAQ", "Editorial"
    clean = clean.replace(/\s*(\(|\[)(leetcode|gfg|codechef|interviewbit|easy|medium|hard|editorial)(\)|\])/gi, '');
    clean = clean.replace(/\s*\|\s*takeuforward.*$/i, '');
    clean = clean.replace(/\s*\b(core|must do|starred|revision|optional|notes|faqs?|solved|unsolved)\b\s*$/gi, '');

    // Strip punctuation and reduce whitespace
    let alphaKey = clean
      .toLowerCase()
      .replace(/['’]/g, '')
      .replace(/[^a-z0-9]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();

    // Strip trailing tags that may have had punctuation removed
    alphaKey = alphaKey.replace(/\s*\b(core|must do|starred|revision|optional|notes|faqs?|solved|unsolved)\b\s*$/g, '').trim();

    // Canonicalize standard DSA terminology differences between TUF, LeetCode, and GFG
    alphaKey = alphaKey
      .replace(/\bzig\s*zag\b/g, 'zigzag')
      .replace(/\brain\s*water\b/g, 'rainwater')
      .replace(/\bsub\s*intervals?\b/g, 'intervals')
      .replace(/\bsub\s*arrays?\b/g, 'subarray')
      .replace(/\bsub\s*sequences?\b/g, 'subsequence')
      .replace(/\bpalindromic\b/g, 'palindrome')
      .replace(/\bnon\s*overlapping\b/g, 'nonoverlapping')
      .replace(/\bk\s*th\b/g, 'kth')
      .replace(/\b(of|in)\s+(a\s+)?(binary\s+tree|linked\s+list|array|string)\b/g, '$3')
      .replace(/\s+/g, ' ')
      .trim();

    // Core key removes common generic filler words like "problem", "algorithm", "check for", "check if", prepositions
    const coreKey = alphaKey
      .replace(/\b(problem|problems|algorithm|algorithms|approach|method|implementation|check for|check if|print|find)\b/g, '')
      .replace(/\b(in|of|a|an|the)\b/g, '')
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
      [/\bdll\b/g, 'doubly linked list'],
      [/\bbs\b/g, 'binary search'],
      [/\bbinary search\b/g, 'bs'],
      [/\bbt\b/g, 'binary tree'],
      [/\bbinary tree\b/g, 'bt'],
      [/\bbst\b/g, 'binary search tree'],
      [/\bbinary search tree\b/g, 'bst'],
      [/\blca\b/g, 'lowest common ancestor'],
      [/\blowest common ancestor\b/g, 'lca'],
      [/\blcs\b/g, 'longest common subsequence'],
      [/\blis\b/g, 'longest increasing subsequence'],
      [/\bmcm\b/g, 'matrix chain multiplication'],
      [/\bmst\b/g, 'minimum spanning tree'],
      [/\brating\b/g, 'rank']
    ];

    for (const [regex, replacement] of mappings) {
      if (regex.test(text)) {
        vars.push(text.replace(regex, replacement));
      }
    }

    // Simultaneously expand all acronyms to create fully-expanded variation
    let fullyExpanded = text;
    for (const [regex, replacement] of mappings) {
      fullyExpanded = fullyExpanded.replace(regex, replacement);
    }
    if (fullyExpanded !== text) {
      vars.push(fullyExpanded);
    }

    // Handle "or" variations (e.g. "Zig Zag or Spiral Traversal" -> ["Zig Zag Traversal", "Spiral Traversal"])
    if (text.includes(' or ')) {
      const parts = text.split(' or ');
      if (parts.length === 2) {
        const p1 = parts[0].trim();
        const p2 = parts[1].trim();
        const p2Words = p2.split(' ');
        const lastWord = p2Words[p2Words.length - 1];
        if (lastWord && !p1.endsWith(lastWord)) {
          vars.push(`${p1} ${lastWord}`);
        } else {
          vars.push(p1);
        }
        vars.push(p2);
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

        // 1. Primary Title (highest priority)
        const keysToIndex = [
          ...numberWordVariations(norm.key),
          ...numberWordVariations(norm.coreKey)
        ];

        for (const k of keysToIndex) {
          if (!this.exactIndex.has(k)) {
            this.exactIndex.set(k, entry);
          }
        }

        // Index truncated forms without trailing "of Binary Tree" etc. (e.g. "Boundary Traversal of Binary Tree" -> "Boundary Traversal")
        const strippedTree = norm.coreKey.replace(/\b(binary tree|binary search tree|bst|bt|linked list|ll)\b/g, '').trim();
        if (strippedTree && strippedTree.length >= 6) {
          if (!this.exactIndex.has(strippedTree)) {
            this.exactIndex.set(strippedTree, entry);
          }
        }

        // 2. Index explicit aliases from dataset
        if (Array.isArray(p.aliases)) {
          for (const alias of p.aliases) {
            const aNorm = normalizeTitle(alias);
            if (aNorm.key) {
              for (const ak of [...numberWordVariations(aNorm.key), ...numberWordVariations(aNorm.coreKey)]) {
                if (!this.exactIndex.has(ak)) {
                  this.exactIndex.set(ak, entry);
                }
              }
              aNorm.coreKey.split(' ').filter(t => t.length > 1).forEach(t => entry.tokens.add(t));
            }
          }
        }

        // 3. Extract and index slugs from LeetCode & GFG URLs
        const lcSlug = extractProblemSlug(p.leetcode);
        if (lcSlug) {
          const sNorm = normalizeTitle(lcSlug);
          if (sNorm.key) {
            for (const sk of [...numberWordVariations(sNorm.key), ...numberWordVariations(sNorm.coreKey)]) {
              if (!this.exactIndex.has(sk)) {
                this.exactIndex.set(sk, entry);
              }
            }
            sNorm.coreKey.split(' ').filter(t => t.length > 1).forEach(t => entry.tokens.add(t));
          }
        }

        const gfgSlug = extractProblemSlug(p.gfg);
        if (gfgSlug) {
          const gNorm = normalizeTitle(gfgSlug);
          if (gNorm.key) {
            for (const gk of [...numberWordVariations(gNorm.key), ...numberWordVariations(gNorm.coreKey)]) {
              if (!this.exactIndex.has(gk)) {
                this.exactIndex.set(gk, entry);
              }
            }
            gNorm.coreKey.split(' ').filter(t => t.length > 1).forEach(t => entry.tokens.add(t));
          }
        }

        this.tokenIndex.push(entry);
      }
    }

    find(rawTitle) {
      const norm = normalizeTitle(rawTitle);
      if (!norm.key) return null;

      // 1. Exact Match via full key or core key or number/word variations
      const queryVariations = [
        ...numberWordVariations(norm.key),
        ...numberWordVariations(norm.coreKey)
      ];

      for (const q of queryVariations) {
        if (this.exactIndex.has(q)) {
          const matchedEntry = this.exactIndex.get(q);
          const lcDirect = isValidDirectProblemUrl(matchedEntry.leetcode, 'leetcode') ? matchedEntry.leetcode : null;
          const gfgDirect = isValidDirectProblemUrl(matchedEntry.gfg, 'gfg') ? matchedEntry.gfg : null;
          if (!lcDirect && !gfgDirect) return null;
          return { ...matchedEntry, leetcode: lcDirect, gfg: gfgDirect, matchType: 'exact' };
        }
      }

      // 2. Substring matching (ranked by minimal length delta to prevent false positives)
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

      if (bestSubMatch && minLengthDelta <= 20) {
        const lcDirect = isValidDirectProblemUrl(bestSubMatch.leetcode, 'leetcode') ? bestSubMatch.leetcode : null;
        const gfgDirect = isValidDirectProblemUrl(bestSubMatch.gfg, 'gfg') ? bestSubMatch.gfg : null;
        if (lcDirect || gfgDirect) {
          return { ...bestSubMatch, leetcode: lcDirect, gfg: gfgDirect, matchType: 'substring' };
        }
      }

      // 3. Token Subset Matching (e.g. all search tokens are contained in problem's tokens)
      const searchTokens = norm.coreKey.split(' ').filter(t => t.length > 2);
      if (searchTokens.length >= 2) {
        for (const entry of this.tokenIndex) {
          let allPresent = true;
          for (const token of searchTokens) {
            if (!entry.tokens.has(token)) {
              allPresent = false;
              break;
            }
          }
          if (allPresent) {
            const lcDirect = isValidDirectProblemUrl(entry.leetcode, 'leetcode') ? entry.leetcode : null;
            const gfgDirect = isValidDirectProblemUrl(entry.gfg, 'gfg') ? entry.gfg : null;
            if (lcDirect || gfgDirect) {
              return { ...entry, leetcode: lcDirect, gfg: gfgDirect, matchType: 'token-subset' };
            }
          }
        }
      }

      // 4. Token Overlap / Fuzzy Match
      let bestTokenMatch = null;
      let highestScore = 0;

      if (searchTokens.length > 0) {
        for (const entry of this.tokenIndex) {
          let commonCount = 0;
          for (const token of searchTokens) {
            if (entry.tokens.has(token)) commonCount++;
          }
          const score = (2 * commonCount) / (searchTokens.length + entry.tokens.size);
          if (score > highestScore && score >= 0.5) {
            highestScore = score;
            bestTokenMatch = entry;
          }
        }
      }

      if (bestTokenMatch) {
        const lcDirect = isValidDirectProblemUrl(bestTokenMatch.leetcode, 'leetcode') ? bestTokenMatch.leetcode : null;
        const gfgDirect = isValidDirectProblemUrl(bestTokenMatch.gfg, 'gfg') ? bestTokenMatch.gfg : null;
        if (lcDirect || gfgDirect) {
          return { ...bestTokenMatch, leetcode: lcDirect, gfg: gfgDirect, matchType: 'fuzzy' };
        }
      }

      return null;
    }
  }

  return {
    isValidDirectProblemUrl,
    normalizeTitle,
    extractProblemSlug,
    Matcher
  };
});
