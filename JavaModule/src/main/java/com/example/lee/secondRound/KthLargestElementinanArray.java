package com.example.lee.secondRound;

import java.util.*;

/**
 * Created by benbendaisy on 5/24/15.
 *
 * Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
 *
 * For example,
 * Given [3,2,1,5,6,4] and k = 2, return 5.
 *
 * Note:
 * You may assume k is always valid, 1 ≤ k ≤ array's length.
 */
public class KthLargestElementinanArray {
    public int findKthLargest(int[] nums, int k) {
        if (null == nums || k < 1 || k > nums.length) return -1;
        int l = 0, r = nums.length - 1;
        while (k > 0 && l < r) {
            int idx = patition(nums, l, r);
            int len = r - idx + 1;
            if (len == k) {
                int min = nums[l];
                for (int i = l; i <= r; i++) min = Math.min(min, nums[i]);
                return min;
            } else if (len < k) {
                r = idx - 1;
                k = k - len;
            } else {
                l = idx;
            }
        }
        //handle the case k == 1
        int min = nums[0];
        for (int i = 0; i < nums.length; i++) min = Math.min(min, nums[i]);
        return min;
    }

    private int patition(int[] nums, int s, int e) {
        int pivot = nums[e];
        int l = s, r = e - 1;
        while (l < r) {
            while (l < r && nums[l] < pivot) l++;
            while (r > l && nums[r] > pivot) r--;
            if (l < r) {
                swap(nums, l, r);
            }
        }
        swap(nums, l, e);
        return l;
    }

    private void swap(int[] nums, int i, int j) {
        int t = nums[i];
        nums[i] = nums[j];
        nums[j] = t;
    }

    public int findKthLargestI(int[] nums, int k) {
        if (null == nums || k < 1 || k > nums.length) return -1;
        Queue<Integer> queue = new PriorityQueue<Integer>(k);
        for (int i = 0; i < k; i++) {
            queue.add(nums[i]);
        }
        for (int i = k; i < nums.length; i++){
            if (queue.peek() < nums[i]){
                queue.poll();
                queue.add(nums[i]);
            }
        }
        return queue.peek();
    }

    public static void main(String[] args) {
        int[] nums = {2, 1};
        KthLargestElementinanArray kthLargestElementinanArray = new KthLargestElementinanArray();
        System.out.println(kthLargestElementinanArray.findKthLargest(nums, 2));
    }
}
