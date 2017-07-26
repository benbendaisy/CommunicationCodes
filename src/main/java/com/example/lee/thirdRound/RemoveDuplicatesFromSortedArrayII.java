package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/15/17.
 */
public class RemoveDuplicatesFromSortedArrayII {
    public int removeDuplicates(int[] nums) {
        if (nums == null) {
            return 0;
        } else if (nums.length < 3) {
            return nums.length;
        }
        int l = 0, r = 0;
        while (r <  nums.length) {
            int cnt = 1;
            while (r <  nums.length - 1 && nums[r] == nums[r + 1]) {
                if (cnt < 2) {
                    swap(nums, l, r);
                    l++;
                }
                cnt++;
                r++;
            }
            swap(nums, l, r);
            l++;
            r++;
        }
        return l;
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public static void main(String[] args) {
        RemoveDuplicatesFromSortedArrayII removeDuplicatesFromSortedArrayII = new RemoveDuplicatesFromSortedArrayII();
        int[] nums = {1,1,1,2,2,2,3,3};
        System.out.println(removeDuplicatesFromSortedArrayII.removeDuplicates(nums));
    }
}
