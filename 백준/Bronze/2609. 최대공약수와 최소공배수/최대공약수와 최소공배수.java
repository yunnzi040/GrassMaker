import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static int A = sc.nextInt();
    static int B = sc.nextInt();

    public static void main(String[] args) throws IOException {
        // 최대공약수
        int gcd = gcd(A,B);

        int m = A / gcd;
        int n = B / gcd;

        System.out.println(gcd);
        System.out.println(m * n * gcd);
    }

    // 최대공약수 - 유클리드 호제법 사용
    /*
    * 두 수 A, B가 있을 때,
    * GCD(A, B) = GCD(B, A % B)로 점점 나누면서 작은 수를 찾아가는 방법
    * 나머지가 0이 되면 나머지 0이 될 때 나눈 수가 최대공약수가 된다.
    * */
    public static int gcd(int a, int b) {
        if (b == 0){
            return a;
        }
        return gcd(b, a % b);
    }
}