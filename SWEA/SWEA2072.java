import java.util.Scanner;

public class SWEA2072 {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        int[] sumList = new int[T];

        for (int test_case = 1; test_case <= T; test_case++) {
            int sum = 0;
            for (int i = 0; i < 10; i++) {
                int n = sc.nextInt();
                if (n % 2 == 1) {
                    sum += n;
                }
            }
            sumList[test_case - 1] = sum;
        }

        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("#" + test_case + " " + sumList[test_case - 1]);
        }
    }
}
