import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class SWEA2068 {
    public static void main(String args[]) throws Exception {

        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        int[] arr = new int[T];
        for (int test_case = 1; test_case <= T; test_case++) {
            List<Integer> list = new ArrayList<>();
            for (int i = 0; i < 10; i++) {
                int n = sc.nextInt();
                list.add(n);
            }
            arr[test_case - 1] = Collections.max(list);
        }

        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("#" + test_case + " " + arr[test_case - 1]);
        }
    }
}
