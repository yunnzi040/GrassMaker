import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int L = sc.nextInt();
        sc.nextLine();
        String sentence = sc.nextLine();

        long sum = 0;
        List<String> words = List.of(sentence.split(""));

        for (int i = 0; i < L; i++) {
            char word = words.get(i).charAt(0);
            long temp = 1;
            for (int j = 0; j < i; j++) {
                temp = (temp * 31) % 1234567891;
            }
            sum = (sum + temp * (word - 96)) % 1234567891 ;
        }
        System.out.println(sum);
    }
}