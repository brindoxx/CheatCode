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

  // SVGs for clean branded icons
  const LEETCODE_SVG = `
    <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor">
      <path fill="#FFA116" d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.83 5.83 0 0 0 .349 1.017 5.938 5.938 0 0 0 4.862 3.754 6.257 6.257 0 0 0 2.21-.088 6.46 6.46 0 0 0 2.203-.988l4.498-3.923a1.374 1.374 0 0 0 .438-.961 1.374 1.374 0 0 0-1.374-1.374 1.374 1.374 0 0 0-.961.438l-4.498 3.923a3.687 3.687 0 0 1-1.258.563 3.513 3.513 0 0 1-1.242.049 3.208 3.208 0 0 1-2.632-2.032 2.977 2.977 0 0 1-.188-.55 3.037 3.037 0 0 1-.034-1.298 2.87 2.87 0 0 1 .659-1.147l3.854-4.126 5.406-5.788A1.374 1.374 0 0 0 14.857 1.374 1.374 1.374 0 0 0 13.483 0z"/>
      <path fill="#262626" d="M18.824 10.667h-7.648a1.374 1.374 0 1 0 0 2.748h7.648a1.374 1.374 0 1 0 0-2.748z"/>
    </svg>
  `;

  const GFG_SVG = `
    <svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor">
      <path fill="#2F8D46" d="M19.167 15.632a6.47 6.47 0 0 1-2.227 2.012 6.81 6.81 0 0 1-3.23.774 7.02 7.02 0 0 1-5.109-2.062 7.06 7.06 0 0 1-2.091-5.112c0-2.006.697-3.708 2.091-5.106a7.02 7.02 0 0 1 5.109-2.062c1.233 0 2.32.261 3.26.783a6.438 6.438 0 0 1 2.227 2.062l-2.616 2.042c-.672-.888-1.637-1.332-2.895-1.332-1.077 0-1.996.386-2.756 1.157-.76.772-1.14 1.704-1.14 2.796 0 1.092.38 2.024 1.14 2.796.76.772 1.679 1.157 2.756 1.157 1.115 0 2.006-.358 2.673-1.075v-1.66h-2.673v-2.74h5.685v5.566z"/>
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

  // Ignored common labels/texts
  const IGNORED_STRINGS = new Set([
    'easy', 'medium', 'hard', 'solved', 'unsolved', 'revision', 'notes',
    'status', 'problem', 'practice', 'editorial', 'submission', 'bookmark',
    'youtube', 'code', 'c++', 'java', 'python', 'javascript', 'submit', 'run',
    'dashboard', 'planly', 'prep hub', 'community', 'blogs', 'codespace'
  ]);

  function isIgnoredText(text) {
    const t = text.trim().toLowerCase();
    if (t.length < 3) return true;
    if (IGNORED_STRINGS.has(t)) return true;
    if (/^\d+(\.\d+)?%$/.test(t)) return true; // Accuracy percentage
    return false;
  }

  function processRow(row) {
    if (row.hasAttribute('data-cheatcode-injected')) return;

    // Strategy 1: Find link or title element inside row
    const titleCandidates = row.querySelectorAll('a, p, span, h3, h4');
    let titleEl = null;
    let problemTitle = '';

    for (const el of titleCandidates) {
      // Don't inspect our own elements or badges
      if (el.closest('.cheatcode-badge-container')) continue;
      
      const txt = el.textContent.trim();
      if (!isIgnoredText(txt) && txt.length >= 3 && txt.length <= 120) {
        // Prefer anchors with problem URLs or elements with meaningful text
        if (el.tagName === 'A' || /^[A-Z0-9]/.test(txt)) {
          titleEl = el;
          problemTitle = txt;
          break;
        }
      }
    }

    if (!titleEl || !problemTitle) return;

    const matchInfo = matcher.find(problemTitle);
    if (!matchInfo) return;

    const badgeContainer = createBadgeContainer(matchInfo);
    if (!badgeContainer) return;

    row.setAttribute('data-cheatcode-injected', 'true');

    // Place container right next to the title or inside the title's parent
    if (titleEl.parentNode) {
      // If titleEl is an anchor or inline span, insert right after it
      if (titleEl.nextSibling) {
        titleEl.parentNode.insertBefore(badgeContainer, titleEl.nextSibling);
      } else {
        titleEl.parentNode.appendChild(badgeContainer);
      }
    } else {
      row.appendChild(badgeContainer);
    }
  }

  // Scan all potential problem containers
  function scanAndInject() {
    if (!matcher) return;

    // Potential problem rows across different TUF layouts
    const selectors = [
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
