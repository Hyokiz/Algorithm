import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int m = Integer.parseInt(br.readLine());
        String ball = "1";

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String a = st.nextToken(), b = st.nextToken();
            if (a.equals(ball)) {
                ball = b;
            } else if (b.equals(ball)) {
                ball = a;
            } else {
                continue;
            }
        }

        System.out.println(ball);

    }

}
