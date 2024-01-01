import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); //scanner 와 유사
        BigInteger bin = new BigInteger(br.readLine(), 2);
        System.out.println(bin.toString(8));

    }

}
