import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String X = st.nextToken(), Y = st.nextToken();

        StringBuilder sb1 = new StringBuilder(X);
        StringBuilder sb2 = new StringBuilder(Y);

        String revX = sb1.reverse().toString();
        String revY = sb2.reverse().toString();

        String tmp = String.valueOf(Integer.parseInt(revX) + Integer.parseInt(revY));

        StringBuilder answer = new StringBuilder(tmp).reverse();

        System.out.println(Integer.valueOf(answer.toString()));

    }

}
