import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int N = sc.nextInt();

            for (int i = 1; i <= N; i++) { // 행 반복

                // 별 출력
                for (int j = 0; j <= N - i; j++) {
                    System.out.print("*");
                }
                System.out.println(); // 줄 바꿈
            }
        }
}

