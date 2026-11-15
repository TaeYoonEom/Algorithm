import java.util.Queue;
import java.util.ArrayDeque;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<int[]> queue = new ArrayDeque<>();
        int count = 0;
        
        for(int i=0; i<priorities.length; i++){
            queue.offer(new int[]{i, priorities[i]});
        }
        
        while(!queue.isEmpty()){
            boolean hasHigherPriority = false;
            int[] first = queue.poll(); //A(2)
            
            for(int[] waiting : queue){
                if(first[1] < waiting[1]){
                    hasHigherPriority = true;
                    break;
                }
            }
            if(hasHigherPriority){ // 가장 큰 수는 실행x 
                queue.offer(first);
                continue;
            }
            count++;
            if(first[0] == location){
                return count;
            }
        }
        return -1;
    }
}