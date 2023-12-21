import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] alphabet = new int[26];
        for (int i = 0; i < N; i++) {
            String name = br.readLine();
            char fst = name.charAt(0);
            alphabet[fst - 97]++;
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < alphabet.length; i++) {
            if (alphabet[i] >= 5) {
                sb.append((char) (i + 97));
            }
        }

        if (sb.length() == 0) {
            System.out.println("PREDAJA");
        } else {
            System.out.println(sb);
        }

    }

}
