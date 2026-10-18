import java.util.Arrays;

class Solution {
    public int solution(int[] array) {
        int answer = 0;
        int mid = 0;
        if(array.length % 2 == 0){
            mid = array.length / 2;
        }
        else{
            mid = array.length / 2 + 1;
        }
        
        Arrays.sort(array);
        
        answer = array[mid-1];
        return answer;
    }
}