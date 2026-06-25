import java.util.Arrays;

class Solution {
    public long solution(long n) {
        String str = String.valueOf(n);
        
        String [] arr = str.split("");
        Arrays.sort(arr);
        
        String sortedStr = "";
        for(int i= arr.length -1; i>=0; i--){
            sortedStr += arr[i];
        }
        
        return Long.parseLong(sortedStr);
    }
}