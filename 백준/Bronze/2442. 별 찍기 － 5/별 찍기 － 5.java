import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int N = sc.nextInt();

            for (int i = 1; i <= N; i++) { // 행 반복

                // 왼쪽 공백 출력
                for (int k = 0; k < N-i; k++) {
                    System.out.print(" ");

                }
                // 별 출력
                System.out.print("*".repeat((2*i)-1));
                

                System.out.println(); // 줄 바꿈
            }
        }
}

