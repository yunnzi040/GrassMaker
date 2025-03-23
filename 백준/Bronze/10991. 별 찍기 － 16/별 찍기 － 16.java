import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        // 윗부분 파트 출력
        for (int i = 1; i <= N; i++) {
            // 공백 찍기
            for (int k = 0; k < N - i; k++) {
                System.out.print(" ");
            }

            // 별 찍기
            for (int j = 1; j <= ((2 * i) - 1); j++) {
                if (j % 2 == 0) {
                    System.out.print(" ");
                } else {
                    System.out.print("*");
                }
            }
            System.out.println();
        }
    }
}

