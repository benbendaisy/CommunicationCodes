package com.example.lee.secondRound;

import java.awt.*;
import java.util.LinkedList;
import java.util.*;

/**
 * Created by benbendaisy on 4/8/15.
 *
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 *
 * Example 1:
 *
 * 11110
 * 11010
 * 11000
 * 00000
 * Answer: 1
 *
 * Example 2:
 *
 * 11000
 * 11000
 * 00100
 * 00011
 * Answer: 3
 */
public class NumberofIslands {
    public int numIslands(char[][] grid) {
        if (null == grid || grid.length < 1) return 0;
        int cnt = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    cnt++;
                    setZeros(grid, i, j);
                }
            }
        }
        return cnt;
    }

    private void setZeros(char[][] grid, int i, int j) {
        Queue<Point> que = new LinkedList<Point>();
        que.add(new Point(i, j));
        while (!que.isEmpty()) {
            Point p = que.poll();
            grid[p.x][p.y] = '0';
            if (p.x < grid.length - 1 && grid[p.x + 1][p.y] == '1') que.add(new Point(p.x + 1, p.y));
            if (p.x > 0 && grid[p.x - 1][p.y] == '1') que.add(new Point(p.x - 1, p.y));
            if (p.y < grid[0].length - 1 && grid[p.x][p.y + 1] == '1') que.add(new Point(p.x, p.y + 1));
            if (p.y > 0 && grid[p.x][p.y - 1] == '1') que.add(new Point(p.x, p.y - 1));
        }
    }


}
