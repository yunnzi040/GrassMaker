
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String sentence = sc.nextLine().trim();

        if (sentence.isEmpty()) {
            System.out.println("0");
        } else {
            String[] words = sentence.split("\\s+");
            System.out.println(words.length);

        }
    }
}



