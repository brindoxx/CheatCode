/**
 * CheatCode - Content Script
 * Author: brindoxx
 * Description: Scans TakeUForward pages, identifies DSA problems, and injects
 * direct LeetCode and GeeksforGeeks practice badges into the DOM.
 */

(function () {
  'use strict';

  // Prevent double initialization
  if (window.__cheatcode_initialized) return;
  window.__cheatcode_initialized = true;

  let matcher = null;
  let settings = {
    showLeetcode: true,
    showGfg: true
  };

  // SVGs for clean branded icons (official Simple Icons brand vectors)
  const LEETCODE_SVG = `
    <svg viewBox="0 0 24 24" width="14" height="14" fill="#FFA116" xmlns="http://www.w3.org/2000/svg">
      <path d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.83 5.83 0 0 0 .349 1.017 5.938 5.938 0 0 0 1.271 1.818l4.277 4.193.039.038c2.248 2.165 5.852 2.133 8.063-.074l2.396-2.392c.54-.54.54-1.414.003-1.955a1.378 1.378 0 0 0-1.951-.003l-2.396 2.392a3.021 3.021 0 0 1-4.205.038l-.02-.019-4.276-4.193c-.652-.64-.972-1.469-.948-2.263a2.68 2.68 0 0 1 .066-.523 2.545 2.545 0 0 1 .619-1.164L9.13 8.114c1.058-1.134 3.204-1.27 4.43-.278l3.501 2.831c.593.48 1.461.387 1.94-.207a1.384 1.384 0 0 0-.207-1.943l-3.5-2.831c-.8-.647-1.766-1.045-2.774-1.202l2.015-2.158A1.384 1.384 0 0 0 13.483 0zm-2.866 12.815a1.38 1.38 0 0 0-1.38 1.382 1.38 1.38 0 0 0 1.38 1.382H20.79a1.38 1.38 0 0 0 1.38-1.382 1.38 1.38 0 0 0-1.38-1.382z"/>
    </svg>
  `;

  const GFG_SVG = `
    <svg viewBox="0 0 24 24" width="14" height="14" fill="#2F8D46" xmlns="http://www.w3.org/2000/svg">
      <path d="M21.45 14.315c-.143.28-.334.532-.565.745a3.691 3.691 0 0 1-1.104.695 4.51 4.51 0 0 1-3.116-.016 3.79 3.79 0 0 1-2.135-2.078 3.571 3.571 0 0 1-.13-.353h7.418a4.26 4.26 0 0 1-.368 1.008zm-11.99-.654a3.793 3.793 0 0 1-2.134 2.078 4.51 4.51 0 0 1-3.117.016 3.7 3.7 0 0 1-1.104-.695 2.652 2.652 0 0 1-.564-.745 4.221 4.221 0 0 1-.368-1.006H9.59c-.038.12-.08.238-.13.352zm14.501-1.758a3.849 3.849 0 0 0-.082-.475l-9.634-.008a3.932 3.932 0 0 1 1.143-2.348c.363-.35.79-.625 1.26-.809a3.97 3.97 0 0 1 4.484.957l1.521-1.49a5.7 5.7 0 0 0-1.922-1.357 6.283 6.283 0 0 0-2.544-.49 6.35 6.35 0 0 0-2.405.457 6.007 6.007 0 0 0-1.963 1.276 6.142 6.142 0 0 0-1.325 1.94 5.862 5.862 0 0 0-.466 1.864h-.063a5.857 5.857 0 0 0-.467-1.865 6.13 6.13 0 0 0-1.325-1.939A6 6 0 0 0 8.21 6.34a6.698 6.698 0 0 0-4.949.031A5.708 5.708 0 0 0 1.34 7.73l1.52 1.49a4.166 4.166 0 0 1 4.484-.958c.47.184.898.46 1.26.81.368.36.66.792.859 1.268.146.344.242.708.285 1.08l-9.635.008A4.714 4.714 0 0 0 0 12.457a6.493 6.493 0 0 0 .345 2.127 4.927 4.927 0 0 0 1.08 1.783c.528.56 1.17 1 1.88 1.293a6.454 6.454 0 0 0 2.504.457c.824.005 1.64-.15 2.404-.457a5.986 5.986 0 0 0 1.964-1.277 6.116 6.116 0 0 0 1.686-3.076h.273a6.13 6.13 0 0 0 1.686 3.077 5.99 5.99 0 0 0 1.964 1.276 6.345 6.345 0 0 0 2.405.457 6.45 6.45 0 0 0 2.502-.457 5.42 5.42 0 0 0 1.882-1.293 4.928 4.928 0 0 0 1.08-1.783A6.52 6.52 0 0 0 24 12.457a4.757 4.757 0 0 0-.039-.554z"/>
    </svg>
  `;

  // Load user settings from chrome.storage
  function loadSettings() {
    if (typeof chrome !== 'undefined' && chrome.storage && chrome.storage.sync) {
      chrome.storage.sync.get(['showLeetcode', 'showGfg'], (res) => {
        if (res.showLeetcode !== undefined) settings.showLeetcode = res.showLeetcode;
        if (res.showGfg !== undefined) settings.showGfg = res.showGfg;
        updateExistingBadgesVisibility();
      });

      chrome.storage.onChanged.addListener((changes) => {
        if (changes.showLeetcode) settings.showLeetcode = changes.showLeetcode.newValue;
        if (changes.showGfg) settings.showGfg = changes.showGfg.newValue;
        updateExistingBadgesVisibility();
      });
    }
  }

  function updateExistingBadgesVisibility() {
    document.querySelectorAll('.cheatcode-btn-leetcode').forEach(el => {
      el.style.display = settings.showLeetcode ? 'inline-flex' : 'none';
    });
    document.querySelectorAll('.cheatcode-btn-gfg').forEach(el => {
      el.style.display = settings.showGfg ? 'inline-flex' : 'none';
    });
  }

  // Load the problems database
  async function initMatcher() {
    try {
      const url = chrome.runtime.getURL('data/problems.json');
      const response = await fetch(url);
      const data = await response.json();
      matcher = new window.CheatCodeMatcher.Matcher(data);
      console.log(`[CheatCode by brindoxx] Loaded ${data.length} problems into matching engine.`);
      scanAndInject();
    } catch (err) {
      console.error('[CheatCode] Failed to load problem database:', err);
    }
  }

  function createBadgeContainer(matchInfo) {
    if (!matchInfo) return null;

    const hasLeetcode = Boolean(matchInfo.leetcode);
    const hasGfg = Boolean(matchInfo.gfg);

    if (!hasLeetcode && !hasGfg) return null;

    const container = document.createElement('span');
    container.className = 'cheatcode-badge-container';

    // LeetCode Button - ONLY if problem exists directly on LeetCode
    if (hasLeetcode) {
      const lcBtn = document.createElement('a');
      lcBtn.className = 'cheatcode-btn cheatcode-btn-leetcode';
      lcBtn.href = matchInfo.leetcode;
      lcBtn.target = '_blank';
      lcBtn.rel = 'noopener noreferrer';
      lcBtn.title = `Solve "${matchInfo.title}" on LeetCode`;
      lcBtn.innerHTML = `${LEETCODE_SVG}<span>LeetCode</span>`;
      lcBtn.style.display = settings.showLeetcode ? 'inline-flex' : 'none';
      
      // Stop event propagation so row click / accordion doesn't toggle
      lcBtn.addEventListener('click', (e) => e.stopPropagation());
      container.appendChild(lcBtn);
    }

    // GeeksforGeeks Button - ONLY if problem exists directly on GeeksforGeeks
    if (hasGfg) {
      const gfgBtn = document.createElement('a');
      gfgBtn.className = 'cheatcode-btn cheatcode-btn-gfg';
      gfgBtn.href = matchInfo.gfg;
      gfgBtn.target = '_blank';
      gfgBtn.rel = 'noopener noreferrer';
      gfgBtn.title = `Solve "${matchInfo.title}" on GeeksforGeeks`;
      gfgBtn.innerHTML = `${GFG_SVG}<span>GFG</span>`;
      gfgBtn.style.display = settings.showGfg ? 'inline-flex' : 'none';

      gfgBtn.addEventListener('click', (e) => e.stopPropagation());
      container.appendChild(gfgBtn);
    }

    if (container.children.length === 0) return null;
    return container;
  }

  // Non-problem pages where CheatCode should never inject badges
  function isNonProblemPage() {
    const path = window.location.pathname.toLowerCase();
    return (
      path.startsWith('/leaderboard') ||
      path.startsWith('/profile') ||
      path.startsWith('/settings') ||
      path.startsWith('/login') ||
      path.startsWith('/register') ||
      path.startsWith('/signup') ||
      path.startsWith('/notifications') ||
      path.startsWith('/pricing') ||
      path.startsWith('/plus/pricing') ||
      path.startsWith('/community') ||
      path.startsWith('/coins')
    );
  }

  // Ignored common labels/texts and badge strings
  const IGNORED_STRINGS = new Set([
    'easy', 'medium', 'hard', 'basic', 'solved', 'unsolved', 'revision', 'notes',
    'status', 'problem', 'practice', 'editorial', 'submission', 'bookmark',
    'youtube', 'code', 'c++', 'java', 'python', 'javascript', 'submit', 'run',
    'dashboard', 'planly', 'prep hub', 'community', 'blogs', 'codespace',
    'core', 'must do', 'starred', 'optional', 'faq', 'faqs', 'article', 'video',
    'rank', 'learners', 'leaderboard', 'coins', 'trophies', 'titles', 'you'
  ]);

  function isIgnoredText(text) {
    const t = text.trim().toLowerCase();
    if (t.length < 2) return true;
    if (IGNORED_STRINGS.has(t)) return true;
    if (/^#?\d+$/.test(t)) return true; // Pure numbers or ranks: e.g. #10, 10
    if (/^#?\d+(st|nd|rd|th)$/i.test(t)) return true; // 1st, 2nd, 3rd, #10th
    if (/^@[a-z0-9_.-]+$/i.test(t)) return true; // User handles like @tanyaag31
    if (/^\d+(\.\d+)?[kmb]?\s*(coins?|pts?|points?|xp|per\s*page)?$/i.test(t)) return true; // 650, 1.1k coins, 10 per page
    if (/^page\s*\d+$/i.test(t)) return true; // Page 1, Page 2
    if (/^\d+(\.\d+)?%$/.test(t)) return true; // Accuracy percentage
    return false;
  }

  function processRow(row) {
    if (row.hasAttribute('data-cheatcode-injected')) return;

    // Check if we already injected our badge container inside this row
    if (row.querySelector('.cheatcode-badge-container')) {
      row.setAttribute('data-cheatcode-injected', 'true');
      return;
    }

    // Skip rows located in leaderboards, user profiles, or ranking tables
    if (row.closest('[class*="leaderboard"], [class*="Leaderboard"], [class*="ranking"], [class*="rank"]')) {
      row.setAttribute('data-cheatcode-injected', 'true');
      return;
    }

    const titleCandidates = row.querySelectorAll('span[class*="problemLabel"], td[data-label="Problem"] div, a, p, span, h3, h4');
    let matchedEl = null;
    let matchInfo = null;

    for (const el of titleCandidates) {
      if (el.closest('.cheatcode-badge-container')) continue;
      // Skip rank badges or username containers
      if (el.closest('[class*="rank"], [class*="learner"], [class*="coin"], [class*="avatar"]')) continue;

      // Strategy A: If element has an href, extract problem slug
      const href = el.getAttribute('href');
      if (href) {
        const slugMatch = href.match(/(?:problems|data-structure|practice\/dsa)\/([a-z0-9-_]+)/i);
        if (slugMatch && slugMatch[1]) {
          const slugText = slugMatch[1].replace(/[-_]+/g, ' ');
          const found = matcher.find(slugText);
          if (found) {
            matchedEl = el;
            matchInfo = found;
            break;
          }
        }
      }

      // Strategy B: Inspect element textContent
      // If element has child elements with difficulty badges, prune them for clean title extraction
      let rawTxt = '';
      if (el.children.length > 0) {
        const clone = el.cloneNode(true);
        clone.querySelectorAll('[class*="Badge"], [class*="badge"], span, div').forEach(child => {
          const cTxt = child.textContent.trim().toLowerCase();
          if (IGNORED_STRINGS.has(cTxt) || /^(core|basic|easy|medium|hard|solved|unsolved)$/i.test(cTxt)) {
            child.remove();
          }
        });
        rawTxt = clone.textContent.trim();
      }
      if (!rawTxt) {
        rawTxt = el.textContent.trim();
      }

      if (rawTxt && !isIgnoredText(rawTxt) && rawTxt.length >= 3 && rawTxt.length <= 140) {
        // Strip out trailing or leading status/badge tags like "Core", "Basic", "Solved", "Easy", etc.
        // Handles both spaced ("Traversal Core") and unspaced ("TraversalCore") concatenations
        const cleanedTxt = rawTxt
          .replace(/(?:[\s_-]*|\b)(core|basic|easy|medium|hard|must do|starred|revision|optional|notes|faqs?|solved|unsolved)\s*$/gi, '')
          .replace(/^\s*(core|basic|easy|medium|hard|must do|starred|revision|optional|notes|faqs?|solved|unsolved)(?:[\s_-]*|\b)/gi, '')
          .replace(/\s+/g, ' ')
          .trim();

        if (cleanedTxt.length >= 3 && !isIgnoredText(cleanedTxt)) {
          const found = matcher.find(cleanedTxt);
          if (found) {
            matchedEl = el;
            matchInfo = found;
            break;
          }
        }
      }
    }

    if (!matchedEl || !matchInfo) {
      // Debug: log unmatched rows to help identify remaining gaps
      const firstText = row.querySelector('a, p, span, h3, h4')?.textContent?.trim();
      if (firstText && firstText.length > 5 && firstText.length < 100 && !isIgnoredText(firstText)) {
        console.debug(`[CheatCode] No match for: "${firstText.substring(0, 80)}"`);
      }
      return;
    }

    const badgeContainer = createBadgeContainer(matchInfo);
    if (!badgeContainer) return;

    row.setAttribute('data-cheatcode-injected', 'true');

    // Place container right next to the matched title element
    if (matchedEl.parentNode) {
      if (matchedEl.nextSibling) {
        matchedEl.parentNode.insertBefore(badgeContainer, matchedEl.nextSibling);
      } else {
        matchedEl.parentNode.appendChild(badgeContainer);
      }
    } else {
      row.appendChild(badgeContainer);
    }
  }

  // Scan all potential problem containers
  function scanAndInject() {
    if (!matcher) return;
    if (isNonProblemPage()) return;

    // Potential problem rows across different TUF layouts
    const selectors = [
      'tr[data-sheet-row-key]',
      'tr[class*="contentTableRow"]',
      'tr[data-row-type="practice"]',
      'table tbody tr',
      'div[role="row"]',
      'div[class*="table_row"]',
      'div[class*="problem_row"]',
      'div[class*="problem-row"]',
      'div[class*="accordion"] div.cursor-pointer',
      'div[class*="border"] div.cursor-pointer',
      'li[class*="problem"]',
      'div[class*="sheet_item"]',
      'div[class*="sheet-item"]'
    ];

    const elements = document.querySelectorAll(selectors.join(', '));
    elements.forEach(processRow);

    // Also look for problem title on individual problem / editorial pages
    const mainTitle = document.querySelector('h1, h2.problem-title');
    if (mainTitle && !mainTitle.hasAttribute('data-cheatcode-injected')) {
      const titleText = mainTitle.textContent.trim();
      if (!isIgnoredText(titleText)) {
        const matchInfo = matcher.find(titleText);
        if (matchInfo) {
          const badgeContainer = createBadgeContainer(matchInfo);
          if (badgeContainer) {
            mainTitle.setAttribute('data-cheatcode-injected', 'true');
            mainTitle.appendChild(badgeContainer);
          }
        }
      }
    }
  }

  // Debounced observer to handle Next.js client-side dynamic rendering
  let debounceTimeout = null;
  const observer = new MutationObserver((mutations) => {
    let shouldScan = false;
    for (const m of mutations) {
      if (m.addedNodes.length > 0) {
        for (const node of m.addedNodes) {
          if (node.nodeType === 1 && !node.classList?.contains('cheatcode-badge-container')) {
            shouldScan = true;
            break;
          }
        }
      }
      if (shouldScan) break;
    }

    if (shouldScan) {
      clearTimeout(debounceTimeout);
      debounceTimeout = setTimeout(scanAndInject, 150);
    }
  });

  // Watch for page changes in SPA (History API)
  window.addEventListener('popstate', () => setTimeout(scanAndInject, 300));

  // Initialize
  loadSettings();
  initMatcher();

  // Start observing DOM changes once body is ready
  if (document.body) {
    observer.observe(document.body, { childList: true, subtree: true });
  } else {
    document.addEventListener('DOMContentLoaded', () => {
      observer.observe(document.body, { childList: true, subtree: true });
    });
  }

  // Periodic safety check to catch delayed accordion expansions
  setInterval(scanAndInject, 2000);

})();
