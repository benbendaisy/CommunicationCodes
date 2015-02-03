package com.example.lee;

/**
 * Created by benbendaisy on 2/2/15.
 *
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 *
 * Each element in the array represents your maximum jump length at that position.
 *
 * Your goal is to reach the last index in the minimum number of jumps.
 *
 * For example:
 * Given array A = [2,3,1,1,4]
 *
 * The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
 */
public class JumpGameII {
    //gridy algorithm that always pick the max steps that can reach
    //refer to http://www.cnblogs.com/lichen782/p/leetcode_Jump_Game_II.html
    public int jump(int[] A) {
        if(null == A || A.length == 0){
            return 0;
        }
        //how far current position can reach
        int steps = 0;
        //how many jumps
        int count = 0;
        //how far last position can reach
        int last = 0;
        for(int i = 0; i < A.length; i++){
            //check if need to jump
            if(i > last){
                last = steps;
                count++;
            }

            //always get the farest position that can reach
            steps = Math.max(steps, i + A[i]);
        }

        return count;
    }

    public static void main(String[] args) {
        JumpGameII jumpGameII = new JumpGameII();
        int[] num = {1, 1, 1, 1};
        System.out.println(jumpGameII.jump(num));
    }
}
