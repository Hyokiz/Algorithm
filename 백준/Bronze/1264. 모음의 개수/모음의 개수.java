import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        char[] vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};

        Scanner sc = new Scanner(System.in);
        while (true) {
            int answer = 0;
            String s = sc.nextLine();
            if (s.equals("#")) {
                break;
            }

            for (char x: s.toCharArray()) {
                for (int i=0; i<10; i++) {
                    if (x == vowels[i]) {
                        answer++;
                    }
                }
            }
            System.out.println(answer);
        }

    }

}
