import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String A = st.nextToken(), B = st.nextToken();
        long answer = 0;
        for (int i = 0; i < A.length(); i++) {
            for (int j = 0; j < B.length(); j++) {
                answer += (A.charAt(i) - '0') * (B.charAt(j) - '0');
            }
        }

        System.out.println(answer);

    }

}
