package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;
import java.util.Optional;

public class SingleNumberII {
    public int singleNumber(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        } else if (nums.length == 1) {
            return nums[0];
        }
        int res = 0;
        for (int i = 0; i < 32; i++) {
            int cnt = 0;
            for (int j = 0; j < nums.length; j++) {
                if (((nums[j] >> i) & 1) == 1) {
                    cnt++;
                }
            }
            res |= ((cnt % 3) << i);
        }
        return res;
    }
    public int singleNumberI(int[] nums) {
        if (nums == null || nums.length == 0) {
            return -1;
        } else if (nums.length == 1) {
            return nums[0];
        }
        Map<Integer, Integer> cachedData = new HashMap<>();
        for (int num : nums) {
            int cnt = cachedData.getOrDefault(num, 0);
            cachedData.put(num, ++cnt);
        }
        Optional<Integer> singleNum = cachedData.entrySet().stream().filter(entry -> entry.getValue() == 1).map(x -> x.getKey()).findAny();
        return singleNum.isPresent() ? singleNum.get() : -1;
    }
}
