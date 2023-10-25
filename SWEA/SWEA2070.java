import java.util.Scanner;

public class SWEA2070 {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        String[] strList = new String[T];
        for (int test_case = 1; test_case <= T; test_case++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            if (a < b) {
                strList[test_case - 1] = "<";
            } else if (a == b) {
                strList[test_case - 1] = "=";
            } else {
                strList[test_case - 1] = ">";
            }
        }

        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("#" + test_case + " " + strList[test_case - 1]);
        }
    }
}
