package com.example.lee;

import java.awt.*;
import java.util.*;

/**
 * Created by benbendaisy on 12/27/14.
 * Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.
 * A region is captured by flipping all 'O's into 'X's in that surrounded region.
 * For example,
 * X X X X
 * X O O X
 * X X O X
 * X O X X
 * After running your function, the board should be:
 * X X X X
 * X X X X
 * X X X X
 * X O X X
 */
public class SurroundedRegions {
    public void solve(char[][] board) {
        if(board == null || board.length < 3 || board[0].length < 3){
            return;
        }
        int len1 = board.length;
        int len2 = board[0].length;

        //step1: replace all 'O' and its connected neighbours are also 'O' to 'y'. Then, all left 'O'are validate candidate
        for(int i = 0; i < len2; i++){
            if(board[0][i] == 'O'){
                bloodFill(board, 0, i, 'O', 'y');
            }
            if(board[len1 - 1][i] == 'O'){
                bloodFill(board, len1 - 1, i, 'O', 'y');
            }
        }

        for(int i = 0; i < len1; i++){
            if(board[i][0] == 'O'){
                bloodFill(board, i, 0, 'O', 'y');
            }
            if(board[i][len2 - 1] == 'O'){
                bloodFill(board, i, len2 - 1, 'O', 'y');
            }
        }

        //step2: replace all candidate 'O' and its connected neighbours are also 'O' to 'X'.
        for(int i = 1; i < len1 -1; i++){
            for(int j = 1; j < len2 -1; j++){
                if(board[i][j] == 'O'){
                    bloodFill(board, i, j, 'O', 'X');
                }
            }
        }

        //step3: replace all 'y's back to 'O'.
        for(int i = 0; i < len1; i++){
            for(int j = 0; j < len2; j++){
                if(board[i][j] == 'y'){
                    board[i][j] = 'O';
                }
            }
        }
    }

    private void bloodFill(char[][] board, int x, int y, char t, char r){
        Queue<Point> queue = new LinkedList<Point>();
        Point s = new Point(x, y);
        int len1 = board.length;
        int len2 = board[0].length;
        queue.add(s);
        while(!queue.isEmpty()){
            Point p = queue.poll();
            board[p.x][p.y] = r;
            int px = p.x - 1;
            int py = p.y - 1;

            if(px > 0 && px < len1 && board[px][p.y] == t){
                queue.add(new Point(px, p.y));
            }
            if(py > 0 && py < len2 && board[p.x][py] == t){
                queue.add(new Point(p.x, py));
            }

            px = p.x + 1;
            py = p.y + 1;
            if(px > 0 && px < len1 && board[px][p.y] == t){
                queue.add(new Point(px, p.y));
            }
            if(py > 0 && py < len2 && board[p.x][py] == t){
                queue.add(new Point(p.x, py));
            }
        }
    }

    public void printMatrix(char[][] matrix){
        int len1 = matrix.length;
        int len2 = matrix[0].length;
        for(int i = 0; i < len1; i++){
            for(int j = 0; j < len2; j++){
                System.out.print(matrix[i][j]);
            }
            System.out.print('\n');
        }
    }
    public static void main(String[] args) {
        char[][] matrix = {{'X', 'X', 'X', 'X'},{'X', 'O', 'O', 'X'},{'X', 'X', 'O', 'X'}, {'X', 'O', 'X', 'X'}, {'X', 'X', 'X', 'X'}};
        SurroundedRegions surroundedRegions = new SurroundedRegions();
        surroundedRegions.solve(matrix);
        surroundedRegions.printMatrix(matrix);
    }
}
