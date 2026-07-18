import java.util.Arrays;

class Solution {
    public String solution(String s) {
        char[] charArray = s.toCharArray();
        
        Arrays.sort(charArray);
        
        String ascending = new String(charArray);
        return new StringBuilder(ascending).reverse().toString();
    }
}