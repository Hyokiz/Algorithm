import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int answer = 0;
        for (int i = 4; i < n+1; i++) {
            char[] ch = String.valueOf(i).toCharArray();
            boolean flag = false;

            for (char c: ch) {
                if (c == '4' || c == '7') {
                    continue;
                } else {
                    flag = true;
                }
                
                if (flag) {
                    break;
                }
            }

            if (!flag) {
                answer = i;
            }

        }

        System.out.println(answer);

    }

}
