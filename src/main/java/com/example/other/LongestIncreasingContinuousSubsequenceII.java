package com.example.other;

/**
 * Created by benbendaisy on 5/27/15.
 */
public class LongestIncreasingContinuousSubsequenceII {
    int max = 0;
    public int longestIncreasingContinuousSubsequenceII(int[][] A) {
        if (A == null || A.length < 1) return max;
        int row = A.length;
        int col = A[0].length;
        int[][] dp = new int[A.length][A[0].length];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (dp[i][j] == 0) longestIncreasingContinuousSubsequenceII(A, dp, i, j);
            }
        }
        return dp[row - 1][col - 1];
    }

    private int longestIncreasingContinuousSubsequenceII(int[][] A, int[][] dp, int i, int j) {
        int row = A.length;
        int col = A[0].length;
        if (i < 0 || i >= row || j < 0 || j >= col) return 0;
        if (dp[i][j] > 0) return dp[i][j];
        int len1 = 0, len2 = 0;
        if (i > 0 && A[i - 1][j] > A[i][j]) len1 = longestIncreasingContinuousSubsequenceII(A, dp, i - 1, j);
        if (i < row - 1 && A[i + 1][j] > A[i][j]) {
            len2 = longestIncreasingContinuousSubsequenceII(A, dp, i + 1, j);
            len1 = Math.max(len1, len2);
        }
        if (j > 0 && A[i][j - 1] > A[i][j]) {
            len2 = longestIncreasingContinuousSubsequenceII(A, dp, i, j - 1);
            len1 = Math.max(len1, len2);
        }
        if (j < col - 1 && A[i][j + 1] > A[i][j]) {
            len2 = longestIncreasingContinuousSubsequenceII(A, dp, i, j + 1);
            len1 = Math.max(len1, len2);
        }
        len1++;
        max = Math.max(len1, max);
        dp[i][j] = len1;
        return len1;
    }

    public static void main(String[] args) {
        LongestIncreasingContinuousSubsequenceII longestIncreasingContinuousSubsequenceII = new LongestIncreasingContinuousSubsequenceII();

    }
}
