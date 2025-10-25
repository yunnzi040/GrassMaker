import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();
        double max = 0;
        List<Double> numbers = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            double score = sc.nextDouble();
            numbers.add(score);
            if (score > max) {
                max = score;
            }
        }

        double sum = 0;
        for (int i = 0; i < N; i++) {
            double newScore = numbers.get(i) / max * 100;
            numbers.set(i, newScore);
            sum += newScore;
        }
        System.out.println(sum / N);
    }
}