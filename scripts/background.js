/**
 * CheatCode - Background Service Worker
 * Author: brindoxx
 */

chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === 'install') {
    // Set default preferences
    chrome.storage.sync.set({
      showLeetcode: true,
      showGfg: true
    });
    console.log('[CheatCode by brindoxx] Extension installed successfully!');
  }
});
