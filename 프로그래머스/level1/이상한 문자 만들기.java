class Solution {
    public String solution(String s) {
        StringBuilder builder = new StringBuilder();
        boolean toUpper = true;
        
        for (char c : s.toCharArray()){
            // c를 적절히 변환하여 builder에 추가
            if (!Character.isAlphabetic(c)){
                // 공백 처리
                builder.append(c);
                toUpper = true;
            } else {
                // 알파벳 변환
                if (toUpper) {
                    builder.append(Character.toUpperCase(c));
                } else {
                    builder.append(Character.toLowerCase(c));
                }
                toUpper = !toUpper;
            }
        }
        return builder.toString();
    }
}