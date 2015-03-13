package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Given a 2D board and a word, find if the word exists in the grid.
 *
 * The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
 *
 * For example,
 * Given board =
**
 * [
 * ["ABCE"],
 * ["SFCS"],
 * ["ADEE"]
 * ]
 * word = "ABCCED", -> returns true,
 * word = "SEE", -> returns true,
 * word = "ABCB", -> returns false.
 */
public class WordSearch {
    public boolean exist(char[][] board, String word) {
        if(board == null || word == null) {
            return false;
        } else if(word.length() == 0){
            return true;
        }

        boolean[][] visited = new boolean[board.length][board[0].length];
        for(int i = 0; i < board.length; i++){
            for(int j = 0; j < board[0].length; j++){
                if(board[i][j] == word.charAt(0)){
                    visited[i][j] = true;
                    if(word.length() == 1){
                        return true;
                    }else if(existHelper(board, word.substring(1), i, j, visited)){
                        return true;
                    }
                    visited[i][j] = false;
                }
            }
        }
        return false;
    }

    private boolean existHelper(char[][] board, String word, int row, int col, boolean[][] visited){
        if(row >= board.length || row < 0 || col >= board[0].length || col < 0){
            return false;
        } else if(word.length() == 0){
            return true;
        }

        boolean result = false;
        //up
        if(row - 1 >= 0 && !visited[row - 1][col] && board[row - 1][col] == word.charAt(0)){
            boolean[][] newVisited = copyArray(visited);
            newVisited[row - 1][col] = true;
            result = existHelper(board, word.substring(1), row - 1, col, newVisited);
        }
        if(result){
            return true;
        }

        //right
        if(col + 1 < board[0].length && !visited[row][col + 1] && board[row][col + 1] == word.charAt(0)){
            boolean[][] newVisited = copyArray(visited);
            newVisited[row][col + 1] = true;
            result = existHelper(board, word.substring(1), row, col + 1, newVisited);
        }
        if(result){
            return true;
        }

        //down
        if(row + 1 < board.length && !visited[row + 1][col] && board[row + 1][col] == word.charAt(0)){
            boolean[][] newVisited = copyArray(visited);
            newVisited[row + 1][col] = true;
            result = existHelper(board, word.substring(1), row + 1, col, newVisited);
        }
        if(result){
            return true;
        }

        //left
        if(col - 1 >= 0 && !visited[row][col - 1] && board[row][col - 1] == word.charAt(0)){
            boolean[][] newVisited = copyArray(visited);
            newVisited[row][col - 1] = true;
            result = existHelper(board, word.substring(1), row, col - 1, newVisited);
        }

        if(result){
            return true;
        }

        return false;
    }

    private boolean[][] copyArray(boolean[][] visited){
        boolean[][] newVisited = new boolean[visited.length][visited[0].length];
        for(int i = 0; i < visited.length; i++){
            for(int j = 0; j < visited[0].length; j++){
                newVisited[i][j] = visited[i][j];
            }
        }
        return newVisited;
    }

    public static void main(String[] args) {
        char[][] test = {{'A','B','C', 'E'},{'S','F','E','S'},{'A','D','E','E'}};

        WordSearch wordSearch = new WordSearch();
        System.out.println(wordSearch.exist(test, "ABCEFSADEESE"));
    }
}
