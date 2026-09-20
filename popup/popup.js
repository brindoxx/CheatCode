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

  let problemsData = [];
  let matcher = null;

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

  // 2. Load Problem Database
  try {
    const response = await fetch(chrome.runtime.getURL('data/problems.json'));
    problemsData = await response.json();
    matcher = new window.CheatCodeMatcher.Matcher(problemsData);
  } catch (err) {
    console.error('[CheatCode Popup] Error loading database:', err);
  }

  // 3. Search Handler
  function performSearch() {
    const query = searchInput.value.trim().toLowerCase();
    
    if (!query) {
      resultsContainer.innerHTML = '';
      resultsContainer.classList.remove('active');
      clearBtn.style.display = 'none';
      return;
    }

    clearBtn.style.display = 'block';

    // Filter problems by title or topic
    const matches = problemsData.filter(p => {
      return p.title.toLowerCase().includes(query) || 
             p.topic.toLowerCase().includes(query);
    }).slice(0, 10); // Limit to top 10 results for compact display

    resultsContainer.innerHTML = '';

    if (matches.length === 0) {
      // Smart Fallback result
      const fallbackDiv = document.createElement('div');
      fallbackDiv.className = 'result-item';
      fallbackDiv.innerHTML = `
        <div class="result-info">
          <span class="result-title">${escapeHtml(query)}</span>
          <span class="result-topic">Search on platforms</span>
        </div>
        <div class="result-actions">
          <a href="https://leetcode.com/problemset/?search=${encodeURIComponent(query)}" target="_blank" class="mini-btn mini-btn-lc">LC</a>
          <a href="https://www.geeksforgeeks.org/search/?q=${encodeURIComponent(query)}" target="_blank" class="mini-btn mini-btn-gfg">GFG</a>
        </div>
      `;
      resultsContainer.appendChild(fallbackDiv);
    } else {
      matches.forEach(p => {
        const item = document.createElement('div');
        item.className = 'result-item';
        item.innerHTML = `
          <div class="result-info">
            <span class="result-title" title="${escapeHtml(p.title)}">${escapeHtml(p.title)}</span>
            <span class="result-topic">${escapeHtml(p.topic)} • ${escapeHtml(p.difficulty)}</span>
          </div>
          <div class="result-actions">
            ${p.leetcode ? `<a href="${p.leetcode}" target="_blank" class="mini-btn mini-btn-lc" title="Open in LeetCode">LC</a>` : ''}
            ${p.gfg ? `<a href="${p.gfg}" target="_blank" class="mini-btn mini-btn-gfg" title="Open in GeeksforGeeks">GFG</a>` : ''}
          </div>
        `;
        resultsContainer.appendChild(item);
      });
    }

    resultsContainer.classList.add('active');
  }

  function escapeHtml(str) {
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
});
