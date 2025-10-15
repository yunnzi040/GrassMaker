import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        /*  고유번호 00000 ~ 99999 중 하나
            검증수는 고유번호의 각 자릿수들을 각각 제곱한 수의 합을 10으로 나눈 나머지
         */

        Scanner input = new Scanner(System.in);
        List<Integer> numbers = new ArrayList<>();
        int check = 0;

        // 고유번호 각각 입력 받기
        for (int i=0; i<5; i++){
            numbers.add(input.nextInt());
            check += numbers.get(i) * numbers.get(i);
        }
        System.out.println(check % 10);

    }
}