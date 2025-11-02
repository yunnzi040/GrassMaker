import java.io.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int count = 0;
        int check = 666;

        while (true) {
            if (String.valueOf(check).contains("666")){
                count++;
                if (count == N){
                    break;
                }
            }
            check++;
        }
        System.out.println(check);
    }
}