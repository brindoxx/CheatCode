/**
 * CheatCode - Extension Popup Logic
 * Author: brindoxx
 */

document.addEventListener('DOMContentLoaded', async () => {
  const toggleLeetcode = document.getElementById('toggle-leetcode');
  const toggleGfg = document.getElementById('toggle-gfg');
  const searchInput = document.getElementById('problem-search');
  const clearBtn = document.getElementById('clear-search');
  const resultsContainer = document.getElementById('search-results');
  const searchKbd = document.getElementById('search-kbd');
  const statTotal = document.getElementById('stat-total');
  const statLc = document.getElementById('stat-lc');
  const statGfg = document.getElementById('stat-gfg');
  const pageStatusTitle = document.getElementById('page-status-title');

  let problemsData = [];
  let matcher = null;

  // Official Simple Icons SVGs for mini buttons
  const LC_ICON_SVG = `<svg viewBox="0 0 24 24" width="11" height="11" fill="currentColor"><path d="M13.483 0a1.374 1.374 0 0 0-.961.438L7.116 6.226l-3.854 4.126a5.266 5.266 0 0 0-1.209 2.104 5.35 5.35 0 0 0-.125.513 5.527 5.527 0 0 0 .062 2.362 5.83 5.83 0 0 0 .349 1.017 5.938 5.938 0 0 0 1.271 1.818l4.277 4.193.039.038c2.248 2.165 5.852 2.133 8.063-.074l2.396-2.392c.54-.54.54-1.414.003-1.955a1.378 1.378 0 0 0-1.951-.003l-2.396 2.392a3.021 3.021 0 0 1-4.205.038l-.02-.019-4.276-4.193c-.652-.64-.972-1.469-.948-2.263a2.68 2.68 0 0 1 .066-.523 2.545 2.545 0 0 1 .619-1.164L9.13 8.114c1.058-1.134 3.204-1.27 4.43-.278l3.501 2.831c.593.48 1.461.387 1.94-.207a1.384 1.384 0 0 0-.207-1.943l-3.5-2.831c-.8-.647-1.766-1.045-2.774-1.202l2.015-2.158A1.384 1.384 0 0 0 13.483 0zm-2.866 12.815a1.38 1.38 0 0 0-1.38 1.382 1.38 1.38 0 0 0 1.38 1.382H20.79a1.38 1.38 0 0 0 1.38-1.382 1.38 1.38 0 0 0-1.38-1.382z"/></svg>`;

  const GFG_ICON_SVG = `<svg viewBox="0 0 24 24" width="11" height="11" fill="currentColor"><path d="M21.45 14.315c-.143.28-.334.532-.565.745a3.691 3.691 0 0 1-1.104.695 4.51 4.51 0 0 1-3.116-.016 3.79 3.79 0 0 1-2.135-2.078 3.571 3.571 0 0 1-.13-.353h7.418a4.26 4.26 0 0 1-.368 1.008zm-11.99-.654a3.793 3.793 0 0 1-2.134 2.078 4.51 4.51 0 0 1-3.117.016 3.7 3.7 0 0 1-1.104-.695 2.652 2.652 0 0 1-.564-.745 4.221 4.221 0 0 1-.368-1.006H9.59c-.038.12-.08.238-.13.352zm14.501-1.758a3.849 3.849 0 0 0-.082-.475l-9.634-.008a3.932 3.932 0 0 1 1.143-2.348c.363-.35.79-.625 1.26-.809a3.97 3.97 0 0 1 4.484.957l1.521-1.49a5.7 5.7 0 0 0-1.922-1.357 6.283 6.283 0 0 0-2.544-.49 6.35 6.35 0 0 0-2.405.457 6.007 6.007 0 0 0-1.963 1.276 6.142 6.142 0 0 0-1.325 1.94 5.862 5.862 0 0 0-.466 1.864h-.063a5.857 5.857 0 0 0-.467-1.865 6.13 6.13 0 0 0-1.325-1.939A6 6 0 0 0 8.21 6.34a6.698 6.698 0 0 0-4.949.031A5.708 5.708 0 0 0 1.34 7.73l1.52 1.49a4.166 4.166 0 0 1 4.484-.958c.47.184.898.46 1.26.81.368.36.66.792.859 1.268.146.344.242.708.285 1.08l-9.635.008A4.714 4.714 0 0 0 0 12.457a6.493 6.493 0 0 0 .345 2.127 4.927 4.927 0 0 0 1.08 1.783c.528.56 1.17 1 1.88 1.293a6.454 6.454 0 0 0 2.504.457c.824.005 1.64-.15 2.404-.457a5.986 5.986 0 0 0 1.964-1.277 6.116 6.116 0 0 0 1.686-3.076h.273a6.13 6.13 0 0 0 1.686 3.077 5.99 5.99 0 0 0 1.964 1.276 6.345 6.345 0 0 0 2.405.457 6.45 6.45 0 0 0 2.502-.457 5.42 5.42 0 0 0 1.882-1.293 4.928 4.928 0 0 0 1.08-1.783A6.52 6.52 0 0 0 24 12.457a4.757 4.757 0 0 0-.039-.554z"/></svg>`;

  // 1. Sync Settings with Chrome Storage
  if (typeof chrome !== 'undefined' && chrome.storage && chrome.storage.sync) {
    chrome.storage.sync.get(['showLeetcode', 'showGfg'], (res) => {
      if (res.showLeetcode !== undefined) toggleLeetcode.checked = res.showLeetcode;
      if (res.showGfg !== undefined) toggleGfg.checked = res.showGfg;
    });

    toggleLeetcode.addEventListener('change', () => {
      chrome.storage.sync.set({ showLeetcode: toggleLeetcode.checked });
    });

    toggleGfg.addEventListener('change', () => {
      chrome.storage.sync.set({ showGfg: toggleGfg.checked });
    });
  }

  // 2. Active Tab Detection
  if (typeof chrome !== 'undefined' && chrome.tabs && chrome.tabs.query) {
    try {
      chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
        if (tabs && tabs[0] && tabs[0].url) {
          const currentUrl = tabs[0].url;
          if (currentUrl.includes('takeuforward.org')) {
            if (pageStatusTitle) {
              pageStatusTitle.textContent = 'Active on this Tab';
              const liveDot = document.querySelector('.live-dot');
              if (liveDot) {
                liveDot.style.backgroundColor = '#10b981';
                liveDot.style.boxShadow = '0 0 8px rgba(16, 185, 129, 0.8)';
              }
            }
          }
        }
      });
    } catch (e) {}
  }

  // 3. Load Problem Database & Update Metrics
  try {
    const response = await fetch(chrome.runtime.getURL('data/problems.json'));
    problemsData = await response.json();
    matcher = new window.CheatCodeMatcher.Matcher(problemsData);

    // Update dynamic stats
    if (statTotal) statTotal.textContent = problemsData.length;
    if (searchInput) searchInput.placeholder = `Search ${problemsData.length} Striver problems...`;
    if (statLc) {
      const lcCount = problemsData.filter(p => p.leetcode && p.leetcode.includes('leetcode.com/problems/')).length;
      statLc.textContent = lcCount;
    }
    if (statGfg) {
      const gfgCount = problemsData.filter(p => p.gfg && (p.gfg.includes('geeksforgeeks.org/problems/') || p.gfg.includes('practice.geeksforgeeks.org/problems/'))).length;
      statGfg.textContent = gfgCount;
    }
  } catch (err) {
    console.error('[CheatCode Popup] Error loading database:', err);
  }

  // 4. Search Handler
  function performSearch() {
    const query = searchInput.value.trim().toLowerCase();

    if (!query) {
      resultsContainer.innerHTML = '';
      resultsContainer.classList.remove('active');
      clearBtn.style.display = 'none';
      if (searchKbd) searchKbd.style.display = 'block';
      return;
    }

    clearBtn.style.display = 'block';
    if (searchKbd) searchKbd.style.display = 'none';

    // Search across primary titles, topics, and aliases
    const matches = problemsData.filter(p => {
      if (p.title.toLowerCase().includes(query)) return true;
      if (p.topic && p.topic.toLowerCase().includes(query)) return true;
      if (Array.isArray(p.aliases) && p.aliases.some(a => a.toLowerCase().includes(query))) return true;
      return false;
    }).slice(0, 10);

    resultsContainer.innerHTML = '';

    if (matches.length === 0) {
      const emptyDiv = document.createElement('div');
      emptyDiv.className = 'result-item';
      emptyDiv.style.cursor = 'default';
      emptyDiv.style.justifyContent = 'center';
      emptyDiv.innerHTML = `
        <div class="result-info" style="align-items: center; text-align: center; max-width: none;">
          <span class="result-title" style="color: var(--text-muted);">No matching problems found</span>
          <span class="result-topic">Try another keyword or topic</span>
        </div>
      `;
      resultsContainer.appendChild(emptyDiv);
    } else {
      matches.forEach(p => {
        const hasLc = p.leetcode && p.leetcode.includes('leetcode.com/problems/');
        const hasGfg = p.gfg && (p.gfg.includes('geeksforgeeks.org/problems/') || p.gfg.includes('practice.geeksforgeeks.org/problems/'));

        const diff = (p.difficulty || 'medium').toLowerCase();
        const diffClass = diff === 'easy' ? 'diff-easy' : (diff === 'hard' ? 'diff-hard' : 'diff-medium');

        const item = document.createElement('div');
        item.className = 'result-item';
        item.innerHTML = `
          <div class="result-info">
            <span class="result-title" title="${escapeHtml(p.title)}">${escapeHtml(p.title)}</span>
            <div class="result-meta">
              <span class="diff-pill ${diffClass}">${escapeHtml(p.difficulty || 'Medium')}</span>
              <span class="result-topic" title="${escapeHtml(p.topic || '')}">${escapeHtml(p.topic || '')}</span>
            </div>
          </div>
          <div class="result-actions">
            ${hasLc ? `<a href="${p.leetcode}" target="_blank" rel="noopener noreferrer" class="mini-btn mini-btn-lc" title="Solve on LeetCode">${LC_ICON_SVG}<span>LC</span></a>` : ''}
            ${hasGfg ? `<a href="${p.gfg}" target="_blank" rel="noopener noreferrer" class="mini-btn mini-btn-gfg" title="Solve on GeeksforGeeks">${GFG_ICON_SVG}<span>GFG</span></a>` : ''}
          </div>
        `;
        resultsContainer.appendChild(item);
      });
    }

    resultsContainer.classList.add('active');
  }

  function escapeHtml(str) {
    if (!str) return '';
    return str
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  searchInput.addEventListener('input', performSearch);

  clearBtn.addEventListener('click', () => {
    searchInput.value = '';
    performSearch();
    searchInput.focus();
  });

  // 5. Global Keyboard Shortcuts (/ to search, Esc to clear)
  document.addEventListener('keydown', (e) => {
    if (e.key === '/' && document.activeElement !== searchInput) {
      e.preventDefault();
      searchInput.focus();
      searchInput.select();
    } else if (e.key === 'Escape' && document.activeElement === searchInput) {
      searchInput.value = '';
      performSearch();
      searchInput.blur();
    }
  });
});
