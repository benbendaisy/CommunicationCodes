package com.example.probility;

import java.util.*;

/**
 * Created by pzhong on 1/13/16.
 */
public class WeightedRandom {
    private static final Random _random = new Random();
    public static <E> E getWeightedRandom(Map<E, Double> weights, Random random) {
        E result = null;
        double bestValue = Double.MAX_VALUE;
        for (E element : weights.keySet()) {
            double value = -Math.log(random.nextDouble()) / weights.get(element);
            if (value < bestValue) {
                bestValue = value;
                result = element;
            }
        }
        return result;
    }

    public static <E> E getWeightedRandomI(Map<E, Double> weights, Random random) {
        E result = null;
        double weighted = 0.0;
        for (E e : weights.keySet()) {
            weighted += weights.get(e);
        }
        double r = random.nextDouble() * weighted;
        for (E e : weights.keySet()) {
            r -= weights.get(e);
            if (r <= 0) {
                result = e;
                break;
            }
        }
        return result;
    }

    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        Map<Integer, Double> weightMap = new HashMap<>();
        for (int i = 1; i <= 59; i++) {
            weightMap.put(i, 1.0);
        }
        Set<Integer> weightedSet = new HashSet<>(Arrays.asList(26, 41, 16, 22, 42, 35, 39, 45, 15, 32, 40, 10, 9, 13, 28, 20, 8));
        weightedSet.forEach(
                number -> {
                    weightMap.put(number, 1.5);
                }
        );
        Set<Integer> whiteBalls = new HashSet<>();
        while (whiteBalls.size() < 5) {
            whiteBalls.add(getWeightedRandom(weightMap, _random));
        }
        List<String> stringList = new ArrayList<>();
        whiteBalls.forEach(
                number -> {
                    stringList.add(number.toString());
                }
        );
        System.out.println("white balls: " + String.join(",", stringList));
        Map<Integer, Double> weightedMap = new HashMap<>();
        for (int i = 1; i <= 26; i++) {
            weightedMap.put(i, 1.0);
        }
        weightedSet = new HashSet<>(Arrays.asList(20, 6, 2, 18, 9, 1, 11, 26, 10, 12, 17, 23, 24, 15));
        weightedSet.forEach(
                number -> {
                    weightedMap.put(number, 1.5);
                }
        );
        System.out.println("red ball: " + getWeightedRandom(weightedMap, _random));
        long endTime = System.currentTimeMillis();
        System.out.println("runnint time: " + (endTime - startTime));
    }
}
