import java.util.Scanner;

public class SWEA2029 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        int[] arr = new int[T * 2];
        for (int i = 0; i < T * 2; i += 2) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            arr[i] = a / b;
            arr[i + 1] = a % b;
        }

        for (int i = 0; i < T * 2; i += 2) {
            System.out.println("#" + (i / 2 + 1) + " " + arr[i] + " " + arr[i + 1]);
        }
    }
}
