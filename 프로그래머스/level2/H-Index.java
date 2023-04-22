import java.util.Arrays;

class Solution {
    private boolean isValid(int[] citations, int h){
        // h 조건 검사
        int index = citations.length - h;
        return citations[index] >= h;
    }
    
    public int solution(int[] citations) {
        Arrays.sort(citations);
        for(int h = citations.length; h >= 1; h--){
            if(isValid(citations, h)) return h;
        }
        
        return 0;
    }
}