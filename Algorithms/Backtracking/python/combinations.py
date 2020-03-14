class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(res, [], n, k, 1)
        return res

    def helper(self, res, cur, n, k, start):
        if len(cur) == k:
            res.append(cur[:])
            return

        for i in range(start, n + 1):
            cur.append(i)
            self.helper(res, cur, n, k, i + 1)
            cur.pop()

    def helper_optimized(self, res, cur, n, k, start):
        if k == 0:
            res.append(cur[:])
            return

        for i in range(start, n - k + 2):
            cur.append(i)
            self.helper(res, cur, n, k - 1, i + 1)
            cur.pop()
