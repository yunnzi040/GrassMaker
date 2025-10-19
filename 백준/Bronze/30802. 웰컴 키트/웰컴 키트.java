import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt(); // 참가자의 수
        List<Integer> Tshirts = new ArrayList<>(); // 사이즈별 신청자의 수

        for (int i = 0; i<6; i++){
            Tshirts.add(sc.nextInt());
        }
        int T = sc.nextInt(); // 티셔츠의 묶음 수
        int P = sc.nextInt(); // 펜의 묶음 수

        int Tbundle = 0;
        int Pbundle = 0;

        for (int i = 0; i < Tshirts.size(); i++){
            Tbundle += Tshirts.get(i)/T;

            if (Tshirts.get(i) % T > 0){
                Tbundle ++;
            }
            Pbundle += Tshirts.get(i);
        }

        System.out.println(Tbundle);
        System.out.println((Pbundle/P) + " " + (Pbundle%P));
    }
}