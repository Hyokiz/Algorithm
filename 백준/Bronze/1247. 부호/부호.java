import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 3; i++) {
            int n = Integer.parseInt(br.readLine());
            BigInteger sum = new BigInteger("0");
            for (int j = 0; j < n; j++) {
                BigInteger tmp = new BigInteger(br.readLine());
                sum = sum.add(tmp);
            }

            if (sum.compareTo(BigInteger.ZERO) == -1) System.out.println("-");
            else if (sum.compareTo(BigInteger.ZERO) == 1) System.out.println("+");
            else System.out.println(0);

        }

    }

}
