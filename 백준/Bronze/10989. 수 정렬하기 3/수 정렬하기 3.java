import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] count = new int[10001]; // 입력값의 범위 (1 ~ 10000)

        for (int i = 0; i < N; i++) {
            int num = Integer.parseInt(br.readLine());
            count[num]++;
        }

        for (int i = 0; i <= 10000; i++){
            while (count[i]-- > 0){
                sb.append(i).append("\n");
            }
        }
        System.out.println(sb);
    }
}