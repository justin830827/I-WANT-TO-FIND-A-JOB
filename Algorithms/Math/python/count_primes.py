class Solution:
    def countPrimes(self, n: int) -> int:
        """
        Args:
            n: a non-negative number.

        Returns:
            the number of prime less than n.

        Example:
            Input: 10
            Output: 4

        Idea of solution:
            Use Sieve of Eratosthenes algorithm.
        
        Time complexity: O(n)
        Space complexity: O(n)
        """
        if n < 2: return 0
        is_prime = [False if i < 2 else True for i in range(n)]
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        return is_prime.count(True)