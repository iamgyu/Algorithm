import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class SWEA1933 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        List<Integer> list = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                list.add(i);
            }
        }
        list.forEach(num -> System.out.print(num + " "));
    }
}
