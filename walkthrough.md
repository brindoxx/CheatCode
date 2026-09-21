# Walkthrough: Fix Missing Tags & Misattributed Shortest Path Problem Links

## Root Cause Analysis
1. **Misattributed Links (Bellman Ford vs Cheapest Flights)**:
   - In `utils/generate_dataset.py`, `Bellman Ford Algorithm` had erroneously been assigned `leetcode: "https://leetcode.com/problems/cheapest-flights-within-k-stops/"`.
   - `Floyd Warshall Algorithm` had similarly been assigned `leetcode: "https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/"`.
   - As a result, when the extension parsed the sheet, Bellman Ford stole the LeetCode badge for Cheapest Flights, while the actual `Cheapest flight within K stops` problem was completely absent from the dataset.

2. **Missing Problems in "Shortest Path Algorithms"**:
   - The following 5 problems were missing from `generate_dataset.py` and `data/problems.json`:
     - `Print Shortest Path`
     - `Shortest Distance in a Binary Maze`
     - `Path with minimum effort`
     - `Cheapest flight within K stops`
     - `Minimum multiplications to reach end`
   - Furthermore, `Find the city with the smallest number of neighbors` did not have its own distinct problem entry.

3. **Incomplete Sheet Coverage Across All Modules**:
   - By extracting the live schema tree directly from `takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/`, we verified that Striver's sheet contains exactly **403 practice problems**.
   - The original dataset contained 351 problems, with various minor label discrepancies (e.g. `Insertion Sorting` vs `Insertion Sort`, `paranthesis` spelling, etc.).

---

## Changes Made

### 1. Fixed Problem Attribution & Links
- **Bellman Ford Algorithm**: Removed the wrong LeetCode link (`leetcode: None`), pointing directly to GFG (`https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1`).
- **Floyd Warshall Algorithm**: Removed the wrong LeetCode link (`leetcode: None`), pointing directly to GFG (`https://www.geeksforgeeks.org/problems/floyd-warshall4853/1`).
- **Cheapest Flights Within K Stops**: Added dedicated problem entry with LeetCode (`https://leetcode.com/problems/cheapest-flights-within-k-stops/`) and GFG (`https://www.geeksforgeeks.org/problems/cheapest-flights-within-k-stops/1`).
- **Shortest Distance in a Binary Maze**: Added dedicated problem entry with LeetCode (`https://leetcode.com/problems/shortest-path-in-binary-matrix/`) and GFG (`https://www.geeksforgeeks.org/problems/shortest-distance-in-a-binary-maze/1`).
- **Path with minimum effort**: Added dedicated problem entry with LeetCode (`https://leetcode.com/problems/path-with-minimum-effort/`) and GFG (`https://www.geeksforgeeks.org/problems/path-with-minimum-effort/1`).
- **Print Shortest Path**: Added dedicated problem entry with GFG (`https://www.geeksforgeeks.org/problems/shortest-path-in-weighted-undirected-graph/1`).
- **Minimum multiplications to reach end**: Added dedicated problem entry with GFG (`https://www.geeksforgeeks.org/problems/minimum-multiplications-to-reach-end/1`).
- **Find the city with the smallest number of neighbors**: Added dedicated problem entry with LeetCode (`https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/`) and GFG (`https://www.geeksforgeeks.org/problems/city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/1`).

### 2. Comprehensive 403 TUF Problem Integration
- Added all 403 TUF practice problems into `utils/generate_dataset.py` and `data/problems.json` (bringing total problem count to **476** curated problems with **336 direct LeetCode** links and **457 direct GFG** links).
- Every TUF problem label is included in `aliases` so queries match with 100% exact precision.

### 3. Normalization Enhancements in [scripts/matcher.js](file:///c:/Mrinal%20Subudhi/Projects/CheatCode/scripts/matcher.js)
- Added normalization rules for `zeroes` -> `zeros`, `paranthes(is|es)` -> `parentheses`, `minimi[sz]e` -> `minimize`, `maximi[sz]e` -> `maximize`, `behaviour` -> `behavior`, `traversals` -> `traversal`, and `occurrences` -> `occurrence`.

---

## Verification Results

### Shortest Path Algorithms Test
All 10 problems in the user's screenshot tested with badge suffixes (`Core`, `Pro`):
- `Dijkstra's algorithm Core` -> LeetCode & GFG ✓
- `Print Shortest Path Core` -> GFG ✓
- `Shortest Distance in a Binary Maze Core` -> LeetCode & GFG ✓
- `Path with minimum effort Core` -> LeetCode & GFG ✓
- `Cheapest flight within K stops Core` -> LeetCode & GFG ✓
- `Minimum multiplications to reach end Core` -> GFG ✓
- `Number of ways to arrive at destination Core` -> LeetCode & GFG ✓
- `Bellman ford algorithm Core` -> GFG ✓ (No longer mislinked to Cheapest Flights)
- `Floyd warshall algorithm Pro` -> GFG ✓ (No longer mislinked to Smallest Neighbors)
- `Find the city with the smallest number of neighbors Core` -> LeetCode & GFG ✓

### Overall Test
- **403 / 403** TUF practice problems match with 100% precision (0 failures).
- `npm test` passes cleanly.
- `npm run package` successfully refreshed `CheatCode.zip`.
