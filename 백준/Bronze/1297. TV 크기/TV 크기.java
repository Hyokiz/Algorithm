import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        double D = Double.parseDouble(st.nextToken()), H = Double.parseDouble(st.nextToken()), W = Double.parseDouble(st.nextToken());

        double pow = Math.pow(D, 2) / (Math.pow(H, 2) + Math.pow(W, 2));
        double sqrt = Math.sqrt(pow);   // * sqrt 를 해주면 원래 값

        System.out.println((int) (sqrt * H) + " " + (int) (sqrt * W));

    }

}
