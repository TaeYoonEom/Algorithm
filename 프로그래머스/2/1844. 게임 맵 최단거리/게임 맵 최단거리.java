import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int rows = maps.length;
        int cols = maps[0].length;
        boolean [][] visited = new boolean[rows][cols];
        int[][] distance = new int[rows][cols];
        Queue<int[]> queue = new ArrayDeque<>();

        visited[0][0] = true;
        distance[0][0] = 1;
        queue.offer(new int[]{0, 0});
        
        int[] dr = {-1, 1, 0, 0}; // 위, 아래, 왼쪽, 오른쪽
        int[] dc = {0, 0, -1, 1};

        while(!queue.isEmpty()){
            int[] current = queue.poll();
            int row = current[0];
            int col = current[1];
            
            if(row == rows - 1 && col == cols - 1){
                return distance[row][col];
            }
            
            for(int i=0; i<4; i++){
                int nextRow = row + dr[i];
                int nextCol = col + dc[i];
                
                //1. 지도 밖이면 건너뛰기
                if (nextRow < 0 || nextRow >= rows 
                    || nextCol < 0 || nextCol >= cols){
                    continue;
                }
                
                // 2. 벽이면 건너뛰기
                if (maps[nextRow][nextCol] == 0){
                    continue;
                }
                
                //3. 이미 방문했다면 건너뛰기
                if (visited[nextRow][nextCol]){
                    continue;
                }
                
                visited[nextRow][nextCol] = true;
                distance[nextRow][nextCol] = distance[row][col] + 1;
                queue.offer(new int[]{nextRow, nextCol});
            }
        }
        
        return -1;
    }
}