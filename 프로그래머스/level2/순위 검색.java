import java.util.*;
import java.util.function.Consumer;

class Solution {
    private void forEachKey(int index, String prefix, String[] tokens,
                            Consumer<String> action){
        if (index == tokens.length - 1) {
            // prefix가 만들어진 검색 조건
            action.accept(prefix);
            return;
        }
        
        forEachKey(index + 1, prefix + tokens[index], tokens, action);
        forEachKey(index + 1, prefix + "-", tokens, action);
    }
    
    private Map<String, List<Integer>> buildScoresMap(String[] info) {
        Map<String, List<Integer>> scoresMap = new HashMap<>();
        
        //전처리
        for(String s : info){
            String[] tokens = s.split(" ");
            int score = Integer.parseInt(tokens[tokens.length - 1]);
            // scoresMap에 추가
            forEachKey(0, "", tokens, key -> {
                scoresMap.putIfAbsent(key, new ArrayList<>());
                scoresMap.get(key).add(score);
            });
        }
        
        for(List<Integer> list : scoresMap.values()){
            Collections.sort(list);
        }
        
        return scoresMap;
    }
    
    private int binarySearch(int score, List<Integer> scores){
        int start = 0;
        int end = scores.size() - 1;
        
        while(end > start) {
            int mid = (start + end) / 2;
            
            if(scores.get(mid) >= score){
                end = mid;
            } else {
                start = mid + 1;
            }
        }
        
        if(scores.get(start) < score){
            return scores.size();
        }
        return start;
    }
    
    private int count(String query, Map<String, List<Integer>> scoresMap){
        // scoresMap을 이용하여 query에 맞는 지원자 수 세긷
        String[] tokens = query.split(" (and )?");
        
        String key = String.join("", Arrays.copyOf(tokens, tokens.length - 1));
        
        if(!scoresMap.containsKey(key)) return 0;
        List<Integer> scores = scoresMap.get(key);
        
        int score = Integer.parseInt(tokens[tokens.length - 1]);
        
        return scores.size() - binarySearch(score, scoresMap.get(key));
    }
    
    public int[] solution(String[] info, String[] query) {
        Map<String, List<Integer>> scoresMap = buildScoresMap(info);
        
        int[] answer = new int[query.length];
        for(int i = 0; i < answer.length; i++){
            // 정답 구하기
            answer[i] = count(query[i], scoresMap);
        }
        return answer;
    }
}