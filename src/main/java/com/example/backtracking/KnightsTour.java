package com.example.backtracking;

import java.util.Arrays;

/**
 * Created by benbendaisy on 5/22/15.
 */
public class KnightsTour {
    private boolean isSafe(int x, int y, int[][] sln) {
        if (x >= 0 && x < sln.length && y >= 0 && y < sln[0].length && sln[x][y] == -1) return true;
        return false;
    }

    private boolean knightTour(int[][] sln, int x, int y, int[] xMove, int[] yMove, int move) {
        if (move == sln.length * sln[0].length) return true;
        int nextX = 0, nextY = 0;
        for (int i = 0; i < 8; i++) {
            nextX = x + xMove[i];
            nextY = y + yMove[i];
            if (isSafe(nextX, nextY, sln)) {
                sln[nextX][nextY] = move;
                if (knightTour(sln, nextX, nextY, xMove, yMove, move + 1)) return true;
                sln[nextX][nextY] = -1;
            }
        }
        return false;
    }

    public boolean knightTour() {
        int[][] sln = new int[8][8];
        for (int[] row : sln) {
            Arrays.fill(row, -1);
        }
        //RatMazing.printSln(sln);
        int[] xMove = {2, 1, -1, -2, -2, -1, 1, 2};
        int[] yMove = {1, 2, 2, -1, 1, -2, -2, -1};
        sln[0][0] = 0;
        if (knightTour(sln, 0, 0, xMove, yMove, 1)) {
            RatMazing.printSln(sln);
            return true;
        } else {
            System.out.println("no solution");
            return false;
        }
    }

    public static void main(String[] args) {
        KnightsTour knightsTour = new KnightsTour();
        knightsTour.knightTour();
    }
}
