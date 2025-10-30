import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            int K = Integer.parseInt(br.readLine()); // 층수
            int N = Integer.parseInt(br.readLine()); // 호수

            // 입력받은 K와 N으로 2차원 배열을 만들기
            int[][] arr = new int[K+1][N+1];

            // 0층 값 넣어주기
            for (int j = 1; j <= N; j++){
                arr[0][j] = j; // 0층 j호에 j명
            }
            
            for (int k = 1; k <= K; k++){
                for (int n = 1; n <= N; n++){
                    arr[k][n] = arr[k - 1][n] + arr[k][n - 1];
                }
            }
            System.out.println(arr[K][N]);
        }
    }
}