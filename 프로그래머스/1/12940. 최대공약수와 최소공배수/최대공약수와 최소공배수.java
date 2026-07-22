class Solution {
    public int[] solution(int n, int m) {
        int[] answer = new int[2];
        
        int a = n; // 2
        int b = m; // 5
        
        while(m!=0){
            int temp = m; // temp = 1
            m = n % m; // m = 0
            n = temp; // n = 1
        }
    
        answer[0] = n;
        answer[1] = (a * b) /n;
        
        return answer;
    }
    
}