import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        char[][] castle = new char[n][m];
        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            char[] c = s.toCharArray();
            for (int j = 0; j < m; j++) {
                castle[i][j] = c[j];
            }
        }

        int row = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (castle[i][j] == 'X') break;

                if (j == (m - 1)) row++;
            }
        }

        int col = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (castle[j][i] == 'X') break;

                if (j == (n - 1)) col++;
            }
        }

        System.out.println(Math.max(row, col));
    }

}
