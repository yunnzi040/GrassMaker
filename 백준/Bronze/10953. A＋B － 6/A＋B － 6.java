import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            int sum = 0;

            String T = sc.nextLine();
            int cnt = Integer.parseInt(T);

            for(int i = 0; i < cnt; i++){
                String input = sc.nextLine();
                String[] nums = input.split(",");
                int a = Integer.parseInt(nums[0]);
                int b = Integer.parseInt(nums[1]);
                sum = a + b;

                System.out.println(sum);
            }
        }
    }
