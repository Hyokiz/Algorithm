import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String n = br.readLine();
        for (int i = 0; i < n.length(); i++) {
            int c = n.charAt(i) - '0';      // int 형으로 변환 시 ASKII 코드로 변환되기 때문에 '0'을 빼주어야 한다.
            if (c >= 4) {       // 4보다 클 경우 1XX
                sb.append(1);
                c -= 4;
            } else {
                sb.append(0);   // 4보다 작을 경우 0XX
            }

            if (c >= 2) {       // 2보다 클 경우 X1X
                sb.append(1);
                c -= 2;
            } else {
                sb.append(0);   // 2보다 작을 경우 X0X
            }

            if (c >= 1) {       // 1보다 클 경우 XX1
                sb.append(1);
            } else {
                sb.append(0);   // 1보다 작을 경우 XX0
            }
        }

        if (sb.charAt(0) == '0') {      // 0으로 시작할경우 자르기
            if (sb.charAt(1) == '0') {
                System.out.println(sb.substring(2));
            } else {
                System.out.println(sb.substring(1));
            }
        } else {
            System.out.println(sb);
        }

        br.close();

    }

}
