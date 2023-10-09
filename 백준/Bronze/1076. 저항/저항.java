import java.io.*;
import java.math.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception{
        ArrayList<String> arrayList = new ArrayList<>();
        arrayList.add("black");
        arrayList.add("brown");
        arrayList.add("red");
        arrayList.add("orange");
        arrayList.add("yellow");
        arrayList.add("green");
        arrayList.add("blue");
        arrayList.add("violet");
        arrayList.add("grey");
        arrayList.add("white");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String fst = br.readLine();
        String scd = br.readLine();
        String thd = br.readLine();
        StringBuilder sb = new StringBuilder();
        sb.append(arrayList.indexOf(fst));
        sb.append(arrayList.indexOf(scd));
        Long result = (long) (Integer.parseInt(String.valueOf(sb)) * Math.pow(10, arrayList.indexOf(thd)));
        System.out.println(result);

    }

}
