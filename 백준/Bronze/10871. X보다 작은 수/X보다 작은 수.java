import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int X = sc.nextInt();

        List<Integer> numbers = new ArrayList<>();

        // 자연수를 N개 입력받기
        for (int i = 0; i < N; i++) {
            numbers.add(sc.nextInt());
        }

        // X 보다 작은 자연수를 입력받은 순서대로 공백으로 구분해 출력
        for (int i = 0; i < N; i++) {
            if (numbers.get(i) < X) {
                System.out.print(numbers.get(i)+" ");
            }
        }


    }
}