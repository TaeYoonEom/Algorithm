class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int max1 = 0;
        int max2 = 0;
        
        for(int i=0; i<sizes.length; i++){
            if(sizes[i][0] < sizes[i][1]){
                int m = sizes[i][1];
                sizes[i][1] = sizes[i][0];
                sizes[i][0] = m;
            }
            max1 = Math.max(sizes[i][0], max1);
            max2 = Math.max(sizes[i][1], max2);
            }
        answer = max1 * max2;
        return answer;
        }     
}