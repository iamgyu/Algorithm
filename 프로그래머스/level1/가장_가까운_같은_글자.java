public class 가장_가까운_같은_글자 {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < i; j++) {
                if(arr[i] == arr[j])
                    answer[i] = i - j;
            }
            if(answer[i] == 0)
                answer[i] = -1;
        }
        return answer;
    }
}
