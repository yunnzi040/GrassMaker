import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        sc.nextLine(); // 남은 개행문자를 제거해야한다
        int correct = 0;
        int count = 0;

        for (int i = 0; i < T; i++) {
            String ox = sc.nextLine();

            for (int j = 0; j < ox.length(); j++) {
                if (ox.charAt(j) == 'O') {
                    correct += 1;
                } else if (ox.charAt(j) == 'X') {
                    correct = 0;
                }
                count += correct;
            }
            System.out.println(count);
            count = 0;
            correct = 0;
        }
    }
}