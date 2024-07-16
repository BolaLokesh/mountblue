import java.io.*;
import java.util.*;

class Result {

    /*
     * Complete the 'happyLadybugs' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts STRING b as parameter.
     */

    public static String happyLadybugs(String b) {
        int n = b.length();
        int[] charCount = new int[26]; // Count occurrences of each letter
        boolean hasEmpty = false;

        // Count occurrences of each character
        for (char ch : b.toCharArray()) {
            if (ch != '_') {
                charCount[ch - 'A']++;
            } else {
                hasEmpty = true;
            }
        }

        // Check if all ladybugs are already happy
        boolean allHappy = true;
        for (int i = 0; i < n; i++) {
            if (b.charAt(i) != '_' && (i == 0 || b.charAt(i) != b.charAt(i - 1)) &&
                (i == n - 1 || b.charAt(i) != b.charAt(i + 1))) {
                allHappy = false;
                break;
            }
        }

        // If all ladybugs are already happy, return "YES"
        if (allHappy) {
            return "YES";
        }

        // If there is any ladybug without a pair and no empty cells, return "NO"
        for (int count : charCount) {
            if (count == 1) {
                return "NO";
            }
        }

        // If there is at least one empty cell '_', return "YES" (can rearrange ladybugs)
        if (hasEmpty) {
            return "YES";
        }

        // If all ladybugs have pairs and no empty cells, return "NO" (no possible rearrangement)
        return "NO";
    }
}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));

        int g = Integer.parseInt(bufferedReader.readLine().trim());

        for (int gItr = 0; gItr < g; gItr++) {
            int n = Integer.parseInt(bufferedReader.readLine().trim());

            String b = bufferedReader.readLine();

            String result = Result.happyLadybugs(b);

            bufferedWriter.write(result);
            bufferedWriter.newLine();
        }

        bufferedReader.close();
        bufferedWriter.close();
    }
}

