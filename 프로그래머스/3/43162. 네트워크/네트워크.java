import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        boolean[] visited = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();
        int answer = 0;
        
        for(int i=0; i<n; i++){
            if(!visited[i]){
                answer++;
                
                visited[i] = true;
                queue.offer(i);
                
                while(!queue.isEmpty()){
                    int current = queue.poll();
                    
                    for(int next=0; next<n; next++){
                        if(computers[current][next] == 1 
                           && !visited[next]){
                            visited[next] = true;
                            queue.offer(next);
                        }
                    }
                }
            }
        }
        
        return answer;
    }
}