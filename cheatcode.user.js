// ==UserScript==
// @name         CheatCode - Striver Sheet LeetCode & GFG Links
// @namespace    https://github.com/brindoxx/CheatCode
// @version      2.0.0
// @description  Restores direct LeetCode and GeeksforGeeks buttons beside every problem on Striver's A2Z DSA Sheet (takeuforward.org).
// @author       brindoxx
// @match        *://takeuforward.org/*
// @grant        GM_xmlhttpRequest
// @run-at       document-idle
// ==/UserScript==

(function () {
  'use strict';

  console.log('[CheatCode Userscript by brindoxx] Running...');

  // CSS injection
  const style = document.createElement('style');
  style.textContent = `
    .cheatcode-badge-container {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin-left: 10px;
      vertical-align: middle;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      user-select: none;
    }
    .cheatcode-btn {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 3px 8px;
      font-size: 11.5px;
      font-weight: 600;
      line-height: 1;
      text-decoration: none !important;
      border-radius: 6px;
      transition: all 0.2s ease;
      box-shadow: 0 1px 3px rgba(0,0,0,0.12);
      white-space: nowrap;
    }
    .cheatcode-btn-lc {
      background: #ffffff;
      color: #1a1a1a !important;
      border: 1px solid #e2e8f0;
    }
    .cheatcode-btn-lc:hover {
      background: #fff7ed;
      color: #ea580c !important;
      border-color: #fdba74;
      transform: translateY(-1px);
    }
    .cheatcode-btn-gfg {
      background: #ffffff;
      color: #1a1a1a !important;
      border: 1px solid #e2e8f0;
    }
    .cheatcode-btn-gfg:hover {
      background: #f0fdf4;
      color: #16a34a !important;
      border-color: #86efac;
      transform: translateY(-1px);
    }
    @media (prefers-color-scheme: dark), [data-theme='dark'], .dark {
      .cheatcode-btn-lc, .cheatcode-btn-gfg {
        background: #262626;
        color: #f5f5f5 !important;
        border-color: #404040;
      }
      .cheatcode-btn-lc:hover {
        background: #431407;
        color: #fb923c !important;
        border-color: #ea580c;
      }
      .cheatcode-btn-gfg:hover {
        background: #052e16;
        color: #4ade80 !important;
        border-color: #22c55e;
      }
    }
  `;
  document.head.appendChild(style);

  function normalize(str) {
    return str
      .replace(/^(step\s*\d+(\.\d+)?[:\-]?\s*)/i, '')
      .replace(/^(day\s*\d+[:\-]?\s*)/i, '')
      .replace(/^(q\s*\d+[\.\:\-]?\s*)/i, '')
      .replace(/^(\d+[\.\:\-]\s*)/, '')
      .replace(/\s*(\(|\[)(leetcode|gfg|codechef|interviewbit|easy|medium|hard|editorial)(\)|\])/gi, '')
      .trim();
  }

  function injectRow(row) {
    if (row.hasAttribute('data-cheatcode-injected')) return;

    const candidates = row.querySelectorAll('a, p, span, h3, h4');
    let titleEl = null;
    let titleText = '';

    for (const el of candidates) {
      if (el.closest('.cheatcode-badge-container')) continue;
      const txt = el.textContent.trim();
      if (txt.length >= 3 && txt.length <= 120 && !/^(easy|medium|hard|solved|notes|status)$/i.test(txt)) {
        titleEl = el;
        titleText = txt;
        break;
      }
    }

    if (!titleEl || !titleText) return;

    row.setAttribute('data-cheatcode-injected', 'true');
    const cleanTitle = normalize(titleText);

    const span = document.createElement('span');
    span.className = 'cheatcode-badge-container';

    const lcUrl = `https://leetcode.com/problemset/?search=${encodeURIComponent(cleanTitle)}`;
    const gfgUrl = `https://www.geeksforgeeks.org/search/?q=${encodeURIComponent(cleanTitle)}`;

    span.innerHTML = `
      <a href="${lcUrl}" target="_blank" rel="noopener noreferrer" class="cheatcode-btn cheatcode-btn-lc" title="Search on LeetCode">🟧 LC</a>
      <a href="${gfgUrl}" target="_blank" rel="noopener noreferrer" class="cheatcode-btn cheatcode-btn-gfg" title="Search on GeeksforGeeks">🟩 GFG</a>
    `;

    span.querySelectorAll('a').forEach(a => a.addEventListener('click', (e) => e.stopPropagation()));

    if (titleEl.nextSibling) {
      titleEl.parentNode.insertBefore(span, titleEl.nextSibling);
    } else {
      titleEl.parentNode.appendChild(span);
    }
  }

  function scan() {
    const rows = document.querySelectorAll('table tbody tr, div[role="row"], div[class*="table_row"], div[class*="problem_row"], div[class*="accordion"] div.cursor-pointer, div[class*="border"] div.cursor-pointer');
    rows.forEach(injectRow);
  }

  const observer = new MutationObserver(scan);
  if (document.body) {
    observer.observe(document.body, { childList: true, subtree: true });
    scan();
  } else {
    document.addEventListener('DOMContentLoaded', () => {
      observer.observe(document.body, { childList: true, subtree: true });
      scan();
    });
  }

  setInterval(scan, 2500);
})();
