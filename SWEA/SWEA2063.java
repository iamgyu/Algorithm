import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class SWEA2063 {
    public static void main(String args[]) throws Exception {
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();

        List<Integer> list = new ArrayList<>();
        for (int test_case = 1; test_case <= T; test_case++) {
            int n = sc.nextInt();
            list.add(n);
        }
        Collections.sort(list);
        System.out.println(list.get(T / 2));
    }
}
