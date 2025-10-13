import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        String[] word = sc.nextLine().split("");
        int i = sc.nextInt();

        System.out.println(word[i-1]);
    }
}