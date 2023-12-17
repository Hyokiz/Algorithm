import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String b1 = st.nextToken();
        String b2 = st.nextToken();

        BigInteger decimal1 = new BigInteger(b1, 2);
        BigInteger decimal2 = new BigInteger(b2, 2);

        BigInteger sum = decimal1.add(decimal2);

        String answer = sum.toString(2);

        System.out.println(answer);

    }

}
