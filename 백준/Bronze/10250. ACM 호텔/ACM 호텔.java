import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        // 엘리베이터에서 걷는 거리가 가장 짧은 순서대로 방을 배정하기
        Scanner sc = new Scanner(System.in);

        // 테스트 데이터 갯수
        int T = sc.nextInt();

        // 방 배졍 갯수
        int count = 0;

        for (int o = 0; o < T; o++) {
            // 테스트 데이터 한 행으로 입력
            int H = sc.nextInt(); // 호텔의 층수
            int W = sc.nextInt(); // 각 층의 방 수
            int N = sc.nextInt(); // 몇 번째 손님

            // 층의 방 갯수 (1)
            for (int i = 1; i <= W; i++){
                // 층의 갯수 (1 ~ 6)
                for (int j = 1; j <= H; j++){
                    count++;
                    if (count == N){
                        if (i < 10) {
                            System.out.println(Integer.toString(j) + "0" + Integer.toString(i));
                        } else {
                            System.out.println(Integer.toString(j) + Integer.toString(i));
                        }
                    }
                }
            }
            count = 0;
        }
    }
}