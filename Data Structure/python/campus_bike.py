from typing import List


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        pairs = []
        res = []
        for i, worker in enumerate(workers):
            for j, bike in enumerate(bikes):
                dist = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                pairs.append((dist, i, j))
        pairs.sort()
        res = [-1] * len(workers)
        used = set()
        for pair in pairs:
            w, b = pair[1], pair[2]
            if res[w] == -1:
                if b not in used:
                    res[w] = b
                    used.add(b)
        return res
