from typing import List


class Solution:
    """Check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).

    Args:
        arr: Given an array of integers

    Returns:
        return true if there exists two indices i and j such that :
        1. i != j
        2. 0 <= i, j < arr.length
        3. arr[i] == 2 * arr[j]

    Example:
        Input: [10,2,5,3]
        Output: true

        Input: [7,1,14,11]
        Output: true

        Input:[3,1,7,11]
        Output: false

    Idea of solution:
        The tricky part of this problem is to also check both 2 * arr[i] and arr[i] / 2 if in the array.
        To make the search efficiently, we can use Hash Set to save the previous value,
        and check if the incoming element meet the requirements.

    Time Complexity: O(n)
    Space Complexity: O(n) 
    """

    def checkIfExist(self, arr: List[int]) -> bool:
        table = set()
        for i in range(len(arr)):
            if 2 * arr[i] in table or arr[i] % 2 == 0 and arr[i] // 2 in table:
                return True
            table.add(arr[i])
        return False
