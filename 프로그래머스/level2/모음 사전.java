import java.util.ArrayList;
import java.util.List;

class Solution {
    private static final char[] CHARS = "AEIOU".toCharArray();
    
    private void generate(String word, List<String> words){
        // 종료 조건
        words.add(word);
        if(word.length() == 5) return;
        
        // 점화식 구현
        for(char c : CHARS){
            generate(word + c, words);
        }
    }
    
    public int solution(String word) {
        List<String> words = new ArrayList<>();
        generate("", words);
        return words.indexOf(word);
    }
}