# ⚡ CheatCode

<div align="center">

![CheatCode Banner](https://img.shields.io/badge/CheatCode-Striver%20Sheet%20Restorer-FFA116?style=for-the-badge&logo=code&logoColor=black)

**Restore direct LeetCode & GeeksforGeeks practice links beside every problem on Striver's A2Z DSA Sheet.**

[![Manifest V3](https://img.shields.io/badge/Manifest-V3-3b82f6?style=flat-square&logo=google-chrome&logoColor=white)](https://developer.chrome.com/docs/extensions/mv3/intro/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Platforms Supported](https://img.shields.io/badge/Target-takeuforward.org-orange?style=flat-square)](https://takeuforward.org)
[![Offline Database](https://img.shields.io/badge/Problems%20Mapped-340%2B-blueviolet?style=flat-square)](data/problems.json)
[![Author](https://img.shields.io/badge/Dev-brindoxx-ff69b4?style=flat-square&logo=github)](https://github.com/brindoxx)

[Installation](#-installation-guide-100-free) • [Features](#-key-features) • [How It Works](#-how-it-works) • [Popup Problem Finder](#-instant-popup-problem-finder) • [Contributing](#-contributing)

</div>

---

## 🎯 The Problem

When preparing for campus placements and technical interviews, thousands of developers rely on **Striver's A2Z DSA Sheet** hosted on [takeuforward.org](https://takeuforward.org). 

In a recent platform redesign, **direct external links to LeetCode and GeeksforGeeks were removed from problem sheets** in favor of internal site features. Learners who want to maintain their LeetCode streaks, run test cases against LeetCode's judge, or view company tags on GFG are left manually copying problem names into Google every time.

## 🚀 The Solution: CheatCode

**CheatCode** is a lightweight, high-performance browser extension (Manifest V3) created by **[brindoxx](https://github.com/brindoxx)** that:
- Seamlessly injects sleek **[🟧 LeetCode]** and **[🟩 GFG]** badges directly beside every problem row on TakeUForward.
- Works dynamically with Single-Page Applications (Next.js client-side routing and accordion expansions).
- Ships with an embedded offline database of 340+ canonical Striver problems.
- Features an **instant search popup** so you can find and launch any DSA problem without even visiting TakeUForward.
- Requires **zero external server requests**, respects your privacy, and runs 100% locally.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🟧 **Direct LeetCode Badges** | Opens the exact canonical LeetCode problem with 1 click. |
| 🟩 **Direct GFG Badges** | Opens the corresponding GeeksforGeeks practice problem. |
| 🔄 **SPA / Next.js Observer** | Automatically detects newly expanded accordions and tab transitions without page reloads. |
| 🔍 **Smart Fallback Engine** | If a new question is added by Striver, it intelligently generates direct search URLs so you are never stuck. |
| ⚡ **Offline Problem Finder** | Search 340+ A2Z questions instantly from the extension popup. |
| 🎨 **Theme Adaptive** | Automatically adapts to TakeUForward's light and dark modes. |
| 🔒 **100% Private & Open Source** | Zero data collection, no telemetry, no tracking. |

---

## 📦 Installation Guide (100% Free)

You do **not** need to wait for a store approval or pay any fees to use CheatCode. You can install it right now in 30 seconds:

### Method 1: Load Unpacked (Chrome / Edge / Brave / Opera)

1. **Download CheatCode**:
   - Clone this repository:
     ```bash
     git clone https://github.com/brindoxx/CheatCode.git
     ```
   - *Or* download the repository as a `.ZIP` from the top green **Code** button and extract it.

2. **Open Extensions Management**:
   - In Google Chrome, go to `chrome://extensions/`
   - In Microsoft Edge, go to `edge://extensions/`
   - In Brave, go to `brave://extensions/`

3. **Enable Developer Mode**:
   - Toggle on the **Developer mode** switch in the top right corner.

4. **Load the Extension**:
   - Click the **Load unpacked** button in the top left.
   - Select the folder containing `manifest.json` (e.g. `CheatCode`).

5. **Start Practicing**:
   - Navigate to [takeuforward.org/prep-hub/strivers-a2z-dsa-sheet?page=sheet](https://takeuforward.org/prep-hub/strivers-a2z-dsa-sheet?page=sheet).
   - Expand any module (Arrays, Binary Search, DP, Trees).
   - Enjoy your direct **LeetCode** and **GFG** buttons! 🎉

---

### Method 2: Tampermonkey Userscript (Single Click)

If you already use **Tampermonkey** or **Violentmonkey**:
1. Open [`cheatcode.user.js`](cheatcode.user.js).
2. Click **Raw** to trigger Tampermonkey's auto-installer.
3. Click **Install**. Done!

---

## 🔍 Instant Popup Problem Finder

Can't remember which step contains "Trapping Rain Water" or "Longest Consecutive Sequence"? 

Click the **CheatCode** icon in your browser toolbar to launch the quick finder:
- Type any keyword (e.g. `Two Sum`, `LCS`, `Graph`).
- Instant fuzzy search across all 19 Steps.
- Launch directly into LeetCode or GFG without opening any other tabs.
- Toggle platform badges on or off according to your preference.

---

## 🛠️ Project Structure

```
CheatCode/
├── manifest.json              # Chrome Extension Manifest V3 configuration
├── data/
│   └── problems.json          # Master offline database of 340+ mapped problems
├── scripts/
│   ├── content.js             # High-performance DOM observer & badge injection
│   ├── matcher.js             # Normalization & fuzzy matching engine
│   └── background.js          # Background service worker (settings management)
├── styles/
│   ├── content.css            # Styles & dark-mode adaptations for injected badges
│   └── popup.css              # Dark glassmorphism popup UI stylesheet
├── popup/
│   ├── popup.html             # Extension popup interface
│   └── popup.js               # Popup search & Chrome storage sync
├── icons/
│   ├── icon16.png
│   ├── icon32.png
│   ├── icon48.png
│   └── icon128.png
├── utils/
│   ├── generate_dataset.py    # Python script to compile problem database
│   ├── generate_icons.py      # Script to render branded icons
│   └── package.ps1            # 1-click packager for CheatCode.zip
├── cheatcode.user.js          # Standalone Tampermonkey userscript alternative
├── README.md                  # Project documentation
└── LICENSE                    # MIT License
```

---

## 🧪 Testing & Verification

CheatCode comes with built-in sanity checks:

```bash
# Run matcher verification
npm test
```

To build a fresh release zip for distribution:
```powershell
npm run package
```
This generates `CheatCode.zip` at the project root ready for distribution.

---

## 🤝 Contributing

Contributions are warmly welcomed! If you find a problem title that didn't match or want to add direct links for new sheets:

1. Fork the Project.
2. Add the problem mapping into `utils/generate_dataset.py`.
3. Run `python utils/generate_dataset.py`.
4. Commit your changes and open a Pull Request.

---

## 📜 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more details.

---

<div align="center">

Crafted with dedication by **[brindoxx](https://github.com/brindoxx)**  
*If CheatCode helped you with your DSA preparation, please consider giving it a ⭐ star!*

</div>
