import java.util.Scanner;

public class SWEA2050 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word = sc.nextLine().toUpperCase();

        for (int i = 0; i < word.length(); i++) {
            if (i + 1 == word.length()) {
                System.out.println((int) word.charAt(i) - 64);
            } else {
                System.out.print((int) word.charAt(i) - 64 + " ");
            }
        }
    }
}
