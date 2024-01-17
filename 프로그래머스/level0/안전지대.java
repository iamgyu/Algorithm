package 프로그래머스.level0;

public class 안전지대 {
    public int solution(int[][] board) {
        int answer = 0;
        int[][] newBoard = new int[board.length + 2][board.length + 2];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if(board[i][j] == 1){
                    for (int a = i; a <= i + 2; a++) {
                        for (int b = j; b <= j + 2; b++) {
                            if (newBoard[a][b] != 1) {
                                newBoard[a][b] = 2;
                            }
                        }
                    }
                }
            }
        }

        for (int i = 1; i < newBoard.length - 1; i++) {
            for (int j = 1; j < newBoard.length - 1; j++) {
                if(newBoard[i][j] == 0)
                    answer++;
            }
        }
        return answer;
    }
}
