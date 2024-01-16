package 프로그래머스.level0;

public class 다항식_더하기 {
    public String solution(String polynomial) {
        StringBuilder answer = new StringBuilder();
        int x = 0;
        int num = 0;
        String[] arr = polynomial.split(" ");

        for (String s : arr) {
            if(s.equals("+"))
                continue;
            if(s.contains("x")){
                if(s.length() == 1)
                    x += 1;
                else
                    x += Integer.parseInt(s.replace("x", ""));
            } else{
                num += Integer.parseInt(s);
            }
        }
        if (num == 0) {
            if(x == 1)
                answer.append("x");
            else
                answer.append(x).append("x");
        } else {
            if(x == 0)
                answer.append(num);
            else if(x == 1)
                answer.append("x").append(" + ").append(num);
            else
                answer.append(x).append("x + ").append(num);
        }

        return answer.toString();
    }
}
