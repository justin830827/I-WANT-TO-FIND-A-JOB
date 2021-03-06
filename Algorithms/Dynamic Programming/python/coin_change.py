from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Dynamic Programming solution for Coin Change problem.

        Args:
            coins: Given coins of different denominations.
            amount: A total amount of money.

        Returns:
             The fewest number of coins that you need to make up that amount.
             If that amount of money cannot be made up by any combination of
             the coins, return -1

        Time Complexity: O(nc), where c is the length of coins, n is the amount
        Space Complexity: O(n) 

        """
        memo = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            memo[i] = min(memo[i-c] + 1 if i - c >= 0 else float('inf')
                          for c in coins)
        return -1 if memo[amount] == float('inf') else memo[amount]
