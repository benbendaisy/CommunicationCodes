package com.example.lee.secondRound;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 3/22/15.
 */
public class MaxPointsonaLine {
    public int maxPoints(Point[] points) {
        if (null == points) {
            return 0;
        } else if(points.length <= 2){
            return points.length;
        }
        Map<Double, Integer> map = new HashMap<Double, Integer>();
        int max = 0;
        for (int i = 0; i < points.length; i++) {
            int same = 1;
            map.clear();
            int localMax = 0;
            for (int j = 0; j < points.length; j++) {
                if (i == j) {
                    continue;
                }
                if (points[i].x == points[j].x && points[i].y == points[j].y) {
                    same++;
                } else if (i != j) {
                    double slope = calSlope(points, i, j);
                    if (map.containsKey(slope)) {
                        map.put(slope, map.get(slope) + 1);
                    } else {
                        map.put(slope, 1);
                    }
                    localMax = Math.max(localMax, map.get(slope));
                }
            }
            max = Math.max(max, localMax + same);
        }
        return max;
    }

    private double calSlope(Point[] points, int i, int j) {
        int dx = points[j].x - points[i].x;
        int dy = points[j].y - points[i].y;
        if (dx == 0) {
            return Integer.MAX_VALUE;
        }
        return 1.0 * dy / dx;
    }

    public static void main(String[] args) {
        Point[] points = new Point[3];
        points[0] = new Point(0, 0);
        points[1] = new Point(1, 1);
        points[2] = new Point(1, -1);
        MaxPointsonaLine maxPointsonaLine = new MaxPointsonaLine();
        System.out.println(maxPointsonaLine.maxPoints(points));
    }
}
