import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        String words = sc.nextLine();
        List<String> inputList = Arrays.asList(words.split(""));
        String alphabet = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z";
        List<String> wordList = Arrays.asList(alphabet.split(","));

        // 알파벳 갯수만큼 결과가 나와야 한다.
        for (int i = 0; i < wordList.size(); i++) {
            String word = wordList.get(i); // 몇번째 알파벳 가져오기 ex. a

            // 입력한 단어가 해당 알파벳을 가지고 있을 경우
            if (inputList.contains(word)) {
                System.out.println(inputList.indexOf(word));
            }else {
                System.out.println(-1);
            }
        }
    }
}