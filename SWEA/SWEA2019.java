import java.util.Scanner;

public class SWEA2019 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int mul = 1;

        for (int i = 0; i <= n; i++) {
            System.out.print(mul + " ");
            mul *= 2;
        }
    }
}
