# ⚡ CheatCode

<div align="center">

![CheatCode Banner](https://img.shields.io/badge/CheatCode-Striver%20Sheet%20Restorer-FFA116?style=for-the-badge&logo=code&logoColor=black)

**Restore direct LeetCode & GeeksforGeeks practice links beside every problem on Striver's A2Z DSA Sheet.**

[![Version](https://img.shields.io/badge/Version-v2.1.0-10b981?style=flat-square)](https://github.com/brindoxx/CheatCode/releases)
[![Manifest V3](https://img.shields.io/badge/Manifest-V3-3b82f6?style=flat-square&logo=google-chrome&logoColor=white)](https://developer.chrome.com/docs/extensions/mv3/intro/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](LICENSE)
[![Platforms Supported](https://img.shields.io/badge/Target-takeuforward.org-orange?style=flat-square)](https://takeuforward.org)
[![Offline Database](https://img.shields.io/badge/Problems%20Mapped-403%20(100%25%20A2Z)-blueviolet?style=flat-square)](data/problems.json)
[![Author](https://img.shields.io/badge/Dev-brindoxx-ff69b4?style=flat-square&logo=github)](https://github.com/brindoxx)

[Installation](#-installation-guide-100-free) • [Features](#-key-features) • [Why CheatCode?](#-why-cheatcode) • [Popup Problem Finder](#-instant-popup-problem-finder) • [Contributing](#-contributing)

</div>

---

## 🎯 Why CheatCode?

When preparing for campus placements and technical interviews, thousands of developers rely on **Striver's A2Z DSA Sheet** hosted on [takeuforward.org](https://takeuforward.org).

### 💡 Current State of TakeUForward
TakeUForward recently restored direct LeetCode links for many problems on their platform. However, key gaps remain:
- 🟩 **GeeksforGeeks (GFG) links are still NOT added:** TUF still does not offer direct GeeksforGeeks links. For campus placement preparation, company-tagged questions, and alternative practice environments, GFG remains indispensable for students.
- 🟧 **Missing & incomplete LeetCode links:** Several problems on TUF still lack direct LeetCode links or direct problem mappings.
- ⚡ **Nested navigation friction:** Finding and jumping to a specific problem still requires expanding multiple steps and accordions on TUF.

---

## 🚀 The Solution: CheatCode

**CheatCode** is a lightweight, high-performance browser extension (Manifest V3) created by **[brindoxx](https://github.com/brindoxx)** that bridges every gap:
- **Complete GeeksforGeeks Coverage**: Injects **400 verified direct GFG links** across the sheet where TUF has none.
- **LeetCode Gap Filler**: Ensures canonical LeetCode links (**315 mapped problems**) even for questions where TUF's links are missing or omitted.
- **Unified Dual-Badge UI**: Seamlessly injects sleek **[🟧 LeetCode]** and **[🟩 GFG]** badges directly beside every problem row on TakeUForward.
- **Instant Search Popup (`/`)**: Built-in popup search lets you find and launch any A2Z question in milliseconds without even navigating TakeUForward.
- **Dynamic SPA Support**: Automatically detects newly expanded accordions and tab transitions without page reloads.
- **100% Offline & Private**: Zero external server calls, zero telemetry, lightning-fast execution.

> **ℹ️ Note on Problem Counts:** Striver's TakeUForward dashboard shows **442 total items** in its progress tracker. Out of these, exactly **403 are interactive coding problems** with code editors and test cases. The remaining 39 items are reading tutorials and theory guides (*"Learn C++"*, *"Time Complexity"*, *"C++ STL"*, etc.) which do not have practice coding pages. CheatCode maps 100% of all 403 practice coding problems.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🟩 **Complete GFG Links** | Injects 400 verified direct GeeksforGeeks practice links (which TUF still does not provide). |
| 🟧 **LeetCode Gap Filler** | Provides direct LeetCode links, including questions where TUF's links are missing. |
| 🔄 **SPA / Next.js Observer** | Automatically detects newly expanded accordions and tab transitions without page reloads. |
| 🎯 **Direct Links Only** | Strictly links to verified practice problems—if a problem does not exist on a platform, it is cleanly omitted without useless search redirects. |
| ⚡ **Offline Problem Finder** | Search all 403 A2Z questions instantly from the extension popup (hotkey `/`). |
| 🎨 **Theme Adaptive** | Automatically adapts to TakeUForward's light and dark modes. |
| 🔒 **100% Private & Open Source** | Zero data collection, no telemetry, no tracking. |

---

## 📦 Installation Guide (100% Free)

You do **not** need to wait for a store approval or pay any fees to use CheatCode. You can install it right now in 30 seconds:

### Load Unpacked (Chrome / Edge / Brave / Opera)

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
│   └── problems.json          # Master offline database of 403 canonical A2Z problems
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
