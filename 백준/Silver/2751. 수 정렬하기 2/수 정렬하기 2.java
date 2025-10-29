import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] count = new int[2000001]; // 입력값의 범위 (1 ~ 10000)

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            int index = num + 1000000;
            count[index]++;
        }

        for (int i = 0; i <= 2000000; i++){
            while (count[i]-- > 0){
                sb.append(i - 1000000).append("\n");
            }
        }
        System.out.println(sb);
    }
}