import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String s = br.readLine();
            if (s.equals("0")) break;

            int sum = 1;
            for (char c: s.toCharArray()) {
                if (c == '1') sum += 2;
                else if (c == '0') sum += 4;
                else sum += 3;

                sum++;
            }

            System.out.println(sum);

        }

    }

}
