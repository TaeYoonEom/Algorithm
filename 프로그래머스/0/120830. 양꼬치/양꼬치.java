class Solution {
    public int solution(int n, int k) {
        int total = 0;
        int kochhi = 0;
        int service = 0;
        
        total = n*12000 + k*2000;
        kochhi = n/10;
        service = kochhi * 2000;
        
        total = total - service;
        return total;
    }
}