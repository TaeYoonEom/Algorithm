import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        Set<Integer> types = new HashSet<>();
        int limit = nums.length / 2;
        
        for(int number : nums){
            types.add(number);
        }
        
        if(limit < types.size()){
            return limit;
        }else{
            return types.size();
        }
    }
}