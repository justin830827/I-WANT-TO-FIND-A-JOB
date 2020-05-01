# Binary Search

## Concepts

Search a **sorted** array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

If you are Chinese speaker, please refer to this [link](https://www.youtube.com/watch?v=v57lNF2mb_s).

## Template

### Python

```python
def binary_search(left, right): # leftmost index and rightmost index
    while left < right:
        pivot = left + (right - left) // 2
        if f(pivot): return pivot   # optional
        if g(pivot):
            right = pivot   # search new range [left, pivot)
        else
            left = pivot + 1    # seach new range[pivot+1, right]
    return left     # return the cloest finding or not found i.e. -1
```

### Java

```java
public int binarySearch(int left, int right) {
    while (left < right) {
        int pivot = left + (right - left) / 2;
        if f(pivot) return pivot;   // optional

        if g(pivot) {
            right = pivot;  // search new range [left, pivot)
        } else {
            left = pivot + 1;   // seach new range[pivot+1, right]
        }
    }
    return left;    // return the cloest finding or not found i.e. -1
}

```

Time Complexity: O( log(left-right) \* ( f(pivot) + g(pivot) ) )

Space Complexity: O(1)

**Note**: there is two ways to calculate `pivot`

```
pivot = ( left + right ) / 2
pivot = left + (right - left) / 2
```

The second one is the correct way to aviod **overflow**, even though there won't occur in `python`.

## Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xicd2ynj)

|  #   | Problem                                                                                                                                           | Difficulty |                                   Solution                                   | Follow-up   |  Freq.   |
| :--: | :------------------------------------------------------------------------------------------------------------------------------------------------ | :--------: | :--------------------------------------------------------------------------: | :---------- | :------: |
| 278  | [First Bad Version](https://leetcode.com/problems/first-bad-version/)                                                                             |   `Easy`   | [Python](./python/first_bad_version.py), [Java](./java/FirstBadVersion.java) |             | `Medium` |
| 704  | [Binary Search](https://leetcode.com/problems/binary-search/)                                                                                     |   `Easy`   |                     [Python](./python/binary_search.py)                      | 702, 74, 33 |  `Low`   |
| 702  | [Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/)                               |  `Medium`  |                      [Python](./python/unknown_size.py)                      |             |  `Low`   |
|  74  | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)                                                                           |  `Medium`  |                    [Python](./python/search_2D_matrix.py)                    | 240,        | `Medium` |
| 240  | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)                                                                     |  `Medium`  |                  [Python](./python/search_2D_matrix_II.py)                   |             |  `High`  |
|  33  | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)                                                   |  `Medium`  |                  [Python](./python/search_rotated_array.py)                  | 81,153      |  `High`  |
|  81  | [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)                                             |  `Medium`  |                [Python](./python/search_rotated_array_II.py)                 | 153,        | `Medium` |
| 1351 | [Count Negative Numbers in a Sorted Matrix](https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/)                             |   `Easy`   |  [Python](./python/count_negatives.py), [Java](./java/CountNegatives.java)   |             |  `Low`   |
|  4   | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)                                                         |   `Hard`   |                                     link                                     |             |  `High`  |
|  34  | [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/) |  `Medium`  |                                     link                                     |             | `Medium` |
| 153  | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)                                       |  `Medium`  |                                     link                                     |             |  `High`  |
| 154  | [Find Minimum in Rotated Sorted Array II](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)                                 |   `Hard`   |                                     link                                     |             | `Medium` |
| 658  | [Find K Closest Elements](https://leetcode.com/problems/find-k-closest-elements/)                                                                 |  `Medium`  |                                     link                                     |             | `Medium` |
|  69  | [Sqrt(x)](https://leetcode.com/problems/sqrtx/)                                                                                                   |   `Easy`   |                                     link                                     |             |  `High`  |
| 875  | [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)                                                                         |  `Medium`  |                                     link                                     |             | `Medium` |

### Reference

- [花花酱 LeetCode Binary Search - 刷题找工作 SP5](https://zxi.mytechroad.com/blog/sp/sp5-binary-search/)
- [Binary Search on GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
- [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20题解%20-%20二分查找.md)
- [Leetcode.Wang](https://leetcode.wang)
