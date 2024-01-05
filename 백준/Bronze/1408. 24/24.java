import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사
        int now = 0;
        int start = 0;

        StringTokenizer st = new StringTokenizer(br.readLine(), ":");
        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int s = Integer.parseInt(st.nextToken());

        now = (h * 3600) + (m * 60) + s;

        st = new StringTokenizer(br.readLine(), ":");
        h = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        s = Integer.parseInt(st.nextToken());

        start = (h * 3600) + (m * 60) + s;

        int answer = 0;

        if (start > now) answer = start - now;
        else answer = (24 * 3600) - (now - start);

        System.out.format("%02d:%02d:%02d", (answer / 3600), ((answer / 60) % 60), (answer % 60));

    }

}
