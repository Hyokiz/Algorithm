import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        char[] arr = br.readLine().toCharArray();
        String answer = "NO";
        for (int i = 0; i < arr.length - 1; i++) {
            long i1 = 1, i2 = 1;
            for (int j = 0; j <= i; j++) {
                i1 *= Integer.valueOf(arr[j] - '0');
            }
            for (int j = i+1; j < arr.length; j++) {
                i2 *= Integer.valueOf(arr[j] - '0');
            }

            if (i1 == i2) {
                answer = "YES";
                break;
            }

        }

        System.out.println(answer);

    }

}
