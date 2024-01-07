import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        boolean[] isValid = new boolean[101];
        int count = 0;

        for (int i = 0; i < n; i++) {
            int idx = Integer.parseInt(st.nextToken());
            if (!isValid[idx]) isValid[idx] = true;
            else count++;
        }

        System.out.println(count);


    }

}
