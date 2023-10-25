import java.util.Scanner;

public class SWEA2071 {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        int[] avgList = new int[T];

        for (int test_case = 1; test_case <= T; test_case++) {
            int avg = 0;
            float sum = 0;
            for (int i = 0; i < 10; i++) {
                int n = sc.nextInt();
                sum += n;
            }
            avg = Math.round(sum / 10);
            avgList[test_case - 1] = avg;
        }

        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("#" + test_case + " " + avgList[test_case - 1]);
        }
    }
}
