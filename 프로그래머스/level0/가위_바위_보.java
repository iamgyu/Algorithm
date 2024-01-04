package 프로그래머스.level0;

public class 가위_바위_보 {
    public String solution(String rsp) {
        char[] charArr = rsp.toCharArray();
        StringBuilder sb = new StringBuilder();

        for (char c : charArr) {
            if(c == '2') sb.append('0');
            if(c == '5') sb.append('2');
            if(c == '0') sb.append('5');
        }

        return sb.toString();
    }
}