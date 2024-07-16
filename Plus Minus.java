import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'plusMinus' function below.
     *
     * The function accepts INTEGER_ARRAY arr as parameter.
     */

    public static void plusMinus(List<Integer> arr) {
        int n = arr.size();
        int posCount = 0, negCount = 0, zeroCount = 0;
        
        for(int num : arr) {
            if(num > 0) {
                posCount++;
            }else if (num < 0) {
                negCount++;
            }else {
                zeroCount++;
            }
        }
        // calculating the fractions
        double posFrac = (double) posCount / n;
        double negFrac = (double) negCount / n;
        double zeroFrac = (double) zeroCount / n;
       
        System.out.printf("%.6f%n",posFrac);
        System.out.printf("%.6f%n",negFrac);
        System.out.printf("%.6f%n",zeroFrac);
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.plusMinus(arr);

        bufferedReader.close();
    }
}
