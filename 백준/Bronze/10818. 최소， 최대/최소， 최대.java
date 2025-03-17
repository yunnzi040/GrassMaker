import java.util.Scanner;

public class Main {
        public static void main(String[] args) {

            //배열을 쓰지 않고 입력용 변수 하나로만 해보자
            Scanner sc = new Scanner(System.in);
            int N = sc.nextInt();

            int maxNum = -1000000;
            int minNum = 1000000;

            for (int i = 0; i < N; i++) {
                int num = sc.nextInt();
                if (num > maxNum) {
                    maxNum = num;
                }
                if (num < minNum) {
                    minNum = num;
                }
            }
            System.out.println(minNum + " " + maxNum);
        }
}
