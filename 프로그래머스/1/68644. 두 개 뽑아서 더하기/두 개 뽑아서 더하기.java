import java.util.*;
class Solution {
    public int[] solution(int[] numbers) {
        Set<Integer> arrays = new HashSet<>();
        
        for(int i=0; i<numbers.length - 1; i++){
            for(int j=i+1; j<numbers.length; j++){
                arrays.add(numbers[i] + numbers[j]);
            }
        }
        int[] answer = new int[arrays.size()];
        int index = 0;
        
        for(int sum : arrays){
            answer[index] = sum;
            index++;
        }
        
        Arrays.sort(answer);
        
        return answer;
    }
}