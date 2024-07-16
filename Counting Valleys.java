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
     * Complete the 'countingValleys' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER steps
     *  2. STRING path
     */

    public static int countingValleys(int steps, String path) {
    // Write your code here
        int altitude = 0;
        int valleys = 0;
        boolean inValley = false;

        for (int i = 0; i < steps; i++) {
            char step = path.charAt(i);
            
            if (step == 'U') {
                altitude++;
            } else if (step == 'D') {
                altitude--;
            }
            
            // Check if we just entered a valley
            if (altitude < 0 && !inValley) {
                inValley = true;
            }
            
            // Check if we just exited a valley
            if (altitude == 0 && inValley) {
                valleys++;
                inValley = false;
            }
        }

        return valleys;

   }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int steps = Integer.parseInt(bufferedReader.readLine().trim());

        String path = bufferedReader.readLine();

        int result = Result.countingValleys(steps, path);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedReader.close();
        bufferedWriter.close();
    }
}
