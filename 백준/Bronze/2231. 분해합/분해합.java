import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        /*
        * 분해합 = 수 = 각 자리수 합
        * */

        int N = sc.nextInt();
        int temp = N;
        int count = 0;

        // 자리수 갯수 구하기
        while (temp > 0) {
            count++;
             temp /= 10;
        }

        int start = Math.max(1, N - count * 9);
        boolean found = false;
        for (int m = start; m <= N; m++){
            int M = 0;
            // m의 각 자리수 더하기
            int num = m;
            while (num > 0){
                M += num % 10;
                num /= 10;
            }

            if ((M + m) == N){
                System.out.println(m);
                found = true;
                break;
            }
        }
        if (!found){
            System.out.println(0);
        }
    }
}