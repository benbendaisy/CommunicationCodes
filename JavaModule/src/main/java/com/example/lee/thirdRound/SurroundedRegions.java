package com.example.lee.thirdRound;

import javafx.util.Pair;

import java.util.LinkedList;
import java.util.Queue;

public class SurroundedRegions {
    public void solve(char[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) {
            return;
        }
        handlingZero(board, 'O', 'Y');
        for (int i = 1; i < board.length - 1; i++) {
            for (int j = 1; j < board[i].length - 1; j++) {
                if (board[i][j] == 'O') {
                    bloodFilling(board, i, j, 'O', 'X');
                }
            }
        }
        handlingZero(board, 'Y', 'O');
    }

    private void handlingZero(char[][] board, char from, char to) {
        for (int i = 0; i < board.length; i++) {
            if (board[i][0] == from) {
                bloodFilling(board, i, 0, from, to);
            }
            if (board[i][board[0].length - 1] == from) {
                bloodFilling(board, i, board[0].length - 1, from, to);
            }
        }

        for (int j = 0; j < board[0].length; j++) {
            if (board[0][j] == from) {
                bloodFilling(board, 0, j, from, to);
            }
            if (board[board.length - 1][j] == from) {
                bloodFilling(board, board.length - 1, j, from, to);
            }
        }
    }

    private void bloodFilling(char[][] board, int i, int j, char from, char to) {
        Queue<Pair<Integer, Integer>> queue = new LinkedList<>();
        queue.add(new Pair<>(i, j));
        while (!queue.isEmpty()) {
            Pair<Integer, Integer> pair = queue.poll();
            if (pair.getKey() < 0 || pair.getKey() >= board.length
                    || pair.getValue() < 0 || pair.getValue() >= board[0].length
                    || board[pair.getKey()][pair.getValue()] != from) {
                continue;
            }
            board[pair.getKey()][pair.getValue()] = to;
            queue.add(new Pair<>(pair.getKey() - 1, pair.getValue()));
            queue.add(new Pair<>(pair.getKey() + 1, pair.getValue()));
            queue.add(new Pair<>(pair.getKey(), pair.getValue() - 1));
            queue.add(new Pair<>(pair.getKey(), pair.getValue() + 1));
        }
    }

    private void bloodFillingI(char[][] board, int i, int j, char from, char to) {
        if (i < 0 || i >= board.length || j < 0 || j >= board[0].length) {
            return;
        } else if (board[i][j] != from) {
            return;
        }
        board[i][j] = to;
        bloodFillingI(board, i - 1, j, from, to);
        bloodFillingI(board, i + 1, j, from, to);
        bloodFillingI(board, i, j - 1, from, to);
        bloodFillingI(board, i, j + 1, from, to);
    }


}
