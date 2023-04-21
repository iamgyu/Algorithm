import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(String s) {
        int min = Integer.MAX_VALUE;
        for(int length = 1; length <= s.length(); length++){
            // 문자열 압축 후 가장 짧은 길이 선택
            int compressed = compress(s, length);
            if (compressed < min){
                min = compressed;
            }
        }
        return min;
    }
    
    private int compress(String source, int length){
        // 압축한 문자열의 길이 반환
        StringBuilder builder = new StringBuilder();
        String last = "";
        int count = 0;
        
        for(String token : split(source, length)){
            // 압축 문자열 구성
            if (token.equals(last)) {
                count++;
            } else {
                // 새로운 토큰 등장 처리
                if (count > 1) builder.append(count);
                builder.append(last);
                last = token;
                count = 1;
            }
        }
        if (count > 1) builder.append(count);
        builder.append(last);
        
        return builder.length();
    }
    
    private List<String> split(String source, int length){
        List<String> tokens = new ArrayList<>();
        // source를 length만큼씩 잘라 tokens 리스트에 추가
        for (int startIndex = 0; startIndex < source.length(); startIndex += length){
            // 문자열을 startIndex부터 잘라 tokens 리스트에 추가
            int endIndex = startIndex + length;
            if (endIndex > source.length()) endIndex = source.length();
            // 문자열을 startIndex부터 endIndex까지 잘라 tokens 리스트에 추가
            tokens.add(source.substring(startIndex, endIndex));
        }
        return tokens;
    }
}