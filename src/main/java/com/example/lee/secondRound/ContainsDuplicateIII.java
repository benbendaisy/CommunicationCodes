package com.example.lee.secondRound;

import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Set;

/**
 * Created by benbendaisy on 5/31/15.
 *
 * Given an array of integers, find out whether there are two distinct indices i and j in the array such that the difference between nums[i] and nums[j] is at most t and the difference between i and j is at most k.
 *
 */
public class ContainsDuplicateIII {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (null == nums || nums.length < 1 || k < 1) return false;
        Map<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();
        int idx = 0;
        for (int i = 0; i < nums.length; i++) {
            Set<Integer> set = map.keySet();
            boolean isFirst = true;
            for (int it : set) {
                if (isFirst) {
                    idx = it;
                    isFirst = false;
                }
                if (i - map.get(it) <= k && Math.abs(nums[i] - it) <= t) return true;
            }
            if (map.size() == k) map.remove(idx);
            map.put(nums[i], i);

        }
        return false;
    }
}
