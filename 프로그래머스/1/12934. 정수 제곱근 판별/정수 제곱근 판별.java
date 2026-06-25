class Solution {
    public long solution(long n) {
        long i = 1;
        
        while(i*i <= n){
            if(n == i*i){
                return (i+1) * (i+1);
            }
            i++;
        }
        return -1;
    }
}