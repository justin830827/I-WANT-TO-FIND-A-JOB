# Data Structues

In this folder, we will discuss some important DSs and the declaration on different programming lanuage. The outline inspired from the book [Cracking the Code Interview](http://www.crackingthecodinginterview.com).

## Array and List

An array is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together. When we declare an array in program, the memory assign a fixed size of space for the array. A list is an object which holds variables in a specific order.

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/x8iyupb5)

|  #   | Problem                                                                                           | Difficulty |                                     Solution                                     |         Type         | Follow-up         |  Freq.   |
| :--: | :------------------------------------------------------------------------------------------------ | :--------: | :------------------------------------------------------------------------------: | :------------------: | :---------------- | :------: |
| 896  | [Monotonic Array](https://leetcode.com/problems/monotonic-array/)                                 |   `Easy`   |    [Python](./python/monotonic_array.py), [Java](./java/MonotonicArray.java)     |       `Array`        |                   |  `Low`   |
| 766  | [Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)                                 |   `Easy`   |    [Python](./python/toeplitz_matrix.py), [Java](./java/ToeplitzMatrix.java)     |       `Array`        | 1329,             |  `Low`   |
| 1346 | [Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/) |   `Easy`   |       [Python](./python/check_double.py), [Java](./java/CheckDouble.java)        |       `Array`        |                   |  `Low`   |
| 238  | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)       |  `Medium`  | [Python](./python/prodcut_except_self.py), [Java](./java/ProductExceptSelf.java) |       `Array`        |                   |  `High`  |
|  1   | [Two Sum](https://leetcode.com/problems/two-sum/)                                                 |   `Easy`   |            [Python](./python/two_sum.py), [Java](./java/TwoSum.java)             |     `HashTable`      | 1099, 560         |  `High`  |
|  55  | [Jump Game](https://leetcode.com/problems/jump-game/)                                             |  `Medium`  |          [Python](./python/jump_game.py), [Java](./java/JumpGame.java)           |       `Greedy`       | 45, 1306          | `Medium` |
|  45  | [Jump Game II](https://leetcode.com/problems/jump-game-ii/)                                       |   `Hard`   |        [Python](./python/jump_game_ii.py), [Java](./java/JumpGameII.java)        |       `Greedy`       | 1306,             | `Medium` |
|  56  | [Merge Intervals](https://leetcode.com/problems/merge-intervals/)                                 |  `Medium`  |    [Python](./python/merge_intervals.py), [Java](./java/MergeIntervals.java)     |        `Sort`        | 57, 252, 759, 986 |  `High`  |
| 252  | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/)                                     |   `Easy`   |       [Python](./python/meeting_room.py), [Java](./java/MeetingRooms.java)       |        `Sort`        | 253,              | `Medium` |
| 253  | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms-ii/)                                  |   `Easy`   |    [Python](./python/meeting_room_ii.py), [Java](./java/MeetingRoomsII.java)     |        `Sort`        |                   |  `High`  |
| 152  | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)               |  `Medium`  |     [Python](./python/max_prod_subarr.py),[Java](./java/MaxProdSubArr.java)      |       `Array`        | 238, 713          | `Medium` |
|  54  | [Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)                                     |  `Medium`  |      [Python](./python/spiral_matrix.py), [Java](./java/SpiralMatrix.java)       |       `Array`        | 59                | `Medium` |
| 1366 | [Rank Teams by Votes](https://leetcode.com/problems/rank-teams-by-votes/)                         |  `Medium`  |         [Python](./python/rank_teams.py), [Java](./java/RankTeams.java)          | `Sort` + `HashTable` |                   |  `N/A`   |
|  15  | [3 Sum](https://leetcode.com/problems/3sum/)                                                      |  `Medium`  |          [Python](./python/three_sum.py), [Java](./java/ThreeSum.java)           |    `Two Pointer`     | 16, 18, 253       |  `High`  |
|  16  | [3Sum Closest](https://leetcode.com/problems/3sum-closest/)                                       |  `Medium`  |   [Python](./python/three_sum_closest.py), [Java](./java/ThreeSumClosest.java)   |    `Two Pointer`     | 15, 18, 253       | `Medium` |
| 560  | [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)                     |  `Medium`  |  [Python](./python/subarray_sum_equal.py), [Java](./java/SubarraySumEqual.java)  |     `HashTable`      | 713,              |  `High`  |
| 128  | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)       |   `Hard`   |                [Python](./python/lcs.py), [Java](./java/LCS.java)                |      `HashSet`       |                   |  `High`  |
| 1057 | [Campus Bikes](https://leetcode.com/problems/campus-bikes/)                                       |  `Medium`  |                        [Python](./python/campus_bikes.py)                        |        `Sort`        |                   | `Medium` |

## Characters and String

A string is a data type used in programming, it is comprised of a set of characters that can also contain spaces and numbers. String is immutable in most cases.

### String vs String Buffer vs String Builder

This is a popular interview question in Java.

|  Parameter  |               String               |                  String Buffer                   |            String Builder             |
| :---------: | :--------------------------------: | :----------------------------------------------: | :-----------------------------------: |
|   Storage   |            String Pool             |                       Heap                       |                 Heap                  |
| Mutability  |             Immutable              |                     Mutable                      |                Mutable                |
| Thread Safe | Not used in a threaded environment |       Used in a multi-threaded environment       | Used in a single-threaded environment |
| Performance |                Slow                | Slower than StringBuilder but faster than String |       Faster than StringBuffer        |

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xicddurd)

|  #  | Problem                                                             | Difficulty |                                  Solution                                   | Follow-up | Freq.  |
| :-: | :------------------------------------------------------------------ | :--------: | :-------------------------------------------------------------------------: | :-------- | :----: |
| 125 | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) |   `Easy`   | [Python](./python/valid_palindrome.py), [Java](./java/ValidPalindrome.java) | 680       | `High` |

## LinkedList

### Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xij041s6)

|  #   | Problem                                                                                                                                 | Difficulty |                                 Solution                                 | Follow-up |  Freq.   |
| :--: | :-------------------------------------------------------------------------------------------------------------------------------------- | :--------: | :----------------------------------------------------------------------: | :-------- | :------: |
|  19  | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)                                     |  `Medium`  | [Python](./python/remove_nth_node.py), [Java](./java/RemoveNthNode.java) |           | `Medium` |
| 1171 | [Remove Zero Sum Consecutive Nodes from Linked List](https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/) |  `Medium`  | [Python](./python/remove_zero_sum.py), [Java](./java/RemoveZeroSum.java) |           |  `Low`   |
| 206  | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)                                                               |   `Easy`   |                                                                          | 234       |  `High`  |
| 234  | [Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/)                                                         |   `Easy`   |                                                                          |           | `Meidum` |

## Stack and Queue

## Tree, Trie and Graph

## Reference

- [Cracking the Code Interview 6th edition](http://www.crackingthecodinginterview.com)
- [Leetcode](https://leetcode.com/)

## Style Guilde

- [Python Style Guide](http://google.github.io/styleguide/pyguide.html)

- [Java Style Guide](https://github.com/twitter-archive/commons/blob/master/src/java/com/twitter/common/styleguide.md#documentation)
