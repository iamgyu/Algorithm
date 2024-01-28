public class 문자열_내_p와_y의_개수 {
    boolean solution(String s) {
        int count_p = 0;
        int count_y = 0;
        String temp = s.toLowerCase();

        for (char c : temp.toCharArray()) {
            if(c == 'p')
                count_p++;
            if(c == 'y')
                count_y++;
        }

        return count_p == count_y;
    }
}
