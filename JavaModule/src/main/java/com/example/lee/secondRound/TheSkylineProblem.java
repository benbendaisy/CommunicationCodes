package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/25/15.
 *
 * A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo (Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).
 *
 * Buildings  Skyline Contour
 * The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height. It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0. You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
 *
 * For instance, the dimensions of all buildings in Figure A are recorded as: [ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .
 *
 * The output is a list of "key points" (red dots in Figure B) in the format of [ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline. A key point is the left endpoint of a horizontal line segment. Note that the last key point, where the rightmost building ends, is merely used to mark the termination of the skyline, and always has zero height. Also, the ground in between any two adjacent buildings should be considered part of the skyline contour.
 *
 * For instance, the skyline in Figure B should be represented as:[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].
 *
 * Notes:
 *
 * The number of buildings in any input list is guaranteed to be in the range [0, 10000].
 * The input list is already sorted in ascending order by the left x position Li.
 * The output list must be sorted by the x position.
 * There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...[2 3], [4 5], [12 7], ...]
 */
public class TheSkylineProblem {
    public List<int[]> getSkyline(int[][] buildings) {
        if (null == buildings || buildings.length < 1) return new ArrayList<int[]>();
        return getSkyline(buildings, 0, buildings.length - 1);
    }

    private List<int[]> getSkyline(int[][] buildings, int l, int r) {
        if (l == r) {
            List<int[]> list = new ArrayList<int[]>();
            int[] t1 = new int[2];
            t1[0] = buildings[l][0];
            t1[1] = buildings[l][2];
            int[] t2 = new int[2];
            t2[0] = buildings[l][1];
            t2[1] = 0;
            list.add(t1);
            list.add(t2);
            return list;
        }
        int mid = (l + r) / 2;
        List<int[]> left = getSkyline(buildings, l, mid);
        List<int[]> right = getSkyline(buildings, mid + 1, r);
        return mergeSkyline(left, right);
    }

    private List<int[]> mergeSkyline(List<int[]> l, List<int[]> r) {
        int idxL = 0, idxR = 0;
        List<int[]> list = new ArrayList<int[]>();
        int hL = 0, hR = 0, max = 0;
        while (idxL < l.size() && idxR < r.size()) {
            if (l.get(idxL)[0] < r.get(idxR)[0]) {
                hL = l.get(idxL)[1];
                int[] t = new int[2];
                t[0] = l.get(idxL)[0];
                if (max == Math.max(hL, hR)) {
                    idxL++;
                    continue;
                }
                max = Math.max(hL, hR);
                t[1] = max;
                list.add(t);
                idxL++;
            } else if (l.get(idxL)[0] > r.get(idxR)[0]) {
                hR = r.get(idxR)[1];
                int[] t = new int[2];
                t[0] = r.get(idxR)[0];
                if (max == Math.max(hL, hR)) {
                    idxR++;
                    continue;
                }
                max = Math.max(hL, hR);
                t[1] = max;
                list.add(t);
                idxR++;
            } else {
                hR = r.get(idxR)[1];
                hL = l.get(idxL)[1];
                int[] t = new int[2];
                t[0] = r.get(idxR)[0];
                if (max == Math.max(hL, hR)) {
                    idxR++;
                    idxL++;
                    continue;
                }
                max = Math.max(hL, hR);
                t[1] = max;
                list.add(t);
                idxR++;
                idxL++;
            }
        }

        while (idxL < l.size()) {
            int[] t = new int[2];
            t[0] = l.get(idxL)[0];
            t[1] = l.get(idxL)[1];
            list.add(t);
            idxL++;
        }

        while (idxR < r.size()) {
            int[] t = new int[2];
            t[0] = r.get(idxR)[0];
            t[1] = r.get(idxR)[1];
            list.add(t);
            idxR++;
        }

        return list;
    }
}
