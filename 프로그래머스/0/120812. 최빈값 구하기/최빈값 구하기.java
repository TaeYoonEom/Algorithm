class Solution {
    public int solution(int[] array) {
        int max = 0;

        // 1. 배열에서 가장 큰 숫자 찾기
        for (int i = 0; i < array.length; i++) {
            if (max < array[i]) {
                max = array[i];
            }
        }

        // 2. 등장 횟수 배열 생성
        int[] count = new int[max + 1];

        // 3. 각 숫자의 등장 횟수 계산
        for (int i = 0; i < array.length; i++) {
            count[array[i]]++;
        }

        // 4. 최빈값 찾기
        int maxCount = 0;
        int answer = 0;

        for (int i = 0; i < count.length; i++) {
            if (count[i] > maxCount) {
                maxCount = count[i];
                answer = i;
            } else if (count[i] == maxCount) {
                answer = -1;
            }
        }

        return answer;
    }
}