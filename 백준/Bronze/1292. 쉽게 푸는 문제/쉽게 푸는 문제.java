import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int A = Integer.parseInt(st.nextToken()), B = Integer.parseInt(st.nextToken());

        ArrayList<Integer> arr = new ArrayList<>();
        int count = 1;
        for (int i = 1; i < 50; i++) {
            for (int j = 0; j < i; j++) {
                arr.add(count);
            }
            count++;
        }

        int sum = 0;
        for (int i = A - 1; i < B; i++) {
            sum += arr.get(i);
        }

        System.out.println(sum);

    }

}
