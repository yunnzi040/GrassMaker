import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int[] numbers = new int[8];

        boolean ascending = false;   // 오름차순 가능성
        boolean descending = false;  // 내림차순 가능성
        boolean mixed = false; // 혼합 가능성


        // 숫자 8개 무작위로 입력 받기
        for (int i = 0; i < 8; i++){
            numbers[i] = sc.nextInt();
        }

        for (int i = 0; i < numbers.length-1; i++){
           int differ = numbers[i] - numbers[i+1];
           int abs = Math.abs(differ);

           if (abs != 1){
               mixed = true;
               break;
           } else {
               if (differ < 0){
                   ascending = true;
               } else {
                   descending = true;
               }
           }
        }

        if (mixed){
            System.out.println("mixed");
        } else if (ascending){
            System.out.println("ascending");
        } else if (descending){
            System.out.println("descending");

        }
    }
}