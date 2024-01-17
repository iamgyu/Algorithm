package 프로그래머스.level0;

public class 외계어사전 {
    public int solution(String[] spell, String[] dic) {
        int answer = 2;

        for (String d : dic) {
            boolean b = true;

            for(String s : spell){
                if(!d.contains(s)){
                    b = false;
                    break;
                }
            }

            if(b){
                answer = 1;
            }
        }

        return answer;
    }
}
