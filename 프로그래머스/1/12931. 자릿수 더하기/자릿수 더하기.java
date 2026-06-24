public class Solution {
    public int solution(int n) {
        int answer = 0;
        
        String[] rows = String.valueOf(n).split("");
        
        for(int i=0; i<rows.length; i++){
            answer += Integer.parseInt(rows[i]);
        }

        return answer;
    }
}