import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        // 두 정수 A와 B를 입력 받음
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        System.out.println(A + B - C);

        // AB를 문자열을 사용해서 붙여서 다시 숫자로 만듬
        String AB = Integer.toString(A) + Integer.toString(B);

        System.out.println(Integer.parseInt(AB) - C);
    }
}