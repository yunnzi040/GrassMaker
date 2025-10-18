import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        Set<Integer> numberSet = new HashSet<>();

        // 숫자 10개 무작위로 입력 받고 43으로 나눈 나머지
        for (int i = 0; i < 10; i++){
            int number = sc.nextInt();
            numberSet.add(number % 42);
        }
        System.out.println(numberSet.size());
    }
}