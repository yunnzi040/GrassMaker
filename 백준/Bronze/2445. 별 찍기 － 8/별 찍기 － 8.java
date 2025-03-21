import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int N = sc.nextInt();

            // 윗부분 파트 출력
            for (int i = 1; i <= N; i++) { // 행 반복

                // 왼쪽 별 출력
                for (int k = 0; k < i; k++) {
                    System.out.print("*");
                }
                // 공백 출력
                for (int b = 0; b < 2*(N - i); b++) {
                    System.out.print(" ");
                }

                // 오른쪽 별 출력
                for (int j = 0; j < i; j++) {
                    System.out.print("*");
                }
                System.out.println();
            }

            // 아랫부분 파트 출력

            for (int m = N-1; m >= 0; m--) {
                // 왼쪽 별 출력
                for (int n = 1; n <= m; n++) {
                    System.out.print("*");
                }

                // 공백 출력
                for (int a = 1; a <= 2 * (N-m); a++) {
                    System.out.print(" ");
                }

                // 오른쪽 별 출력
                for (int j = 0; j < m; j++) {
                    System.out.print("*");
                }

                System.out.println();
            }
        }
}

