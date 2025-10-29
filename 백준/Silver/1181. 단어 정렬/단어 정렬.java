import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) throws IOException {
        int N = sc.nextInt();

        Comparator<String> comparator = Comparator
                .comparingInt(String::length) // 문자열 길이 기준
                .thenComparing(Comparator.naturalOrder()); // 사전순

        TreeSet<String> set = new TreeSet<>(comparator); // 중복 확인 및 알파벳 순으로 자동 정렬됨

        for (int i = 0; i < N; i++) {
            set.add(sc.next());
        }

        for (String s : set) {
            System.out.println(s);
        }
    }
}