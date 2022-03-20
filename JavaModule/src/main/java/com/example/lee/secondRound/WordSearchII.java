package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/19/15.
 *
 * Given a 2D board and a list of words from the dictionary, find all words in the board.
 *
 * Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
 *
 * For example,
 * Given words = ["oath","pea","eat","rain"] and board =
 *
 * [
 * ['o','a','a','n'],
 * ['e','t','a','e'],
 * ['i','h','k','r'],
 * ['i','f','l','v']
 * ]
 * Return ["eat","oath"].
 */
public class WordSearchII {
    public List<String> findWords(char[][] board, String[] words) {
        List<String> list = new ArrayList<String>();
        if (null == board || null == words || words.length == 0) return list;

        for (String word : words) {
            if (!list.contains(word) && findWord(board, word)) list.add(word);
        }

        return list;
    }

    private boolean findWord(char[][] board, String word) {
        if (null == word || word.length() == 0) return true;
        int row = board.length;
        int col = board[0].length;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == word.charAt(0)) {
                    visited[i][j] = true;
                    if (findWord(board, visited, word, i, j, 1)) return true;
                    visited[i][j] = false;
                }
            }
        }
        return false;
    }

    private boolean findWord(char[][] board, boolean[][] visited, String word, int i, int j, int idx) {
        if (idx == word.length()) return true;
        int row = board.length;
        int col = board[0].length;

        if (i - 1 >= 0 && board[i - 1][j] == word.charAt(idx) && !visited[i - 1][j]) {
            visited[i - 1][j] = true;
            if (findWord(board, visited, word, i - 1, j, idx + 1)) return true;
            visited[i - 1][j] = false;
        }

        if (i + 1 < row && board[i + 1][j] == word.charAt(idx) && !visited[i + 1][j]) {
            visited[i + 1][j] = true;
            if (findWord(board, visited, word, i + 1, j, idx + 1)) return true;
            visited[i + 1][j] = false;
        }

        if (j - 1 >= 0 && board[i][j - 1] == word.charAt(idx) && !visited[i][j - 1]) {
            visited[i][j - 1] = true;
            if (findWord(board, visited, word, i, j - 1, idx + 1)) return true;
            visited[i][j - 1] = false;
        }

        if (j + 1 < col && board[i][j + 1] == word.charAt(idx) && !visited[i][j + 1]) {
            visited[i][j + 1] = true;
            if (findWord(board, visited, word, i, j + 1, idx + 1)) return true;
            visited[i][j + 1] = false;
        }

        return false;
    }
}
