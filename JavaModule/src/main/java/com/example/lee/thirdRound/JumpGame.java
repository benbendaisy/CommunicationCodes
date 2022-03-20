package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/7/17.
 */
public class JumpGame {
    public boolean canJump(int[] nums) {
        if (nums == null || nums.length < 1) {
            return false;
        }

        int canJump = 0;
        int l = 0;
        while (l < nums.length) {
            if (canJump < l) {
                return false;
            }
            canJump = Math.max(l + nums[l], canJump);
            l++;
        }
        return true;
    }

    public static void main(String[] args) {
        JumpGame jumpGame = new JumpGame();
        System.out.println();
    }
}
