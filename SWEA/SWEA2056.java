import java.util.Scanner;

public class SWEA2056 {
    public static void main(String args[]) throws Exception {
        int[] days = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        Scanner sc = new Scanner(System.in);
        int T;
        T = sc.nextInt();
        sc.nextLine();

        String[] strList = new String[T];
        for (int test_case = 1; test_case <= T; test_case++) {
            String str = sc.nextLine();
            String year = str.substring(0, 4);
            String month = str.substring(4, 6);
            String day = str.substring(6, 8);

            int intMonth = Integer.parseInt(month);
            int intDay = Integer.parseInt(day);
            if ((intMonth > 0 && intMonth < 13) && (intDay > 0 && days[intMonth - 1] >= intDay)) {
                strList[test_case - 1] = year + "/" + month + "/" + day;
            } else {
                strList[test_case - 1] = "-1";
            }
        }

        for (int test_case = 1; test_case <= T; test_case++) {
            System.out.println("#" + test_case + " " + strList[test_case - 1]);
        }
    }
}
