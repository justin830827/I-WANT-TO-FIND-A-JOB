# Backtracking

## Concepts

Backtracking is used when you need to find the correct series of choices that will solve a problem. For instances, Combination, Permutation, Subsets. There are three steps of Backtracking algorithm.

1. Choose: choose the start point.
2. Explore: find the solutions recusively with constraints.
3. Un-choose: undo the previous choice to explor next one.

We generally use Backtracking to find all the possible solutions or check whether there is a solution recursively.

## Template

### Python

#### Combination

```python
def backtracking(self, arr: List[any]) -> List[any]:
    res = []    # A list to save the results
    self.helper(res, [], arr, 0)   # call the initial recursion

    return res

def helper(self, res: List[any], cur: List[any], arr: List[any], start: int) -> None:
    if f(cur):  # Optional: add the coniditon to filter the solutions.
        res.append(cur[:])  # Note: use cur[:] to treat as different object.
    for i in range(start, len(arr)):
        if i > start and arr[i] == arr[i-1]:  # Optional: skip duplicates
            continue
        if g(cur):  # Optional: backtrack on certain condition
            cur.append(arr[i]) # Choose
            helper(res, cur, arr, i + 1)   # Explore the next element
            cur.pop()   # Un-choose
```

#### Permutation

```python
def backtracking(self, arr: List[any]) -> List[any]:
    res = []    # A list to save the results
    if not arr: return res  # Corner case
    seen = [False for _ in range(len(arr))]    # A list to record the points have been seen
    self.helper(res, [], nums, seen) # Call the initial recursion

    return res

def helper(self, res: List[any], cur: List[any], arr: List[any], seen: List[bool]) -> None:
    if len(cur) == len(arr):
        res.append(cur[:]) # Note: use cur[:] to treat as different object.
    for i in range(len(arr)):
        if seen[i]:  # Skip visted point
            continue
        if i > 0 and nums[i] == nums[i-1] and not seen[i-1]: # Optional: skip duplicates
            continue
        if g(cur):  # Optional: backtrack on certain condition
            cur.append(arr[i]) # Choose
            seen[i] = True   # Choose, update seen
            helper(res, cur, arr, seen) # Explore
            cur.pop()   # Un-choose
            seen[i] = False

```

**Note:** There is a very useful article about copy object in `Python`. Please refer this [link](https://www.geeksforgeeks.org/python-cloning-copying-list/)

### Java

#### Combination

```java
public List<List<Integer>> backtracking(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();    // A ArrayList to save the results.
    if (nums.length == 0) return res;
    Arrays.sort(nums);  // Optional: only need to sort in advance with input containing duplicates.
    helper(res, new ArrayList<>(), nums, 0);    // Call the inital recursion.

    return res;

}

private void helper(List<List<Integer>> res, List<Integer> cur, int[] nums, int start) {
    if (f(cur)) // Optional: add the coniditon to filter the solutions.
        res.add(new ArrayList(cur));    // Note: create a new ArrayList to treat as different object.

    for (int i = start; i < nums.length; i++) {
        if (i > start && nums[i-1] == nums[i])  // Optional: Skip duplicates.
            continue;
        if (g(cur)) {   // Optional: backtrack on certain condition.
            cur.add(nums[i]);   // Choose
            helper(res, cur, nums, i + 1);  // Explore
            cur.remove(cur.size() - 1); // Un-choose
        }
    }
}

```

#### Permutation

```java
public List<List<Integer>> backtracking(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();    // A ArrayList to save the results.
    if(nums.length == 0) return res;
    boolean[] seen = new boolean[nums.length];   // A boolean list to record the points have been. seen
    helper(res, new ArrayList<>(), nums, seen);  // Call the inital recursion.

    return res;
}

private void helper(List<List<Integer>> res, List<Integer> cur, int[] nums, boolean[] seen){
    if (cur.size() == nums.length) {
        res.add(new ArrayList(cur)); // Note: create a new ArrayList to treat as different object.
    }

    for (int i = 0; i < nums.length; i++) {
        if (seen[i]) // Skip seen point
            continue;
        if (i > 0 && nums[i] == nums[i-1] && !seen[i])   // Optional: skip duplicates
            continue;
        if (g(cur)) {       // Optional: backtrack on certain condition
            cur.add(nums[i]);   // Choose
            seen[i] = true;  // Choose, update seen
            helper(res, cur, nums, seen);    // Explore
            cur.remove(cur.size() - 1); // Un-choose
            seen[i] = false;
        }
    }
}
```

Time Complextiy: O(n \* 2^n)

Space Complexity: O(2^n)

## Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xt2fsyae)

|  #  | Problem                                                              | Difficulty |                                   Solution                                    | Follow-up | Comments    |
| :-: | :------------------------------------------------------------------- | :--------: | :---------------------------------------------------------------------------: | :-------- | :---------- |
| 78  | [Subsets](https://leetcode.com/problems/subsets/)                    |  `Medium`  |          [Python](./python/subsets.py), [Java](./java/Subsets.java)           | 90,       | Combination |
| 90  | [Subsets II](https://leetcode.com/problems/subsets-ii/)              |  `Medium`  |         [Python](./python/subsetsII.py), [Java](./java/SubsetsII.py)          |           | Combination |
| 39  | [Combination Sum](https://leetcode.com/problems/combination-sum/)    |  `Medium`  |   [Python](./python/combination_sum.py), [Java](./java/CombinationSum.java)   | 40, 77    | Combination |
| 40  | [Combination Sum II](https://leetcode.com/problems/combination-sum/) |  `Medium`  | [Python](./python/combination_sumII.py), [Java](./java/CombinationSumII.java) |           | Combination |
| 46  | [Permutations](https://leetcode.com/problems/permutations/)          |  `Medium`  |     [Python](./python/permutations.py), [Java](./java/Permutations.java)      | 47, 31    | Permutation |
| 47  | [Permutations II](https://leetcode.com/problems/permutations-ii/)    |  `Medium`  |   [Python](./python/permutationsII.py), [Java](./java/PermutationsII.java)    | 31, 267   | Permutation |
| 77  | [Combinations](https://leetcode.com/problems/combinations/)          |  `Medium`  |     [Python](./python/combinations.py), [Java](./java/Combinations.java)      | 40        | Combination |
| 31  | [Next Permutation](https://leetcode.com/problems/next-permutation/)  |  `Medium`  |  [Python](./python/next_permutaiton.py), [Java](./java/NextPermutation.java)  | 60        | Permutation |

## Reference:

- [Backtracking Episode 1: leetcode 46. 47. Permutation and 78. 90. Subsets](https://www.youtube.com/watch?v=RkXl5iYoQn4)
- [花花酱 LeetCode 78. Subsets - 刷题找工作 EP236](https://www.youtube.com/watch?v=CUzm-buvH_8)
- [Leetcode Post](<https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)>)
- [Python | Cloning or Copying a list](https://www.geeksforgeeks.org/python-cloning-copying-list/)
