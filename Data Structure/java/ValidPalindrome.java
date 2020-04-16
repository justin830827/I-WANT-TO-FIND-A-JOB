/**
 * Given a string, determine if it is a palindrome, considering only
 * alphanumeric characters and ignoring cases.
 * 
 * Note: For the purpose of this problem, we define empty string as valid
 * palindrome.
 * 
 * Idea of Solution:
 * 
 * 1. Compare reversed string: rebuild a string to filter the non-related
 * character and check if string is equal to its reversed.
 * 
 * 2. Two pointer
 */
public class ValidPalindrome {
    /**
     * @param s: a string contains alphannumeric characters
     * @return if string is a palindrome
     * 
     *         Time Complexity: O(n), Space Complexity: O(n)
     */
    public boolean isPalindromeCompare(String s) {
        StringBuilder cleanString = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                cleanString.append(Character.toLowerCase(c));
            }
        }
        String string = cleanString.toString();
        String reverse = cleanString.reverse().toString();
        return string.equals(reverse);
    }

    /**
     * @param s: a string contains alphannumeric characters
     * @return if string is a palindrome
     * 
     *         Time Complexity: O(n), Space Complexity: O(1)
     */
    public boolean isPalindromeTwoPointer(String s) {
        s = s.toLowerCase();
        int left = 0, right = s.length() - 1;
        while (left < right) {
            while (left < right && !Character.isLetterOrDigit(s.charAt(left))) {
                left++;
            }
            while (left < right && !Character.isLetterOrDigit(s.charAt(right))) {
                right--;
            }

            if (s.charAt(left) != s.charAt(right))
                return false;
            left++;
            right--;
        }
        return true;
    }
}