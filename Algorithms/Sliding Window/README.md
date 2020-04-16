# Sliding Window

## Concepts

## Template

### Python

### Java

```java
public class Solution {
    public List<Integer> slidingWindow(String s, String t) {
        //init a collection or int value to save the result according the question.
        List<Integer> result = new LinkedList<>();
        if(t.length()> s.length()) return result;

        //create a hashmap to save the Characters of the target substring.
        //(K, V) = (Character, Frequence of the Characters)
        Map<Character, Integer> map = new HashMap<>();
        for(char c : t.toCharArray()){
            map.put(c, map.getOrDefault(c, 0) + 1);
        }
        //maintain a counter to check whether match the target string.
        int counter = map.size();//must be the map size, NOT the string size because the char may be duplicate.

        //Two Pointers: begin - left pointer of the window; end - right pointer of the window
        int left = 0, right = 0;

        //the length of the substring which match the target string.
        int res = Integer.MAX_VALUE;

        //loop at the begining of the source string
        while(right < s.length()){

            char c = s.charAt(right);//get a character

            if( map.containsKey(c) ){
                map.put(c, map.get(c)-1);// plus or minus one
                if(map.get(c) == 0) counter--;//modify the counter according the requirement(different condition).
            }
            right++;

            //increase begin pointer to make it invalid/valid again
            while(counter == 0){

                char tempc = s.charAt(begin);//***be careful here: choose the char at begin pointer, NOT the end pointer
                if(map.containsKey(tempc)){
                    map.put(tempc, map.get(tempc) + 1);//plus or minus one
                    if(map.get(tempc) > 0) counter++;//modify the counter according the requirement(different condition).
                }

                /* save / update(min/max) the result if find a target*/
                // result collections or result int value

                begin++;
            }
        }
        return result;
    }
}

```

## Leetcode Problems

Clone the problem list [here](https://leetcode.com/list/xicd07oh)

|  #  | Problem                                                                                                                         | Difficulty | Solution | Follow-up | Freq.  |
| :-: | :------------------------------------------------------------------------------------------------------------------------------ | :--------: | :------: | :-------- | :----: |
|  3  | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) |  `Medium`  |          |           | `High` |
