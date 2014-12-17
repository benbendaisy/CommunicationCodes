package com.example.lee;

import java.awt.*;
import java.util.HashMap;
import java.util.Map;

/**
 * Created by pzhong1 on 12/16/14.
 * Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
 */
public class MaxPointsonaLine {
    public int maxPoints(Point[] points) {
        if(null == points){
            return 0;
        } else if(points.length <= 2){
            return points.length;
        }
        Map<Double, Integer> map = new HashMap<Double, Integer>();
        int max = 0, same = 0;
        for(int i = 0; i < points.length; i++){
            same = 1;
            map.clear();
            for(int j = 0; j < points.length; j++){
                if(i == j){
                    continue;
                } else if(points[i].x == points[j].x && points[i].y == points[j].y){
                    same++;
                    continue;
                }
                double slope = calSlope(points[i], points[j]);
                if(map.containsKey(slope)){
                    map.put(slope, map.get(slope) + 1);
                } else {
                    map.put(slope, 1);
                }
            }
            if(map.isEmpty()){
                max = Math.max(max, same);
            }
            for(double key : map.keySet()){
                max = Math.max(max, same + map.get(key));
            }
        }
        return max;
    }
    private double calSlope(Point A, Point B){
        int dx = A.x - B.x;
        int dy = A.y - B.y;
        if(dx == 0){
            return Integer.MAX_VALUE;
        }
        return 1.0 * dy / dx;
    }
}
