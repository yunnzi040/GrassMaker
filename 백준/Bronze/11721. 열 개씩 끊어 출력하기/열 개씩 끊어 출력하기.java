import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);

            // 문자열이 알파벳 하나씩 배열에 입력되어 있겠지.
            String input = sc.nextLine();
            String[] words = input.split("");

            int count = words.length;
            int index = 0;

            while ( count > 0 ){
                if (count / 10 > 0) {
                    System.out.println(input.substring(index, index + 10));
                    index += 10;
                    count -= 10;
                    }
                else {
                    System.out.println(input.substring(index));
                    break;
                }
            }
        }
    }
