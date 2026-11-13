import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> batches = new ArrayList<>();
        int releaseDay = 0;
        int count = 0;
        
        for(int i=0; i<progresses.length; i++){
            int remaining = 100 - progresses[i];
            int days = remaining / speeds[i];
            
            if(remaining % speeds[i] != 0){
                days++;
            }
            
            if(i == 0){
                releaseDay = days;
                count = 1;
            }else if(days <= releaseDay){
                count ++;
            }else{
                batches.add(count);
                releaseDay = days;
                count = 1;
            }
        }
        batches.add(count);
        
        int[] answer = new int[batches.size()];
        for(int i=0; i<batches.size(); i++){
            answer[i] = batches.get(i);
        }
        return answer;
    }

}