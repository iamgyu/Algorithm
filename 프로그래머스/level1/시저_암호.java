public class 시저_암호 {
    public String solution(String s, int n) {
        char[] arr = s.toCharArray();
        for (int i = 0; i < arr.length; i++) {
            if ((int) arr[i] > 64 && (int) arr[i] < 91) {
                if ((int) arr[i] + n > 90)
                    arr[i] = (char) (arr[i] + n - 26);
                else
                    arr[i] = (char) (arr[i] + n);
            } else if ((int) arr[i] > 96 && (int) arr[i] < 123) {
                if ((int) arr[i] + n > 122)
                    arr[i] = (char) (arr[i] + n - 26);
                else
                    arr[i] = (char) (arr[i] + n);
            }
        }
        return String.valueOf(arr);
    }
}
