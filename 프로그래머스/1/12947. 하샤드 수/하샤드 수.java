class Solution {
    public boolean solution(int x) {
        boolean answer = true;
        int sum = 0;
        String str = String.valueOf(x);
        
        String[] arr = str.split("");
        
        for(int i=0; i<arr.length; i++){
            sum += Integer.parseInt(arr[i]);
        }
        if(x % sum == 0){
            answer = true;
        }else{
            answer = false;
        }
        return answer;
    }
}