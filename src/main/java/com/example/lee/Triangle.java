package com.example.lee;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 12/31/14.
 * Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
 * For example, given the following triangle
 * [
 * [2],
 * [3,4],
 * [6,5,7],
 * [4,1,8,3]
 * ]
 * The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

 * Note:
 * Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
 */
public class Triangle {
    public int minimumTotal(List<List<Integer>> triangle) {
        if(triangle == null || triangle.size() == 0 ){
            return 0;
        }

        int rows = triangle.size();
        int[] dp = new int[rows];
        for(int i = 0; i < rows; i++){
            dp[i] = triangle.get(rows-1).get(i);
        }
        for(int i = rows - 2; i >= 0; i--){
            List<Integer> list = triangle.get(i);
            int size = list.size();
            for(int j = 0; j < size; j++){
                dp[j] = Math.min(dp[j], dp[j + 1]) + triangle.get(i).get(j);
            }
        }
        return dp[0];
    }

    public static void main(String[] args) {
        Triangle triangle = new Triangle();
        List<Integer> list1 = new ArrayList<Integer>(Arrays.asList(-1));
        List<Integer> list2 = new ArrayList<Integer>(Arrays.asList(3, 2));
        List<Integer> list3 = new ArrayList<Integer>(Arrays.asList(1, -2, -1));
        List<List<Integer>> tri = new ArrayList<List<Integer>>();
        tri.add(list1);
        tri.add(list2);
        tri.add(list3);
        System.out.println(triangle.minimumTotal(tri));
    }
}
