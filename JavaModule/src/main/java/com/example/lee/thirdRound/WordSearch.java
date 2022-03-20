package com.example.lee.thirdRound;

import java.util.Arrays;

/**
 * Created by benbendaisy on 7/15/17.
 */
public class WordSearch {
    public boolean exist(char[][] board, String word) {
        if (board == null || word == null || board.length == 0 || board[0].length == 0) {
            return false;
        }
        boolean[][] visited = new boolean[board.length][board[0].length];
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (existHelper(board, word, i, j, 0, visited)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean existHelper(char[][] board, String word, int idx, int idy, int curIdx, boolean[][] visited) {
        if (curIdx == word.length()) {
            return true;
        } else if (idx < 0 || idx >= board.length || idy < 0
                || idy >= board[0].length || visited[idx][idy]
                || board[idx][idy] != word.charAt(curIdx)) {
            return false;
        }
        visited[idx][idy] = true;
        curIdx++;
        boolean res = existHelper(board, word, idx - 1, idy, curIdx, visited)
                || existHelper(board, word, idx + 1, idy, curIdx, visited)
                || existHelper(board, word, idx, idy - 1, curIdx, visited)
                || existHelper(board, word, idx, idy + 1, curIdx, visited);
        visited[idx][idy] = false;
        return res;
    }
}
