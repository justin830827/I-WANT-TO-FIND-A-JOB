from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """Dynamic Programming solution for Paint House problem.

        Args:
            costs: n x k cost matrix.
                e.q. costs[0][0] is the cost of painting house 0 with color 0;
                costs[1][2] is the cost of painting house 1 with color 2.

        Returns:
            Return the minimum cost to paint all houses

        Time Complexity: O(nk^2)
        Space Complexity: O(1) 

        """
        if not costs:
            return 0
        n, k = len(costs), len(costs[0])
        for i in range(1, n):
            for j in range(k):
                costs[i][j] = min(costs[i-1][l]+costs[i][j]
                                  for l in range(k) if l != j)
        return min(costs[n-1])
