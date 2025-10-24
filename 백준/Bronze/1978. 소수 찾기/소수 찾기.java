import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int prime = 0;
        Integer[] numbers  = new Integer[N];

        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }

        boolean isPrime = true;
        for (int i = 0; i < N; i++) {
            if (numbers[i] == 1) { // 1일 경우는 제외시키기
                continue;
            }
            for (int j = 2; j <= Math.sqrt(numbers[i]); j++) {
                if (numbers[i] % j == 0) { // 나누어 떨어질 경우
                    isPrime = false; // 소수가 아님
                    break;
                }
            }
            if (isPrime) { // 소수일 경우
                prime++; // 카운트하기
            }
            isPrime = true; // 초기화하기
        }
        System.out.println(prime);
    }
}