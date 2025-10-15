import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        // 두 정수 H(시)와 M(분)이 주어진다. 입력 시간은 24시간 표현을 사용한다.
        Scanner input = new Scanner(System.in);

        int H = input.nextInt();
        int M = input.nextInt();

        if (H == 0){
            if (M < 45){
                System.out.println(23 + " " + (M+60-45));
            } else {
                System.out.println(H + " " + (M-45));
            }
        } else {
            if (M < 45){
                System.out.println((H-1) + " " + (M+60-45));
            } else {
                System.out.println(H + " " + (M-45));
            }
        }
    }
}