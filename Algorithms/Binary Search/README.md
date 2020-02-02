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

| LC no. | Problem                                                                                                             | Difficulty |                                                             Solution                                                             | Follow-up   |  Freq.   |
| :----: | :------------------------------------------------------------------------------------------------------------------ | :--------: | :------------------------------------------------------------------------------------------------------------------------------: | :---------- | :------: |
|  278   | [First Bad Version](https://leetcode.com/problems/first-bad-version/)                                               |   `Easy`   |                                              [link](../binarySearch_1stBadVersion)                                               |             | `Medium` |
|  704   | [Binary Search](https://leetcode.com/problems/binary-search/)                                                       |   `Easy`   |       [link](https://github.com/justin830827/I-WANT-TO-FIND-A-JOB/blob/master/Algorithms/Binary%20Search/binarySearch.py)        | 702, 74, 33 |  `Low`   |
|  702   | [Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) |  `Medium`  | [link](https://github.com/justin830827/I-WANT-TO-FIND-A-JOB/blob/master/Algorithms/Binary%20Search/binarySearch_unknown_size.py) |             |  `Low`   |
|   74   | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)                                             |  `Medium`  |    [link](https://github.com/justin830827/I-WANT-TO-FIND-A-JOB/blob/master/Algorithms/Binary%20Search/binarySearch_matrix.py)    | 240,        | `Medium` |
|  240   | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)                                       |  `Medium`  |   [link](https://github.com/justin830827/I-WANT-TO-FIND-A-JOB/blob/master/Algorithms/Binary%20Search/binarySearch_matrixII.py)   |             |  `High`  |
|   33   | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)                     |  `Medium`  |                                                               link                                                               | 81          |  `High`  |
|   81   | [Search in Rotated Sorted Array II](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/)               |  `Medium`  |                                                               link                                                               |             | `Medium` |

### Reference

- [花花酱 LeetCode Binary Search - 刷题找工作 SP5](https://zxi.mytechroad.com/blog/sp/sp5-binary-search/)
- [Binary Search on GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
- [CyC2018/CS-Notes](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20题解%20-%20二分查找.md)
