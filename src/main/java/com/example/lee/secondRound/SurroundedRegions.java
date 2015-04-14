package com.example.lee.secondRound;

import java.awt.*;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Set;

/**
 * Created by benbendaisy on 4/6/15.
 *
 * Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
 *
 * A region is captured by flipping all 'O's into 'X's in that surrounded region.
 *
 * For example,
 * X X X X
 * X O O X
 * X X O X
 * X O X X
 * After running your function, the board should be:
 *
 * X X X X
 * X X X X
 * X X X X
 * X O X X
 *
 */
public class SurroundedRegions {
    public void solve(char[][] board) {
        if (null == board || board.length <= 1 || board[0].length <= 1) return;
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'O' && isSurrounded(board, i, j)) {
                    setBoard(board, i, j);
                }
            }
        }
    }
    private boolean isSurrounded(char[][] board, int i, int j) {
        Queue<Point> queue = new LinkedList<Point>();
        Set<String> set = new HashSet<String>();
        Point point = new Point(i, j);
        queue.add(point);
        while (!queue.isEmpty()) {
            point = queue.poll();
            if (board[point.x][point.y] == 'O') {
                if (point.x == 0 || point.x == board.length - 1 || point.y == 0 || point.y == board[0].length - 1) {
                    return false;
                }
                if (board[point.x - 1][point.y] == 'O' && set.add((point.x - 1) + "" + (point.y))) queue.add(new Point(point.x - 1, point.y));
                if (board[point.x + 1][point.y] == 'O' && set.add((point.x + 1) + "" + (point.y))) queue.add(new Point(point.x + 1, point.y));
                if (board[point.x][point.y - 1] == 'O' && set.add((point.x) + "" + (point.y - 1))) queue.add(new Point(point.x, point.y - 1));
                if (board[point.x][point.y + 1] == 'O' && set.add((point.x) + "" + (point.y + 1))) queue.add(new Point(point.x, point.y + 1));
            }
        }
        return true;
    }

    private void setBoard(char[][] board, int i, int j) {
        Queue<Point> queue = new LinkedList<Point>();
        Set<String> set = new HashSet<String>();
        Point point = new Point(i, j);
        queue.add(point);
        while (!queue.isEmpty()) {
            point = queue.poll();
            if (board[point.x][point.y] == 'O') {
                if (board[point.x - 1][point.y] == 'O' && set.add((point.x - 1) + "" + (point.y))) queue.add(new Point(point.x - 1, point.y));
                if (board[point.x + 1][point.y] == 'O' && set.add((point.x + 1) + "" + (point.y))) queue.add(new Point(point.x + 1, point.y));
                if (board[point.x][point.y - 1] == 'O' && set.add((point.x) + "" + (point.y - 1))) queue.add(new Point(point.x, point.y - 1));
                if (board[point.x][point.y + 1] == 'O' && set.add((point.x) + "" + (point.y + 1))) queue.add(new Point(point.x, point.y + 1));
                board[point.x][point.y] = 'X';
            }
        }
    }

    public void solveI(char[][] board) {
        if (null == board || board.length <= 1 || board[0].length <= 1) return;
        int row = board.length;
        int col = board[0].length;
        //replace 'O' in the first column and last colomn with 'y'
        for (int i = 0; i < row; i++) {
            if (board[i][0] == 'O') bloodFill(board, i, 0, 'O', 'y');
            if (board[i][col - 1] == 'O') bloodFill(board, i, col - 1, 'O', 'y');
        }
        ////replace 'O' in the first row and last row with 'y'
        for (int j = 0; j < col; j++) {
            if (board[0][j] == 'O') bloodFill(board, 0, j, 'O', 'y');
            if (board[row - 1][j] == 'O') bloodFill(board, row - 1, j, 'O', 'y');
        }

        //left 'O' should be valid candidate
        for (int i = 1; i < row - 1; i++) {
            for (int j = 1; j < col - 1; j++) {
                if (board[i][j] == 'O') bloodFill(board, i, j, 'O', 'X');
            }
        }

        ////replace 'y' in the first column and last colomn with 'O'
        for (int i = 0; i < row; i++) {
            if (board[i][0] == 'y') bloodFill(board, i, 0, 'y', 'O');
            if (board[i][col - 1] == 'y') bloodFill(board, i, col - 1, 'y', 'O');
        }
        //replace 'y' in the first column and last colomn with 'O'
        for (int j = 0; j < col; j++) {
            if (board[0][j] == 'y') bloodFill(board, 0, j, 'y', 'O');
            if (board[row - 1][j] == 'y') bloodFill(board, row - 1, j, 'y', 'O');
        }

    }

    private void bloodFill(char[][] board, int i, int j, char ch1, char ch2) {
        Queue<Point> queue = new LinkedList<Point>();
        Point point = new Point(i, j);
        queue.add(point);
        while (!queue.isEmpty()) {
            point = queue.poll();
            if (board[point.x][point.y] == ch1) {
                if (point.x > 0 && board[point.x - 1][point.y] == ch1) queue.add(new Point(point.x - 1, point.y));
                if (point.x < board.length - 1 && board[point.x + 1][point.y] == ch1) queue.add(new Point(point.x + 1, point.y));
                if (point.y > 0 && board[point.x][point.y - 1] == ch1) queue.add(new Point(point.x, point.y - 1));
                if (point.y < board[0].length - 1 && board[point.x][point.y + 1] == ch1) queue.add(new Point(point.x, point.y + 1));
            }
            board[point.x][point.y] = ch2;
        }
    }

    public static void main(String[] args) {
        char[][] board = {{'O', 'X', 'X', 'O', 'X'},{'X', 'O', 'O', 'X', 'O'},
                {'X', 'O', 'X', 'O', 'X'},{'O', 'X', 'O', 'O', 'O'},{'X', 'X', 'O', 'X', 'O'}};
        //char[][] board = {{'0', '0', '0'}, {'0', '0', '0'}, {'0', 'O', 'O'}};
        SurroundedRegions surroundedRegions = new SurroundedRegions();
        surroundedRegions.solveI(board);
        //Point point = new Point(1, 2);
        //System.out.println((point.x - 1) + "" + (point.y));
        System.out.println("hello");
    }
}
