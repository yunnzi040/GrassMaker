import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        // 자바에서 제곱수 나타낼 때 사용 - 원래는 double이라 int로 변환해야함.
        int result = (int) Math.pow(2, N) + 1;
        System.out.println(result * result);
    }
}

