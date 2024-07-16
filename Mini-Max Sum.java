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
     * Complete the 'miniMaxSum' function below.
     *
      The function accepts INTEGER_ARRAY arr as parameter.
    */

    public static void miniMaxSum(List<Integer> arr) {
    // Write your code hwre
      // sorting array
        Collections.sort(arr);
        long minSum = 0;
        for (int i = 0; i < 4; i++) {
            minSum += arr.get(i);
        }
        
        // Step 3: Calculate the maximum sum (sum of the last four elements)
        long maxSum = 0;
        for (int i = 1; i <= 4; i++) {
            maxSum += arr.get(arr.size() - i);
        }
        
        // Step 4: Print the results
        System.out.println(minSum + " " + maxSum);
    }

}

public class Solution {
    public static void main(String[] args) {
      Scanner scanner = new Scanner(System.in);
        
        // Read input
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            arr.add(scanner.nextInt());
        }
        
        // Call the miniMaxSum function
        Result.miniMaxSum(arr);
        
        // Close the scanner
        scanner.close();
    }
}
