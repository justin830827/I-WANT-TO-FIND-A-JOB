import java.util.*;

/**
 * Given a string containing digits from 2-9 inclusive, return all possible
 * letter combinations that the number could represent.
 * 
 * Example:
 * 
 * Input: "23"
 * 
 * Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 */
public class PhoneLetterCombination {
    /**
     * 
     * @param digits: a string contains the numbers on the phone.
     * @return an array contain all the possible combinations. if the input contains
     *         "0" or "1", return empty array.
     * 
     *         Time Complexity: O(3^N * 4^M) where N is the number of digits in the
     *         input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the
     *         number of digits in the input that maps to 4 letters (e.g. 7, 9), and
     *         N+M is the total number digits in the input.
     * 
     *         Space Complexity: O(3^N * 4^M), the maximum space where we save in
     *         'cur'
     */
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0)
            return new ArrayList<String>();
        HashMap<Character, String> letters = new HashMap<>();
        letters.put('2', "abc");
        letters.put('3', "def");
        letters.put('4', "ghi");
        letters.put('5', "jkl");
        letters.put('6', "mno");
        letters.put('7', "pqrs");
        letters.put('8', "tuv");
        letters.put('9', "wxyz");
        letters.put('1', "");
        letters.put('0', "");

        List<String> combinations = new ArrayList<>(Arrays.asList(""));
        for (char digit : digits.toCharArray()) {
            List<String> cur = new ArrayList<>();
            for (char letter : letters.get(digit).toCharArray()) {
                for (String combination : combinations) {
                    StringBuilder sb = new StringBuilder(combination);
                    sb.append(letter);
                    cur.add(sb.toString());
                }
            }
            combinations = cur;
        }
        return combinations;
    }
}