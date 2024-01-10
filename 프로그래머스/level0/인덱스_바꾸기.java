package 프로그래머스.level0;

public class 인덱스_바꾸기 {
    public String solution(String my_string, int num1, int num2) {
        char[] arr = my_string.toCharArray();
        char temp = arr[num1];
        arr[num1] = arr[num2];
        arr[num2] = temp;
        return String.valueOf(arr);
    }
}
