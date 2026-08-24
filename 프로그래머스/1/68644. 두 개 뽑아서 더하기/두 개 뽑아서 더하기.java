import java.util.Arrays;
import java.util.TreeSet;

class Solution {
    public int[] solution(int[] numbers) {
        TreeSet<Integer> answer = new TreeSet<>();
        
        for(int i=0; i<numbers.length; i++){ // 1 1 2 3 4
            for(int j=i+1; j<numbers.length; j++)
            answer.add(numbers[i] + numbers[j]);
        }
        return answer.stream()
            .mapToInt(Integer::intValue)
            .toArray();
    }
}