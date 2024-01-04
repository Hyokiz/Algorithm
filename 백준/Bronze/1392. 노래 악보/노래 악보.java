import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken()), Q = Integer.parseInt(st.nextToken());
        ArrayList<Integer> arr = new ArrayList<>();
        int music = 1;
        for (int i = 0; i < N; i++) {
            int count = Integer.parseInt(br.readLine());
            for (int j = 0; j < count; j++) {
                arr.add(music);
            }
            music++;
        }

        for (int i = 0; i < Q; i++) {
            int index = Integer.parseInt(br.readLine());
            System.out.println(arr.get(index));
        }

    }

}
