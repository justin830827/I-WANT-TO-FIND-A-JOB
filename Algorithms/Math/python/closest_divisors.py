class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        """
        Args:
            nums: Given a non-empty integer array of size n.

        Returns:
            return the minimum number of moves required to make all array elements equal.

        Example:
            Input: date1 = "2019-06-29", date2 = "2019-06-30"
            Output: 1

            Input: date1 = "2020-01-15", date2 = "2019-12-31"
            Output: 15

        Idea of solution:
            Iterate a from sqrt(x+2) to 1, and check:
            1. if (x + 1) % a == 0, we directly return the pair [a, (x + 1) / a].
            2. if (x + 2) % a == 0, we directly return the pair [a, (x + 2) / a].
            The first valid pair we meet will have be the closet pair.
        
        Time complexity: O(sqrt(n))
        Space complexity: O(1)
        """
        for i in range(int( (num + 2) ** 0.5), 0, -1):
            if (num + 1) % i == 0:
                return [i, (num + 1) // i]
            if (num + 2) % i == 0:
                return [i, (num + 2) // i]