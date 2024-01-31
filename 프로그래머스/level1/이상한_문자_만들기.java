public class 이상한_문자_만들기 {
    public String solution(String s) {
        s = s.toLowerCase();

        StringBuilder sb = new StringBuilder();
        String[] arr = s.split("");

        boolean upper = true;
        for (String a : arr) {
            if (upper) {
                sb.append(a.toUpperCase());
            } else {
                sb.append(a);
            }

            upper = !upper;
            if (a.equals(" ")) {
                upper = true;
            }
        }

        return sb.toString();
    }
}
