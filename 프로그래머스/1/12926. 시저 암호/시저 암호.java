class Solution {
    public String solution(String s, int n) {
        String answer = "";
       for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
           
           if(c == ' '){
               answer += c;
           }
           else if(c >= 'A' && c <= 'Z'){
               c = (char) (c+n);
               
               if(c > 'Z'){
                   c = (char) (c-26);
               }
               answer += c;
           }
           else if(c >= 'a' && c <= 'z'){
               c = (char) (c + n);
               
               if(c > 'z'){
                   c = (char) (c-26);
               }
               
               answer += c;
           }
        }
        
        return answer;
    }
}