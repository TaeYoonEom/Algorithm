class Solution {
    public int solution(int[] number) {
        int answer = 0;
        int size = number.length;

        for(int i = 0; i < size - 2; i++){ // 처음 숫자 number[0]
            for(int j = i + 1; j < size - 1;j++){ // 두번째 숫자 number[1]
                for(int z = j + 1; z < size; z++){ // 세번째 숫자 number[2]
                    if(number[i] + number[j] + number[z] == 0){ 
                        // 3개 합이 0이면 카운트
                        answer++;
                    }
                }
            }    
        }
        return answer;
    }
}