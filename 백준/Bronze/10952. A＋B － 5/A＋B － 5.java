import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while(sc.hasNext()){
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (a == 0 && b == 0){
                break;
            }
            int sum = a+b;
            System.out.println(sum);
        }
    }
}