package 프로그래머스.level0;

import java.util.ArrayList;
import java.util.List;

public class OX퀴즈 {
    public String[] solution(String[] quiz) {
        List<String> list = new ArrayList<>();
        int i = 0;
        for (String str : quiz) {
            String[] arr = str.split(" ");
            if(arr[1].equals("+")){
                if (Integer.parseInt(arr[0]) + Integer.parseInt(arr[2]) == Integer.parseInt(arr[4]))
                    list.add("O");
                else
                    list.add("X");
            }else{
                if(Integer.parseInt(arr[0]) - Integer.parseInt(arr[2]) == Integer.parseInt(arr[4]))
                    list.add("O");
                else
                    list.add("X");
            }
        }
        return list.toArray(new String[list.size()]);
    }
}