package com.example.backtracking;

/**
 * Created by benbendaisy on 5/22/15.
 */
public class RatMazing {
    private boolean isSafe(int[][] maze, int x, int y) {
        if (x >= 0 && x < maze.length && y >= 0 && y < maze[0].length && maze[x][y] == 1) return true;
        return false;
    }

    private boolean solveMazeUtil(int[][] maze, int x, int y, int[][] sln) {
        if (x == maze.length - 1 && y == maze[0].length - 1) {
            sln[x][y] = 1;
            return true;
        }
        if (isSafe(maze, x, y)) {
            sln[x][y] = 1;
            if (solveMazeUtil(maze, x + 1, y, sln)) return true;
            if (solveMazeUtil(maze, x, y + 1, sln)) return true;
            sln[x][y] = 0;
        }
        return false;
    }

    public static void printSln(int[][] sln) {
        for (int i = 0; i < sln.length; i++) {
            for (int j = 0; j < sln[0].length; j++) {
                System.out.print(sln[i][j] + ", ");
            }
            System.out.print("\n");
        }
    }

    public boolean solveRatMazing(int[][] maze) {
        int[][] sln = new int[maze.length][maze[0].length];
        boolean res = solveMazeUtil(maze, 0, 0, sln);
        printSln(sln);
        return res;
    }

    public static void main(String[] args) {
        RatMazing ratMazing = new RatMazing();
        int[][] maze = { {1, 0, 0, 0},
                {1, 1, 0, 1},
                {0, 1, 0, 0},
                {1, 1, 1, 1}
        };
        ratMazing.solveRatMazing(maze);
    }
}
