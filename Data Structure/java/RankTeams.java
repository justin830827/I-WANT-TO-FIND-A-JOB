import java.util.*;

/**
 * In a special ranking system, each voter gives a rank from highest to lowest
 * to all teams participated in the competition.
 * 
 * The ordering of teams is decided by who received the most position-one votes.
 * If two or more teams tie in the first position, we consider the second
 * position to resolve the conflict, if they tie again, we continue this process
 * until the ties are resolved. If two or more teams are still tied after
 * considering all positions, we rank them alphabetically based on their team
 * letter.
 * 
 * Given an array of strings votes which is the votes of all voters in the
 * ranking systems. Sort all teams according to the ranking system described
 * above.
 * 
 * Return a string of all teams sorted by the ranking system.
 * 
 * Time Complextiy: O(nmlogm), Space Complexity: O(m^2), where n = votes.length
 * and m = votes[0].length <= 26
 */

class RankTeams {
    /**
     * @param votes: a string list with fixed size strings and the string only
     *               contain unique upper case letter.
     * @return string of all teams sorted by the ranking system.
     */
    public String rankTeams(String[] votes) {
        int n = votes[0].length();
        HashMap<Character, int[]> map = new HashMap<Character, int[]>();
        for (char c : votes[0].toCharArray()) {
            map.put(c, new int[n]);
        }
        for (String vote : votes) {
            for (int i = 0; i < vote.length(); i++) {
                char c = vote.charAt(i);
                map.get(c)[i]--;
            }
        }
        List<Character> chars = new ArrayList<>(map.keySet());
        Collections.sort(chars, (a, b) -> {
            for (int i = 0; i < n; i++) {
                if (map.get(a)[i] != map.get(b)[i]) {
                    return map.get(a)[i] - map.get(b)[i];
                }
            }
            return a - b;
        });
        StringBuilder sb = new StringBuilder();
        for (char c : chars) {
            sb.append(c);
        }

        return sb.toString();
    }
}