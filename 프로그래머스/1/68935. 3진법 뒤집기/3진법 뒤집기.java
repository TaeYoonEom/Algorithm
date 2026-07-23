class Solution {
    public int solution(int n) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        
        while(n > 0){
            sb.append(n % 3);
            n /= 3;
        }
        for(int i=0; i<sb.length(); i++){
            int num = sb.charAt(i) - '0';
            answer = answer * 3 + num;
        }
        return answer;
    }
}