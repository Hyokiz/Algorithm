import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st1 = new StringTokenizer(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st1.nextToken()), K = Integer.parseInt(st1.nextToken());
        int[] arr = new int[K];
        int grade;
        for (int i = 0; i < K; i++) {
            int rank = Integer.parseInt(st2.nextToken()) * 100 / N;
            if (0 <= rank && rank <= 4) grade = 1;
            else if (4 < rank && rank <= 11) grade = 2;
            else if (11 < rank && rank <= 23) grade = 3;
            else if (23 < rank && rank <= 40) grade = 4;
            else if (40 < rank && rank <= 60) grade = 5;
            else if (60 < rank && rank <= 77) grade = 6;
            else if (77 < rank && rank <= 89) grade = 7;
            else if (89 < rank && rank <= 96) grade = 8;
            else grade = 9;
            arr[i] = grade;
        }
        for (int x: arr) {
            System.out.print(x + " ");
        }

    }

}
