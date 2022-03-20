package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.
 *
 * The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.
 *
 * Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).
 *
 * In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.
 *
 *
 * Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.
 *
 * For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.
 *
 * -2 (K)	-3	3
 * -5	-10	1
 * 10	30	-5 (P)
 *
 * Notes:
 *
 * The knight's health has no upper bound.
 * Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
 */
public class DungeonGame {
    public int calculateMinimumHP(int[][] dungeon) {
        if(dungeon == null || dungeon.length == 0){
            return 0;
        }

        int[][] dp = new int[dungeon.length][dungeon[0].length];
        int m = dungeon.length - 1;
        int n = dungeon[0].length - 1;
        dp[m][n] = setHp(1 - dungeon[m][n]);

        //initial right most column
        for(int i = m - 1; i >= 0; i--){
            dp[i][n] = setHp(dp[i + 1][n] - dungeon[i][n]);
        }

        //initial bottom column
        for(int j = n - 1; j >= 0; j--){
            dp[m][j] = setHp(dp[m][j + 1] - dungeon[m][j]);
        }

        for(int i = m - 1; i >= 0; i--){
            for(int j = n - 1; j >= 0; j--){
                dp[i][j] = setHp(Math.min(dp[i + 1][j] - dungeon[i][j], dp[i][j + 1] - dungeon[i][j]));
            }
        }

        return dp[0][0];
    }

    private int setHp(int hp){
        return hp <= 0 ? 1 : hp;
    }

    public static void main(String[] args) {
        DungeonGame dungeonGame = new DungeonGame();
        int[][] dungeon = {{-200}};
        System.out.println(dungeonGame.calculateMinimumHP(dungeon));
    }
}
