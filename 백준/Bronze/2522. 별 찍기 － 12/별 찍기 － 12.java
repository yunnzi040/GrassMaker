import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        // 윗부분 파트 출력
        for (int i = N; i > 0; i--) {

            // 공백 출력
            for (int j = 0; j < i-1; j++) {
                System.out.print(" ");
            }

            // 별 출력
            for (int j = 0; j <= N - i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        //아랫부분 파트 출력
        for (int i = 1; i < N; i++) {
            // 공백 출력
            for (int j = 0; j < i; j++) {
                System.out.print(" ");
            }
            // 별 출력
            for (int k = 0; k < N-i; k++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}

