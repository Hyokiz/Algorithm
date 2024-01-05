import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()), m = Integer.parseInt(st.nextToken());
        int[] box = new int[n];
        int[] book = new int[m];
        int sum = 0;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            box[i] = Integer.parseInt(st.nextToken());
            sum += box[i];
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            book[i] = Integer.parseInt(st.nextToken());
            sum -= book[i];
        }

        System.out.println(sum);


    }

}
