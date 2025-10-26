import java.io.*;
import java.util.*;

public class Main {
    static Scanner sc = new Scanner(System.in);
    static String ISBN = sc.nextLine();
    static int sum = 0;
    static int weight = 0;


    public static void main(String[] args) throws IOException {
        List<String> nums = List.of(ISBN.split(""));
        for (int i = 0; i < nums.size(); i++) {
            if (nums.get(i).equals("*")) {
                if (i % 2 != 0) { // 홀수번째
                    weight = 3;
                } else {
                    weight = 1;
                }
                continue;
            }
            if (i % 2 != 0) { // 홀수번째일 경우 3 곱해서 sum에 더하기
                int num = Integer.parseInt(nums.get(i));
                sum = sum + (num * 3);
            } else { // 짝수번째일 경우 sum에 그대로 더하기
                int num = Integer.parseInt(nums.get(i));
                sum += num;
            }
        }

        for (int i = 0; i < 10; i++) {
            if ((sum + (i * weight)) % 10 == 0){
                System.out.println(i);
            }
        }
    }
}