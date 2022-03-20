package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/5/15.
 */
public class RemoveDuplicatesfromSortedArrayII {
    public int removeDuplicates(int[] nums) {
        if (nums == null) {
            return 0;
        } else if (nums.length < 3) {
            return nums.length;
        }
        int cnt = 1, idx = 1, len = nums.length - 1;
        while (idx <= len) {
            if (nums[idx - 1] == nums[idx]) {
                idx++;
                cnt++;
                while (idx <= len && nums[idx - 1] == nums[idx]) {
                    moveElement(nums, idx, len);
                    len--;
                }
            } else {
                idx++;
                cnt++;
            }
        }
        return cnt;
    }

    private void moveElement(int[] nums, int idx, int len) {
        for (int i = idx; i < len; i++) {
            nums[i] = nums[i + 1];
        }
    }

    public static void main(String[] args) {
        RemoveDuplicatesfromSortedArrayII arrayII = new RemoveDuplicatesfromSortedArrayII();
        int[] arrs = {-3,-1,-1,0,0,0,0,0,2};
        System.out.println(arrayII.removeDuplicates(arrs));
    }
}
