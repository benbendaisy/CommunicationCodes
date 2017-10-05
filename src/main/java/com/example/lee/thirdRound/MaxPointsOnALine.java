package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

public class MaxPointsOnALine {
    private static class Point {
      int x;
      int y;
      Point() { x = 0; y = 0; }
      Point(int a, int b) { x = a; y = b; }
    }

    /**
     * both this method and I are O(n^2) solution but this method passed leetcode
     * as the key of cached rate is double in I that may have prcision issue
     * @param points
     * @return
     */
    public int maxPoints(Point[] points) {
        if (points == null || points.length == 0) {
            return 0;
        }
        int max = 0;
        for (int i = 0; i < points.length; i++) {
            int same = 1;
            int vertical = 0;
            int localMax = 0;
            Map<String, Integer> cachedRate = new HashMap<>();
            for (int j = 0; j < points.length; j++) {
                if (i == j) {
                    continue;
                }
                if (points[i].x == points[j].x) {
                    if (points[i].y == points[j].y) {
                        same++;
                    } else {
                        vertical++;
                    }
                } else {
                    String key = getKey(points[i], points[j]);
                    int cnt = cachedRate.getOrDefault(key, 0) + 1;
                    cachedRate.put(key, cnt);
                    localMax = Math.max(localMax, cnt);
                }
            }
            localMax = Math.max(localMax, vertical) + same;
            max = Math.max(max, localMax);
        }
        return max;
    }

    private String getKey(Point p1, Point p2) {
        int dy = p1.y - p2.y;
        int dx = p1.x - p2.x;
        int common = gcd(dy, dx);
        return dy * 1.0 / common + ":" + dx * 1.0 / common;
    }

    private int gcd(int a, int b) {
        return b == 0 ? a : gcd(b, a % b);
    }

    /**
     * Failed on case: [[0,0],[94911151,94911150],[94911152,94911151]] because of precision problem
     * @param points
     * @return
     */
    public int maxPointsI(Point[] points) {
        if (points == null || points.length == 0) {
            return 0;
        }

        int max = 0;
        for (int i = 0; i < points.length; i++) {
            int same = 1;
            int vertical = 0;
            int localMax = 0;
            Map<Double, Integer> cacheRate = new HashMap<>();
            for (int j = 0; j < points.length; j++) {
                if (i == j) {
                    continue;
                }
                if (points[i].x == points[j].x) {
                    if (points[i].y == points[j].y) {
                        same++;
                    } else {
                        vertical++;
                    }
                } else {
                    double rate = getRate(points[i], points[j]);
                    int cnt = cacheRate.getOrDefault(rate, 0) + 1;
                    localMax = Math.max(localMax, cnt);
                    cacheRate.put(rate, cnt);
                }
            }
            localMax = Math.max(same + localMax, same + vertical);
            max = Math.max(max, localMax);
        }
        return max;
    }

    private double getRate(Point point1, Point point2) {
        return (point2.y - point1.y) * 1.0 / (point2.x - point1.x);
    }

    public static void main(String[] args) {
        MaxPointsOnALine maxPointsOnALine = new MaxPointsOnALine();
        Point[] points = new Point[3];
        points[0] = new Point(0, 0);
        points[1] = new Point(94911151, 94911150);
        points[2] = new Point(94911152, 94911151);
        System.out.println(maxPointsOnALine.maxPoints(points));
    }
}
