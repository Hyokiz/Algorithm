import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), L = Integer.parseInt(st.nextToken()), D = Integer.parseInt(st.nextToken());
        boolean[] time = new boolean[(N * L) + 5 * (N - 1)];
        for (int i = 0; i < N; i++) {
            int s = (L + 5) * i;
            for (int j = s; j < s + L; j++) {
                time[j] = true;
            }
        }

        int answer = 0;
        while (answer < time.length) {
            if (!time[answer]) break;
            answer += D;
        }

        System.out.println(answer);


    }

}
