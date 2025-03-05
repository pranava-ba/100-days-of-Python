## 🎨 Intuition 
The problem involves expanding a colored region on a 2D grid over time. 

Observing the pattern, the number of colored cells at each step follows a quadratic sequence. 

This suggests that the problem can be solved mathematically rather than simulating the entire process. 

---

##  Grid Expansion Pattern
![Grid Expansion Visualization](https://assets.leetcode.com/uploads/2023/01/10/example-copy-2.png)

---

## 🚀 Approach
Instead of simulating the coloring process, we derive a precise formula:  
- At `n = 1`, only the center cell is colored (`1` cell). 🔴
- At `n = 2`, the pattern expands outward by 4, forming a cross (`5` cells). ➕
- At `n = 3`, the expansion continues outward, adding 8 more cells (`13` cells). 🌟

The pattern reveals a clear mathematical relationship:  

For a given step `n`, the total number of colored cells `f(n)` can be expressed as:
`f(n)` = 1 + 2n(n-1) = `2n² - 2n + 1`


This formula allows us to directly compute the number of colored cells for any `n` in constant time. 

---

## Step-by-Step Cell Coloring


| Step (n) | Total Cells | Pattern Description |
|----------|-------------|---------------------|
| 1        | 1           | Single center cell |
| 2        | 5           | Center + 4 adjacent cells |
| 3        | 13          | Previous cells + 8 new cells |
| 4        | 25          | Previous cells + 12 new cells |
| 5        | 41          | Previous cells + 16 new cells |

---

## Observable Pattern

Notice the sequence of total cells: 1, 5, 13, 25, 41...

Differences between consecutive totals:
- 1st to 2nd step: +4 cells
- 2nd to 3rd step: +8 cells
- 3rd to 4th step: +12 cells
- 4th to 5th step: +16 cells

The number of new cells follows: 4, 8, 12, 16...  
This is an arithmetic sequence where each step adds 4 more cells.

---

## 📊 Complexity Analysis
- **Time Complexity:**  
  Since we are using a direct mathematical formula, the computation is done in **O(1)** time. ⏱️

- **Space Complexity:**  
  No extra data structures are used, making the space complexity **O(1)**. 💾

---

## 💻 Code Implementation
```python
class Solution:
    def coloredCells(self, n: int) -> int:
        return 2 * n * n - 2 * n + 1
