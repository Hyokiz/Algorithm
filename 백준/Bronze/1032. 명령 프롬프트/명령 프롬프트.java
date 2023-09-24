import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        String answer = "";
        char[] arr = br.readLine().toCharArray();
        for (int t=0; t<T-1; t++) {
            String str = br.readLine();
            char[] temp = str.toCharArray();
            for (int i=0; i<str.length(); i++) {
                if (arr[i] != temp[i]) {
                    arr[i] = '?';
                }
            }

        }
        answer = String.valueOf(arr);
        System.out.println(answer);

    }

}
