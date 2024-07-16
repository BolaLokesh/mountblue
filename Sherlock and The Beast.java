import java.io.*;
import java.util.*;

class Result {

    public static void decentNumber(int n) {
        // We need to find the largest number with n digits which is a decent number
        // x -> number of '5's, y -> number of '3's
        
        // Check for all possible values of x starting from n down to 0
        for (int x = n; x >= 0; x--) {
            int y = n - x;
            if (y % 5 == 0 && x % 3 == 0) {
                // Found a valid x and y
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < x; i++) {
                    sb.append('5');
                }
                for (int i = 0; i < y; i++) {
                    sb.append('3');
                }
                System.out.println(sb.toString());
                return;
            }
        }
        // If no valid decent number found
        System.out.println("-1");
    }

}

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(bufferedReader.readLine().trim());

        for (int tItr = 0; tItr < t; tItr++) {
            int n = Integer.parseInt(bufferedReader.readLine().trim());

            Result.decentNumber(n);
        }

        bufferedReader.close();
    }
}


