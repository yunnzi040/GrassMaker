import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        /*
        * 3개의 자연수 A, B, C를 입력 받기
        * 세 자연수를 곱한 결과에서
        * 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지 구하는 프로그램 작성
        * */

        Scanner input = new Scanner(System.in);
        List<Integer> inputNums = new ArrayList<>();
        int complex = 1;

        // 세 자연수를 입력 받기
        for (int i = 0; i < 3; i++) {
            inputNums.add(input.nextInt());
            complex *= inputNums.get(i);
        }

        // 각 자릿수를 문자로 바꿔야 숫자를 자릿수로 인식할 수 있을 듯
        String digits = String.valueOf(complex);
        List<String> digitsList = List.of(digits.split(""));
        int count = 0;

        for (int i = 0; i < 10; i++) {
            // 리스트 각 값들을 유니코드를 사용해서 비교하기
            for (String s : digitsList) {
                if (s.charAt(0) == (char) ('0' + i)) {
                    count++;
                }
            }
            System.out.println(count);
            count = 0;
        }
    }
}