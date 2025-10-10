import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        double result = (double) n  / m;
        System.out.println(result);
    }
}