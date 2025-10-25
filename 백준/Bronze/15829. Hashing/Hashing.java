import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        sc.nextLine();
        String sentence = sc.nextLine();

        int sum = 0;
        List<String> words = List.of(sentence.split(""));

        for (int i = 0; i < L; i++) {
            char word = words.get(i).charAt(0);
            int temp = 1;
            for (int j = 0; j < i; j++) {
                temp *= 31;
            }
            sum += temp * (word - 96);
        }
        System.out.println(sum);
    }
}