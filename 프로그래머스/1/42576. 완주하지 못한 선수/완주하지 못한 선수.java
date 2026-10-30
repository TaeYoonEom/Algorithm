import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> naming = new HashMap<>();
        
        for(String name: participant){
            if(naming.containsKey(name)){
                naming.put(name, naming.get(name)+1);
            } else {
                naming.put(name, 1);    
            }
        }
        
        for(String name2:completion){
            if(naming.containsKey(name2)){
                naming.put(name2, naming.get(name2)-1);
            }
        }
        
        for(String name:naming.keySet()){
            if(naming.get(name) == 1){
                return name;
            }
        }
        return "";
    }
}