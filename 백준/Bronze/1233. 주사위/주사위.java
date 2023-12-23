import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int S1 = Integer.parseInt(st.nextToken()), S2 = Integer.parseInt(st.nextToken()), S3 = Integer.parseInt(st.nextToken());

        int[] numbers = new int[81];

        for (int i = 1; i < S1 + 1; i++) {
            for (int j = 1; j < S2 + 1; j++) {
                for (int k = 1; k < S3 + 1; k++) {
                    numbers[i+j+k]++;
                }
            }
        }

        int max = 0, idx = 0;
        for (int i = 0; i < numbers.length; i++) {
            if (max < numbers[i]) {
                max = numbers[i];
                idx = i;
            }
        }

        System.out.println(idx);

    }

}
