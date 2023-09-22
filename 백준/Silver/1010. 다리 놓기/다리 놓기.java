import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int tc=0; tc<T; tc++) {
            BigInteger answer = new BigInteger("1");
            int n = sc.nextInt(), m = sc.nextInt();
            int max = Math.max(n, m), min = Math.min(n, m);
            for (int i=1; i<max+1; i++) {
                BigInteger temp = new BigInteger(String.valueOf(i));
                answer = answer.multiply(temp);
            }
            for (int j=1; j<min+1; j++) {
                BigInteger temp = new BigInteger(String.valueOf(j));
                answer = answer.divide(temp);
            }
            for (int k=1; k<(max - min + 1); k++) {
                BigInteger temp = new BigInteger(String.valueOf(k));
                answer = answer.divide(temp);
            }
            System.out.println(answer);
        }
    }

}
