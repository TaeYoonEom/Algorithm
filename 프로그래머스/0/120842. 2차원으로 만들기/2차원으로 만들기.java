class Solution {
    public int[][] solution(int[] num_list, int n) {
        int[][] answer = new int[num_list.length / n][n];
        int number = 0;
        for(int i=0; i<num_list.length; i+=n){// 0 2 4 6
            for(int j=i; j<n+i; j++){
                answer[number][j-i] = num_list[j];
            }
            number++;
        }
        
        
        return answer;
    }
}