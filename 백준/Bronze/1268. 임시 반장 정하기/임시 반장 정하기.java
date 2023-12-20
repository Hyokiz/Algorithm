import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] group = new int[n][5];
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 5; j++) {
                group[i][j] = Integer.parseInt(st.nextToken());
            }

        }

        int max = 0;
        int idx = 0;

        for (int i = 0; i < n; i++) {
            Set<Integer> set = new HashSet<>();
            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < n; k++) {
                    if (i == k) continue;
                    if (group[i][j] == group[k][j]) {
                        set.add(k);
                    }
                }
            }
            if (max < set.size()) {
                max = set.size();
                idx = i + 1;
            }

        }

        if (idx == 0) System.out.println(1);
        else System.out.println(idx);

    }

}
