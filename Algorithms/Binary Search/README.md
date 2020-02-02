# Binary Search

## Concepts

If you are Chinese speaker, please refer to this [link](https://www.youtube.com/watch?v=v57lNF2mb_s).

Typically, binary search can be used on a sorted `Input`.

### Reference

- [花花酱 LeetCode Binary Search - 刷题找工作 SP5](https://www.youtube.com/watch?v=v57lNF2mb_s)

## Template

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

Time Complexity: O( log(left-right) \* ( f(pivot) + g(pivot) ) )

Space Complexity: O(1)

## Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xicd2ynj)

| LC no. | Problem                                                                                                             | Difficulty | Solution | Follow-up |
| :----: | :------------------------------------------------------------------------------------------------------------------ | :--------: | :------: | :-------- |
|  704   | [Binary Search](https://leetcode.com/problems/binary-search/)                                                       |   `Easy`   |   link   | 702, 74   |
|  702   | [Search in a Sorted Array of Unknown Size](https://leetcode.com/problems/search-in-a-sorted-array-of-unknown-size/) |  `Medium`  |   link   |           |
|   74   | [Search a 2D Matrix](https://leetcode.com/problems/search-a-2d-matrix/)                                             |  `Medium`  |   link   | 240,      |
|  240   | [Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)                                       |  `Medium`  |   link   |           |
|   33   | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)                     |  `Medium`  |   link   |           |
