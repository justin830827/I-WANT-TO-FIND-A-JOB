from typing import List


class Solution:
    """
    Args:
        votes: a string list with fixed size strings and the string only
             contain unique upper case letter.

    Returns:
        return string of all teams sorted by the ranking system.

    Idea of Solution:
        Count the rank of vote for each candidate. Sort all teams according to the ranking system.

    Time Complextiy: O(nmlogm)
    Space Complexity: O(m^2), where n = votes.length and m = votes[0].length <= 26
    """
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        rank = { t: [0] * n for t in votes[0] }
        for vote in votes:
            for i, t in enumerate(vote):
                rank[t][i] -= 1
        return ''.join(sorted(votes[0], key= lambda x: rank[x] + [x]))