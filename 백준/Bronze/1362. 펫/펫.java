import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사
        int num = 1;

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int O = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());

            if (O == 0 && W == 0) break;
            int count = 0;

            while (true) {
                st = new StringTokenizer(br.readLine());
                String EF = st.nextToken();
                int n = Integer.parseInt(st.nextToken());

                if (EF.equals("#") && n == 0) break;

                if (EF.equals("E")) W -= n;
                if (EF.equals("F")) W += n;

                if (W <= 0) {
                    count = 1;
                }
            }

            if (count == 1) {
                System.out.println(num + " RIP");
            } else {
                if ((O / 2) < W && W < (O * 2)) {
                    System.out.println(num + " :-)");
                } else {
                    System.out.println(num + " :-(");
                }
            }

            num++;

        }

    }

}
