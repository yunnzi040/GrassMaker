import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] C = new int[T];

        for (int i = 0; i < T; i++) {
            C[i] = sc.nextInt();
        }

        for (int i = 0; i < T; i++) {
            int quater = C[i] / 25 ;
            int dime = C[i] % 25 / 10 ;
            int Nickel = C[i] % 25 % 10 / 5;
            int Penny = C[i] % 25 % 10 % 5;
            System.out.println(quater + " " + dime + " " + Nickel + " " + Penny);
        }



    }
}

