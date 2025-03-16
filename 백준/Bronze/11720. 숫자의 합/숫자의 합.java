import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            // 첫쨰 줄에 숫자의 개수 N개 주어진다.
            String N = sc.nextLine();
            int n = Integer.parseInt(N);

            String k = sc.nextLine();
            String[] digits = k.split("");

            int sum = 0;

            for (int i = 0; i < n; i++) {
                sum += Integer.parseInt(digits[i]);
            }

            System.out.println(sum);

        }
    }
