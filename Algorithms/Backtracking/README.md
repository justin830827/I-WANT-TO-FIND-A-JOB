# Backtracking

## Concepts

Backtracking is used when you need to find the correct series of choices that will solve a problem. For instances, Combination, Permutation, Subsets. There are three steps of Backtracking algorithm.

1. Choose: choose the start point.
2. Explore: find the solutions recusively with constraints.
3. Un-choose: undo the previous choice to explor next one.

We generally use Backtracking to find all the possible solutions or check whether there is a solution recursively.

## Template

### Python

```python
def backtracking(self, arr: List[Any]) -> List[Any]:
    res = [] # A list to save the results
    self.helper(res, [], nums, 0) # call the initial recursion

    return res

def helper(res: List[Any], cur: List[Any], nums: List[Any], start: int) -> None:
    res.append(cur[:]) # Note: use cur[:] to treat as different object.
    for i in range(start, len(nums)):
        cur.append(nums[i]) # Choose
        helper(res, cur, nums, i + 1) # Explore
        cur.pop()   # Un-choose
```

Time Complextiy: O(n \* 2^n)
Space Complexity: O(2^n)

## Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xt2fsyae)

| LC no. | Problem                                                 | Difficulty |            Solution            | Follow-up |  Freq.   |
| :----: | :------------------------------------------------------ | :--------: | :----------------------------: | :-------- | :------: |
|   78   | [Subsets](https://leetcode.com/problems/subsets/)       |  `Medium`  | [link](./backtrack_subsets.py) | 90,       | `Medium` |
|   90   | [Subsets II](https://leetcode.com/problems/subsets-ii/) |  `Medium`  |              link              |           | `Medium` |

## Reference:

- [Backtracking Episode 1: leetcode 46. 47. Permutation and 78. 90. Subsets](https://www.youtube.com/watch?v=RkXl5iYoQn4)
- [花花酱 LeetCode 78. Subsets - 刷题找工作 EP236](https://www.youtube.com/watch?v=CUzm-buvH_8)
- [Leetcode Post](<https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)>)
