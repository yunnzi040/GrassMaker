import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        List<String> list = new ArrayList<>();
        for (int i = 0; i < 3; i++) {
            list.add(br.readLine());
        }
        if (list.get(2).matches("\\d+")) { // 정규식: 숫자만 있는지 확인
            solve((Integer.parseInt(list.get(2)) + 1));
        } else { // 마지막 문자열이 숫자로 되어있지 않은 경우
            if (list.get(0).matches("\\d+")) { // 첫번째 문자열이 숫자인지 확인
                solve((Integer.parseInt(list.get(0)) + 3));
            } else if (list.get(1).matches("\\d+")){ // 두번째 문자열이 숫자인지 확인
                solve((Integer.parseInt(list.get(1)) + 2));
            }
        }
    }

    public static void solve(int num) {
        String nextNum;

        if (num % 3 == 0 && num % 5 == 0) {
            nextNum = "FizzBuzz";
        } else if (num % 3 == 0) {
            nextNum = "Fizz";
        } else if (num % 5 == 0) {
            nextNum = "Buzz";
        } else {
            nextNum = String.valueOf(num);
        }
        System.out.println(nextNum);
    }
}