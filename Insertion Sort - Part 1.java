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
     * Complete the 'insertionSort1' function below.
     *
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY arr
     */

    public static void insertionSort1(int n, List<Integer> arr) {
    
        int valueToInsert = arr.get(n - 1);  // The element to be inserted
        int i = n - 2;  // Start comparing from the second last element

        // Loop to find the correct position for the valueToInsert
        while (i >= 0 && arr.get(i) > valueToInsert) {
            arr.set(i + 1, arr.get(i));  // Shift the element to the right
            printList(arr);  // Print the list after each shift
            i--;
        }
        arr.set(i + 1, valueToInsert);  // Insert the element at its correct position
        printList(arr);  // Print the final state of the list
    }
    
    // Helper function to print the list
    public static void printList(List<Integer> arr) {
        System.out.println(arr.stream()
                              .map(String::valueOf)
                              .collect(Collectors.joining(" ")));
    }

    
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<Integer> arr = Stream.of(bufferedReader.readLine().replaceAll("\\s+$", "").split(" "))
            .map(Integer::parseInt)
            .collect(toList());

        Result.insertionSort1(n, arr);

        bufferedReader.close();
    }
}
