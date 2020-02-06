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
def backtracking(self, arr: List[any]) -> List[Any]:
    res = []    # A list to save the results
    if not res: return res  # Corner case
    visited = [False for _ in range(len(arr))]    # A list to record the points have been visited
    self.helper(res, [], nums, visited) # Call the initial recursion

    return res

def helper(self, res: List[any], cur: List[any], arr: List[any], visited: List[bool]) -> None:
    if len(cur) == len(arr):
        res.append(cur[:]) # Note: use cur[:] to treat as different object.
    for i in range(len(arr)):
        if visited[i]:  # Skip visted point
            continue
        if i > 0 and nums[i] == nums[i-1] and not visited[i-1]: # Optional: skip duplicates
            continue
        if g(cur):  # Optional: backtrack on certain condition
            cur.append(arr[i]) # Choose
            visited[i] = True   # Choose, update visited
            helper(res, cur, arr, visited) # Explore
            cur.pop()   # Un-choose
            visited[i] = False

```

**Note:** There is a very useful article about copy object in `Python`. Please refer this [link](https://www.geeksforgeeks.org/python-cloning-copying-list/)

### Java

#### Combination

```java
public List<List<Integer>> subsetsWithDup(int[] nums) {
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
public List<List<Integer>> permute(int[] nums) {
    List<List<Integer>> res = new ArrayList<>();    // A ArrayList to save the results.
    if(nums.length == 0) return res;
    boolean[] visited = new boolean[nums.length];   // A boolean list to record the points have been. visited
    helper(res, new ArrayList<>(), nums, visited);  // Call the inital recursion.

    return res;
}

private void helper(List<List<Integer>> res, List<Integer> cur, int[] nums, boolean[] visited){
    if (cur.size() == nums.length) {
        res.add(new ArrayList(cur)); // Note: create a new ArrayList to treat as different object.
    }


    for (int i = 0; i < nums.length; i++) {
        if (visited[i]) // Skip visted point
            continue;
        if (i > 0 && nums[i] == nums[i-1] && !visited[i])   // Optional: skip duplicates
            continue;
        if (g(cur)) {       // Optional: backtrack on certain condition
            cur.add(nums[i]);   // Choose
            visited[i] = true;  // Choose, update visited
            helper(res, cur, nums, visited);    // Explore
            cur.remove(cur.size() - 1); // Un-choose
            visited[i] = false;
        }

    }
}
```

Time Complextiy: O(n \* 2^n)

Space Complexity: O(2^n)

## Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xt2fsyae)

| LC no. | Problem                                                              | Difficulty |                    Solution                     | Follow-up |  Freq.   |
| :----: | :------------------------------------------------------------------- | :--------: | :---------------------------------------------: | :-------- | :------: |
|   78   | [Subsets](https://leetcode.com/problems/subsets/)                    |  `Medium`  |      [Combination](./backtrack_subsets.py)      | 90,       | `Medium` |
|   90   | [Subsets II](https://leetcode.com/problems/subsets-ii/)              |  `Medium`  |     [Combination](./backtrack_subsetsII.py)     |           | `Medium` |
|   39   | [Combination Sum](https://leetcode.com/problems/combination-sum/)    |  `Medium`  |  [Combination](./backtrack_combination_sum.py)  | 40,       | `Medium` |
|   40   | [Combination Sum II](https://leetcode.com/problems/combination-sum/) |  `Medium`  | [Combination](./backtrack_combination_sumII.py) |           | `Medium` |
|   46   | [Permutations](https://leetcode.com/problems/permutations/)          |  `Medium`  |   [Permutation](./backtrack_permutations.py)    | 47, 60    |  `High`  |
|   47   | [Permutations II](https://leetcode.com/problems/permutations-ii/)    |  `Medium`  |  [Permutation](./backtrack_permutationsII.py)   | 31, 267   | `Medium` |

## Reference:

- [Backtracking Episode 1: leetcode 46. 47. Permutation and 78. 90. Subsets](https://www.youtube.com/watch?v=RkXl5iYoQn4)
- [花花酱 LeetCode 78. Subsets - 刷题找工作 EP236](https://www.youtube.com/watch?v=CUzm-buvH_8)
- [Leetcode Post](<https://leetcode.com/problems/subsets/discuss/27281/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)>)
- [Python | Cloning or Copying a list](https://www.geeksforgeeks.org/python-cloning-copying-list/)
