import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (a % 10 == 0) {
                sb.append(10 + "\n");
                continue;
            }
            int num = a % 10;
            for (int j=1; j<b; j++) {
                num = (num * a) % 10;
            }
            sb.append(num + "\n");
        }
        bw.write(String.valueOf(sb));
        bw.flush();
        bw.close();
    }

}
