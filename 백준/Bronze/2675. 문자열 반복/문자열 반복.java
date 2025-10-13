import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 입력 '3 ABC'
        Scanner sc = new Scanner(System.in);

        // 테스트 케이스 개수
        int T = sc.nextInt();
        sc.nextLine(); // 이걸 하는 이유?? next 어쩌구들의 차이가 좀 중요하나봐

        for (int i = 0; i < T; i++) {
            // 입력이 '3 ABC' 일 경우, ['3', 'ABC']로 나누기
            String[] words = sc.nextLine().split(" ");
            // ['A', 'B', 'C']로 나누기
            String[] word = words[1].split("");
            int count = Integer.parseInt(words[0]);

            for (String w : word) {
                System.out.print(w.repeat(count));
            }
            System.out.println();
        }
    }
}