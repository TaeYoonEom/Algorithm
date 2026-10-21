class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = new int[num2-num1+1];
        
        for(int i=num1; i<num2+1; i++){// 1, 2, 3
            answer[i-num1] = numbers[i]; // 0, 1, 2
        }
        return answer;
    }
}