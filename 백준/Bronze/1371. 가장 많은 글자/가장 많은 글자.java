import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사

        int[] alpha = new int[26]; //알파벳 개수 배열
        int max = 0;
        String input; //EOF 처리를 위해 받을 문자열;;
        String str = "";

        while ((input = br.readLine()) != null) {
            str += input;
        }

        //알파벳 갯수 저장 및 가장 많이 나온 알파벳의 횟수 저장
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) != ' ') {
                alpha[str.charAt(i) - 'a']++;

                if (alpha[str.charAt(i) - 'a'] > max) {
                    max = alpha[str.charAt(i) - 'a'];
                }
            }
        }

        for (int i = 0; i < 26; i++) {
            if (max == alpha[i]) {
                System.out.print((char) (i + 'a'));
            }
        }

    }

}
