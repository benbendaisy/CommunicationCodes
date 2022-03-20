package com.example.other;

/**
 * Created by benbendaisy on 4/29/15.
 */
public class CanIWin {
    /*
     * nums is the candidate array that player I can choose
     * used is the array to record which candidate has been taken
     *
     */
    public boolean canIWin(int[] nums, boolean[] used, int target) {
        if (target <= 0) return false;
        //for player I to win
        for (int i = 0; i < nums.length; i++) {
            if (used[i]) continue;
            if (target <= nums[i]) return true;
            //choose nums[i]
            used[i] = true;
            boolean winAllTime = true;
            //for player II to win
            for (int j = 0; j < nums.length; j++) {
                if (used[i]) continue;
                used[j] = true;
                //there is a chance that player II will win
                if (canIWin(nums, used, target - nums[j] - nums[i])) winAllTime = false;
                used[j] = false;
                //if there is a chance playerII will win break
                if (!winAllTime) break;
            }
            used[i] = false;
            if (winAllTime) return true;
        }
        return false;
    }
}
