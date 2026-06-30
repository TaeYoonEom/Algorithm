class Solution {
    public String solution(String s) {
        String [] arr = s.split("");
        
        int mid = s.length() / 2;
        if(arr.length % 2 == 0){
            return arr[mid-1] + arr[mid];
        }else{
            return arr[mid];
        }

    }
}