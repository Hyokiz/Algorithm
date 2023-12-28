import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        BigInteger cluster = new BigInteger(br.readLine());

        long times = 0;
        for (int i = 0; i < N; i++) {
            BigInteger size = new BigInteger(st.nextToken());
            if (size.remainder(cluster).intValue() == 0) {
                times += size.divide(cluster).intValue();
            } else {
                times += size.divide(cluster).intValue() + 1;
            }
        }

        System.out.println(cluster.multiply(BigInteger.valueOf(times)));

    }

}
