class Solution {
    public int solution(String t, String p) {
        int answer = 0;
        int n = p.length();
        
        for(int i=0; i<= t.length()-n; i++){
            if(Long.parseLong(t.substring(i, i+n)) <= Long.parseLong(p)){
                answer += 1;
            }
        }
        return answer;
    }
}