class Solution {
    private int countZeros(String s){
        int zeros = 0;
        for (char c : s.toCharArray()){
            if (c == '0') zeros++;
        }
        return zeros;
    }
    
    public int[] solution(String s) {
        int loop = 0;
        int removed = 0;
        
        // s가 "1"이 될 때까지 반복하며 loop, removed 누적
        while(!s.equals("1")){
            // s 변환하며 loop, removed 누적
            int zeros = countZeros(s);
            loop += 1;
            removed += zeros;
            
            // 문자열 s 변환
            int ones = s.length() - zeros;
            s = Integer.toString(ones, 2);
        }
        
        
        return new int[] {loop, removed};
    }
}