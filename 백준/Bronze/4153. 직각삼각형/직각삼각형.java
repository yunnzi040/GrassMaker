import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        boolean input = true;
        int[] arr = new int[3];

        while (input){
            for (int i=0; i<3; i++){
                arr[i] = sc.nextInt();
            }

            // 각 입력이 모두 0일 경우
            if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0){
                break;
            }

            // 값을 오름차순 정렬
            Arrays.sort(arr);
            if (arr[2] * arr[2] == arr[1] * arr[1] + arr[0] * arr[0]){
                System.out.println("right");
            } else {
                System.out.println("wrong");
            }
        }
    }
}