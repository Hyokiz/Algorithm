import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] calls = new int[N];
        for (int i = 0; i < N; i++) {
            calls[i] = Integer.parseInt(st.nextToken());
        }
        double Y = 0;
        double M = 0;
        for (int call: calls) {
            Y += 10 * (call / 30 + 1);
            M += 15 * (call / 60 + 1);
        }

        if (Y == M) {
            System.out.println("Y M " + (int)Y);
        } else if (Y < M) {
            System.out.println("Y " + (int)Y);
        } else {
            System.out.println("M " + (int)M);
        }

    }

}
