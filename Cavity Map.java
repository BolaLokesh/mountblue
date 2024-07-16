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
     * Complete the 'cavityMap' function below.
     *
     * The function is expected to return a STRING_ARRAY.
     * The function accepts STRING_ARRAY grid as parameter.
     */

    public static List<String> cavityMap(List<String> grid) {
    // Write your code here
        int n = grid.size();
        List<String> result = new ArrayList<>(grid);
        
        // Convert list of strings to array of char arrays for easy manipulation
        char[][] matrix = new char[n][];
        for (int i = 0; i < n; i++) {
            matrix[i] = grid.get(i).toCharArray();
        }
        
        // Iterate through the matrix to find cavities
        for (int i = 1; i < n - 1; i++) {
            for (int j = 1; j < matrix[i].length - 1; j++) {
                char current = matrix[i][j];
                // Check if current cell is a cavity
                if (current > matrix[i - 1][j] &&
                    current > matrix[i + 1][j] &&
                    current > matrix[i][j - 1] &&
                    current > matrix[i][j + 1]) {
                    // Mark as cavity by replacing with 'X'
                    matrix[i][j] = 'X';
                }
            }
        }
        
        // Convert back to list of strings
        for (int i = 0; i < n; i++) {
            result.set(i, new String(matrix[i]));
        }
        return result;

    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int n = Integer.parseInt(bufferedReader.readLine().trim());

        List<String> grid = IntStream.range(0, n).mapToObj(i -> {
            try {
                return bufferedReader.readLine();
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        })
            .collect(toList());

        List<String> result = Result.cavityMap(grid);

        bufferedWriter.write(
            result.stream()
                .collect(joining("\n"))
            + "\n"
        );

        bufferedReader.close();
        bufferedWriter.close();
    }
}