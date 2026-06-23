class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        int lens = numbers.length;
        
        for(int i=0; i<lens; i++){
            answer += numbers[i];
        }
        answer = answer / lens;
        return answer;
    }
}