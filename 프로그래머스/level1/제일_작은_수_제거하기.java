public class 제일_작은_수_제거하기 {
    public int[] solution(int[] arr) {
        if (arr.length == 1)
            return new int[]{-1};

        int[] answer = new int[arr.length - 1];
        int min = arr[0];

        for (int i : arr) {
            min = Math.min(min, i);
        }

        int n = 0;
        for (int i = 0; i < arr.length; i++) {
            if(arr[i] == min)
                continue;

            answer[n++] = arr[i];
        }
        return answer;
    }
}
