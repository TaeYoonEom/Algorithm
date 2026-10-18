class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int[] answer = {};
        
        int numer = numer1 * denom2 + numer2 * denom1; //10
        int denom = denom1 * denom2; //8
        
        int a = numer;
        int b = denom;
        while(b!=0){
            int a1 = a % b;
            a = b;
            b = a1;
        }
        
        answer = new int[]{numer/a, denom/a};
        return answer;
    }
}