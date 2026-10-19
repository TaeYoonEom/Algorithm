class Solution {
    public int solution(int n) {
        int answer = 0;
        int pizza = 0;
        if(n > 7){
            if(n % 7 != 0){
                pizza = n / 7 + 1;
            }else{
                pizza = n / 7;    
            }
            
        }else if(n <= 7){
            return 1;
        }
        answer = pizza;
        return answer;
    }
}