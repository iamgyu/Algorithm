package 프로그래머스.level0;

public class 캐릭터의_좌표 {
    public int[] solution(String[] keyinput, int[] board) {
        int x = 0;
        int y = 0;
        for (String input : keyinput) {
            if(input.equals("up"))
                y++;
            if(input.equals("down"))
                y--;
            if(input.equals("right"))
                x++;
            if(input.equals("left"))
                x--;

            if(x > board[0] / 2)
                x = board[0] / 2;
            if(x < (board[0] / 2) * -1)
                x = board[0] / 2 * -1;
            if(y > board[1] / 2)
                y = board[1] / 2;
            if(y < (board[1] / 2) * -1)
                y = board[1] / 2 * -1;
        }
        return new int[]{x, y};
    }
}
