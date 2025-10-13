import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 9개의 자연수를 입력받는다.
        Scanner sc = new Scanner(System.in);
        int max = 0;
        int idx = 0;

        for (int i=1; i<10; i++){
            int number = sc.nextInt();
            // 입력받은 수가 최댓값보다 작을 경우
            if (number > max){
                max = number;
                idx = i;
            }
        }
        System.out.println(max);
        System.out.println(idx);
    }
}