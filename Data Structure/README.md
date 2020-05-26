# Data Structues

In this folder, we will discuss some important DSs and the implementation on different programming lanuage. The outline inspired from the book [Cracking the Code Interview](http://www.crackingthecodinginterview.com) and [qiyuangong's leetcode](https://github.com/qiyuangong/leetcode).

## Array and List

An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. When we declare an array in program, the memory assign a fixed size of space for the array. A list is an object which holds variables in a specific order.

**Java**

```Java
// Declare array on different data types
int[] intArray = new int[10];
char[] charArray = new char[26];

// Declare array with defaulted value
int[] intArray = {1, 2, 3, 4, 5};

// Declare list
List<Integer> intList = new ArrayList<>();
List<Character> charList = new ArrayList<>();
```

**Python**

Python does not have array data structure and data type in list declaration

```python
# Declare a list
python_list = []

# Declare a list with defaulted values
python_list = [1, 2, 3, 4, 5]
```

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/x8iyupb5)

|  #   | Title                                                                                             | Difficulty |                                     Solution                                     | Comment                                                                               |
| :--: | :------------------------------------------------------------------------------------------------ | :--------: | :------------------------------------------------------------------------------: | :------------------------------------------------------------------------------------ |
|  1   | [Two Sum](https://leetcode.com/problems/two-sum/)                                                 |   `Easy`   |            [Python](./python/two_sum.py), [Java](./java/TwoSum.java)             | 1. Brute Force: O(N^2) </br> 2. HashTable: O(N) </br> 3. Sort + Two Pointer: O(NlogN) |
|  15  | [3Sum](https://leetcode.com/problems/3sum/)                                                       |  `Medium`  |          [Python](./python/three_sum.py), [Java](./java/ThreeSum.java)           | Sort + Two Pointer/HashSet: O(N^2)                                                    |
|  16  | [3Sum Closest](https://leetcode.com/problems/3sum-closest/)                                       |  `Medium`  |   [Python](./python/three_sum_closest.py), [Java](./java/ThreeSumClosest.java)   | Sort + Two Pointer/HashSet: O(N^2)                                                    |
|  18  | [4Sum](https://leetcode.com/problems/4sum/)                                                       |  `Medium`  |           [Python](./python/four_sum.py), [Java](./java/FourSum.java)            | Sort + Two Pointer/HashSet: O(N^3)                                                    |
|  45  | [Jump Game II](https://leetcode.com/problems/jump-game-ii/)                                       |   `Hard`   |        [Python](./python/jump_game_ii.py), [Java](./java/JumpGameII.java)        | Greedy                                                                                |
|  54  | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)                                     |  `Medium`  |      [Python](./python/spiral_matrix.py), [Java](./java/SpiralMatrix.java)       |                                                                                       |
|  55  | [Jump Game](https://leetcode.com/problems/jump-game/)                                             |  `Medium`  |          [Python](./python/jump_game.py), [Java](./java/JumpGame.java)           | Greedy                                                                                |
|  56  | [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                                 |  `Medium`  |    [Python](./python/merge_intervals.py), [Java](./java/MergeIntervals.java)     |                                                                                       |
| 128  | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)       |   `Hard`   |                [Python](./python/lcs.py), [Java](./java/LCS.java)                |                                                                                       |
| 152  | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)               |  `Medium`  |     [Python](./python/max_prod_subarr.py),[Java](./java/MaxProdSubArr.java)      |                                                                                       |
| 238  | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)       |  `Medium`  | [Python](./python/prodcut_except_self.py), [Java](./java/ProductExceptSelf.java) |                                                                                       |
| 252  | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)                                     |   `Easy`   |       [Python](./python/meeting_room.py), [Java](./java/MeetingRooms.java)       |                                                                                       |
| 253  | [Meeting Rooms II](https://leetcode.com/problems/meeting-rooms-ii/)                               |   `Easy`   |    [Python](./python/meeting_room_ii.py), [Java](./java/MeetingRoomsII.java)     |                                                                                       |
| 259  | [3Sum Smaller](https://leetcode.com/problems/3sum-smaller/)                                       |  `Medium`  |   [Python](./python/three_sum_smaller.py), [Java](./java/ThreeSumSmaller.java)   | Sort + Two Pointer/HashSet: O(N^2)                                                    |  |
| 347  | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)                 |  `Medium`  | [Python](./python/top_k_freq_elements.py), [Java](./java/TopKFreqElements.java)  | 1. HashTable + Heap/Sort: O(NlogK) ~ O(NlogN) </br> 2. Bucket Sort: O(N)              |
| 560  | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)                     |  `Medium`  |  [Python](./python/subarray_sum_equal.py), [Java](./java/SubarraySumEqual.java)  |                                                                                       |
| 692  | [Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words.py)                     |  `Medium`  |    [Python](./python/top_k_freq_words.py), [Java](./java/TopKFreqWords.java)     | HashTable + Heap: O(NlogK)                                                            |
| 766  | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)                                 |   `Easy`   |    [Python](./python/toeplitz_matrix.py), [Java](./java/ToeplitzMatrix.java)     |                                                                                       |
| 896  | [Monotonic Array](https://leetcode.com/problems/monotonic-array/)                                 |   `Easy`   |    [Python](./python/monotonic_array.py), [Java](./java/MonotonicArray.java)     |                                                                                       |
| 1057 | [Campus Bikes](https://leetcode.com/problems/campus-bikes/)                                       |  `Medium`  |                        [Python](./python/campus_bikes.py)                        |                                                                                       |
| 1346 | [Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) |   `Easy`   |       [Python](./python/check_double.py), [Java](./java/CheckDouble.java)        |                                                                                       |
| 1366 | [Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)                         |  `Medium`  |         [Python](./python/rank_teams.py), [Java](./java/RankTeams.java)          |                                                                                       |

## Characters and String

A string is a data type used in programming, it is comprised of a set of characters that can also contain spaces and numbers. String is immutable in most cases.

### String vs String Buffer vs String Builder

This is a popular interview question in **Java**.

|  Parameter  |               String               |                  String Buffer                   |            String Builder             |
| :---------: | :--------------------------------: | :----------------------------------------------: | :-----------------------------------: |
|   Storage   |            String Pool             |                       Heap                       |                 Heap                  |
| Mutability  |             Immutable              |                     Mutable                      |                Mutable                |
| Thread Safe | Not used in a threaded environment |       Used in a multi-threaded environment       | Used in a single-threaded environment |
| Performance |                Slow                | Slower than StringBuilder but faster than String |       Faster than StringBuffer        |

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xicddurd)

|  #  | Problem                                                                                                       | Difficulty |                                          Solution                                           | Comment                                                                  |
| :-: | :------------------------------------------------------------------------------------------------------------ | :--------: | :-----------------------------------------------------------------------------------------: | :----------------------------------------------------------------------- |
| 17  | [Letter Combinations of a Phone Number](https://leetcode.com/problems/letter-combinations-of-a-phone-number/) |  `Medium`  | [Python](./python/phone_letter_combinations.py), [Java](./java/PhoneLetterCombination.java) | Combination: O(3^N \* 4^M)                                               |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)                                           |   `Easy`   |         [Python](./python/valid_palindrome.py), [Java](./java/ValidPalindrome.java)         |                                                                          |
| 387 | [First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)       |   `Easy`   |        [Python](./python/first_unique_char.py), [Java](./java/FirstUniqueChar.java)         | HashTable: O(N)                                                          |
| 451 | [Sort Characters By Frequency](https://leetcode.com/problems/sort-characters-by-frequency/)                   |  `Medium`  |         [Python](./python/sort_char_by_freq.py), [Java](./java/SortCharByFreq.java)         | 1. HashTable + Heap/Sort: O(NlogK) ~ O(NlogN) </br> 2. Bucket Sort: O(N) |

## LinkedList

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xij041s6)

|  #   | Title                                                                                                                                   | Difficulty |                                   Solution                                    | Comment    |
| :--: | :-------------------------------------------------------------------------------------------------------------------------------------- | :--------: | :---------------------------------------------------------------------------: | :--------- |
|  19  | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)                                     |  `Medium`  |   [Python](./python/remove_nth_node.py), [Java](./java/RemoveNthNode.java)    |            |
|  82  | [Remove Duplicates from Sorted List II](https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)                           |  `Medium`  |  [Python](./python/remove_duplicates_II.py), [Java](RemoveDuplicatesII.java)  | Dummy node |
|  83  | [Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)                                 |   `Easy`   | [Python](./python/remove_duplicates.py), [Java](./java/RemoveDuplicates.java) |            |
| 206  | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)                                                               |   `Easy`   |                                                                               |            |
| 234  | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                                                         |   `Easy`   |                                                                               |            |
| 1171 | [Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) |  `Medium`  |   [Python](./python/remove_zero_sum.py), [Java](./java/RemoveZeroSum.java)    |            |

## Stack and Queue

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xicdw3ps)

