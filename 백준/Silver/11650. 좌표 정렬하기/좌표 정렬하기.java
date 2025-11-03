import java.io.*;
import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Map.Entry;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        List<Entry<Integer, Integer>> pairs = new ArrayList<>();

        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            pairs.add(new SimpleEntry<>(x, y));
        }

        pairs.sort(
                Comparator.comparing(Entry<Integer, Integer>::getKey)
                .thenComparing(Entry::getValue)
        );

        for (Entry<Integer, Integer> pair : pairs) {
            System.out.println(pair.getKey() + " " + pair.getValue());
        }
    }
}