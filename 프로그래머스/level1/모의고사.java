import java.util.Arrays;
import java.util.stream.IntStream;

public class 모의고사 {
    public int[] solution(int[] answers) {
        int[] person1 = new int[]{1, 2, 3, 4, 5};
        int[] person2 = new int[]{2, 1, 2, 3, 2, 4, 2, 5};
        int[] person3 = new int[]{3, 3, 1, 1, 2, 2, 4, 4, 5, 5};
        int[] correct = new int[3];


        for (int i = 0; i < answers.length; i++) {
            if(answers[i] == person1[i % person1.length])
                correct[0]++;
            if(answers[i] == person2[i % person2.length])
                correct[1]++;
            if(answers[i] == person3[i % person3.length])
                correct[2]++;
        }

        int max = Arrays.stream(correct).max().orElse(0);
        return IntStream.range(0, 3)
                .filter(i -> correct[i] == max)
                .map(i -> i + 1)
                .toArray();
    }
}
