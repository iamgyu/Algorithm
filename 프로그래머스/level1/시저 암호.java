class Solution {
    private char push(char c, int n){
        // c가 알파벳이 아니라면 그대로 반환
        if(!Character.isAlphabetic(c)) return c;
        
        // c를 n만큼 밀어 반환
        int offset = Character.isUpperCase(c) ? 'A' : 'a';
        int position = c - offset;
        position = (position + n) % ('Z' - 'A' + 1);
        
        return (char) (offset + position);
    }
    public String solution(String s, int n) {
        StringBuilder builder = new StringBuilder();
        for(char c : s.toCharArray()){
            // c를 n만큼 민 문자를 builder에 이어 붙이기
            builder.append(push(c, n));
        }
        return builder.toString();
    }
}