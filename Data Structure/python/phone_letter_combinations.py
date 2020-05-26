class Solution:
    """
    Given a string containing digits from 2-9 inclusive, return all
    possible letter combinations that the number could represent.

    Example:
        Input: "23"
        Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
    """

    def letterCombinations(self, digits: str) -> List[str]:
        """
        Args:
            digits: a string contains the numbers on the phone.

        Return:
            an array contain all the possible combinations.
            if the input contains "0" or "1", return empty
            array.

        Time Complexity: O(3^N * 4^M) where N is the number of digits in
        the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is
        the number of digits in the input that maps to 4 letters (e.g. 7, 9),
        and N+M is the total number digits in the input.

        Space Complexity: O(3^N * 4^M), the maximum space where we save in 'cur'
        """
        if not digits:
            return
        # Letters mapping on the phone
        letters = {'2': "abc",
                   '3': "def",
                   '4': "ghi",
                   '5': "jkl",
                   '6': "mno",
                   '7': "pqrs",
                   '8': "tuv",
                   '9': "wxyz",
                   '1': "",
                   '0': "",
                   }

        combinations = ['']
        for digit in digits:
            cur = []
            for letter in letters[digit]:
                for combination in combinations:
                    cur.append(combination + letter)
            combinations = cur
        return combinations
