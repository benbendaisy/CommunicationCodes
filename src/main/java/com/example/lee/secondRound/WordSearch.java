package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/8/15.
 */
public class WordSearch {
    public boolean exist(char[][] board, String word) {
        if (board == null || word == null) return false;
        if (word.length() == 0) return true;
        int row = board.length;
        int col = board[0].length;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == word.charAt(0) && exist(board, word, i, j, visited, 0)) return true;
            }
        }
        return false;
    }

    private boolean exist(char[][] board, String word, int x, int y, boolean[][] visited, int idx) {
        if (idx == word.length()) return true;
        int row = board.length;
        int col = board[0].length;
        if (x < 0 || x >= row || y < 0 || y >= col) return false;
        char ch = word.charAt(idx);
        if (!visited[x][y] && board[x][y] == ch) {
            visited[x][y] = true;
            if (exist(board, word, x + 1, y, visited, idx + 1) || exist(board, word, x - 1, y, visited, idx + 1) || exist(board, word, x, y + 1, visited, idx + 1) || exist(board, word, x, y - 1, visited, idx + 1)) return true;
            visited[x][y] = false;
        }
        return false;
    }


    public boolean existI(char[][] board, String word) {
        if (board == null || word == null) return false;
        if (word.length() == 0) return true;
        int row = board.length;
        int col = board[0].length;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i][j] == word.charAt(0) && exist(board, word, i, j, visited)) {
                    return true;
                }
            }
        }
        return false;
    }

    private boolean exist(char[][] board, String word, int x, int y, boolean[][] visited) {
        if (word.length() == 0) return true;
        int row = board.length;
        int col = board[0].length;
        if (x < 0 || x >= row || y < 0 || y >= col) return false;
        for (int i = x; i < row; i++) {
            for (int j = y; j < col; j++) {
                char ch = word.charAt(0);
                if (!visited[i][j] && board[i][j] == ch) {
                    visited[i][j] = true;
                    String subString = word.substring(1);
                    if (exist(board, subString, i + 1, j, visited) || exist(board, subString, i - 1, j, visited) || exist(board, subString, i, j + 1, visited) || exist(board, subString, i, j - 1, visited)) return true;
                    visited[i][j] = false;
                }
            }
        }
        return false;
    }


    public static void main(String[] args) {
        char[][] board = {{'a', 'a', 'a', 'a'}, {'a', 'a', 'a', 'a'}, {'a', 'a', 'a', 'a'}};
        //char[][] board = {{'A','B','C', 'E'},{'S','F','E','S'},{'A','D','E','E'}};
        WordSearch wordSearch = new WordSearch();
        System.out.println(wordSearch.exist(board, "aaaaaaaaaaaaa"));
    }
}
