package com.example.lee.thirdRound;

import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by benbendaisy on 7/10/17.
 */
public class PermutationSequence {
    public String getPermutation(int n, int k) {
        if (n < 1) {
            return "";
        }
        k--;
        List<Integer> list = IntStream.range(1, n + 1).boxed().collect(Collectors.toList());
        int[] factorial = new int[n];
        factorial[0] = 1;
        for (int i = 1; i < n; i++) {
            factorial[i] = factorial[i - 1] * i;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = n; i >= 1; i--) {
            int j = k / factorial[i - 1];
            k = k % factorial[i - 1];
            sb.append(list.get(j));
            list.remove(j);
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        PermutationSequence permutationSequence = new PermutationSequence();
        System.out.println(permutationSequence.getPermutation(4, 9));
    }
}
