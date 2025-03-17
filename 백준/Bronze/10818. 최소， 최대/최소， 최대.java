 import java.util.Scanner;

public class Main {
        public static void main(String[] args) {

            //배열을 쓰지 않고 입력용 변수 하나로만 해보자
            Scanner sc = new Scanner(System.in);
            int N = sc.nextInt();
            int[] nums = new int[N];

            for (int i = 0; i < N; i++) {
                nums[i] = sc.nextInt();
            }

            int maxNum = -1000000;
            int minNum = 1000000;

            for (int i = 0; i < N; i++) {
                if (nums[i] > maxNum) {
                    maxNum = nums[i];
                }
                if (nums[i] < minNum) {
                    minNum = nums[i];
                }
            }
            System.out.println(minNum + " " + maxNum);
        }
}