|  #  | Title | Difficulty | Solution | Comment |
| :-: | :---- | :--------: | :------: | :------ |
|     |       |            |          |         |

## Tree, Trie and Graph

### Tree Traverse

![alt text](../images/tree-traverse.png)

### Algorithms

The followings are some certain algorithm can be used on Tree, Trie, Graph structure.

#### Morris Traversal

Using Morris Traversal on tree structure, we can traverse the tree without using stack and recursion. i.e. The space complexity is O(1).

**Preorder**

```
Step 1: Initialize current as root

Step 2: While current is not NULL,

    If current node have left child
        a. Add the current node and its right subtree (cur and cur.right) to the rightmost node of current left subtree (the rightmost node in cur.left)

        b. Go to this left child, i.e., current = current.left

    Else
        a. Add current’s value

        b. Go to the right, i.e., current = current.right
```

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xicd7w93)

|  #  | Title                                                                                         | Difficulty |                                     Solution                                     | Comment |
| :-: | :-------------------------------------------------------------------------------------------- | :--------: | :------------------------------------------------------------------------------: | :------ |
| 94  | [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/) |  `Medium`  | [Python](./python/binary_tree_inorder.py), [Java](./java/BinaryTreeInorder.java) |         |

## Reference

- [Cracking the Code Interview 6th edition](http://www.crackingthecodinginterview.com)
- [Leetcode](https://leetcode.com/)
- [qiyuangong's leetcode](https://github.com/qiyuangong/leetcode)

## Style Guilde

- [Python Style Guide](http://google.github.io/styleguide/pyguide.html)

- [Java Style Guide](https://github.com/twitter-archive/commons/blob/master/src/java/com/twitter/common/styleguide.md#documentation)
