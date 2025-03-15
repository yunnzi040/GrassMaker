import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int sum = 0;

            String T = sc.nextLine();
            int cnt = Integer.parseInt(T);

            for(int i = 0; i < cnt; i++){
                int a = sc.nextInt();
                int b = sc.nextInt();
                sum = a + b;

                System.out.println("Case #" + (i+1) + ": " + sum);
            }
        }
    }