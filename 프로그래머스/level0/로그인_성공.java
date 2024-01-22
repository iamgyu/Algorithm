package 프로그래머스.level0;

public class 로그인_성공 {
    public String solution(String[] id_pw, String[][] db) {
        String answer = "fail";
        for (int i = 0; i < db.length; i++) {
            for (int j = 0; j < id_pw.length; j++) {
                if (id_pw[0].equals(db[i][0]) && id_pw[1].equals(db[i][1])) {
                    answer = "login";
                    break;
                }

                if (id_pw[0].equals(db[i][0]) && !id_pw[1].equals(db[i][1])) {
                    answer = "wrong pw";
                }
            }
        }
        return answer;
    }
}
