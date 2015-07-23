package com.example.syntax;

import java.util.Arrays;
import java.util.concurrent.ThreadLocalRandom;

/**
 * Created by benbendaisy on 7/8/15.
 */
public class ParallelArrays {
    public static void main(String[] args) {
        long[] arry = new long[2000];
        Arrays.parallelSetAll(arry, indx -> ThreadLocalRandom.current().nextInt(1000000));
        Arrays.stream(arry).limit(10).forEach(i -> System.out.println(i + " "));
        System.out.println("--------------------------");
        Arrays.parallelSort(arry);
        Arrays.stream(arry).limit(10).forEach(i -> System.out.println(i + " "));
    }
}
