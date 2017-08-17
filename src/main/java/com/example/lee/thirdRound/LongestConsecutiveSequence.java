package com.example.lee.thirdRound;

import java.util.Arrays;
import java.util.BitSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class LongestConsecutiveSequence {
    public int longestConsecutive(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        Set<Integer> set = Arrays.stream(nums).mapToObj(i -> i).collect(Collectors.toSet());
        int maxLen = 0;
        for (Integer e : nums) {
            int localLen = 1;
            int left = e - 1;
            int right = e + 1;
            set.remove(e);
            while (set.contains(left)) {
                set.remove(left);
                left--;
                localLen++;
            }
            while (set.contains(right)) {
                set.remove(right);
                right++;
                localLen++;
            }
            maxLen = Math.max(maxLen, localLen);
        }
        return maxLen;
    }
    public int longestConsecutiveI(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int max = Arrays.stream(nums).max().getAsInt();
        final BitSet bitSet = new BitSet(max);
        int start = -1;
        int maxLen = 0;
        int minStart = 0;
        List<Integer> positiveList = Arrays.stream(nums).mapToObj(i -> i).filter(i -> i >= 0).collect(Collectors.toList());
        positiveList.stream().forEach(i -> bitSet.set(i));
        for (int i = 0; i <= max; i++) {
            if (bitSet.get(i)) {
                if (i - start > maxLen) {
                    maxLen = i - start;
                    minStart = start + 1;
                }
            } else {
                start = i;
            }
        }
        List<Integer> negativeList = Arrays.stream(nums)
                .mapToObj(i -> i)
                .filter(i -> i < 0)
                .map(i -> -1 * i)
                .collect(Collectors.toList());
        if (negativeList.isEmpty()) {
            return maxLen;
        }
        int newMax = negativeList.stream().max(Integer::compareTo).get();
        BitSet newBitSet = new BitSet(newMax);
        negativeList.stream().forEach(i -> newBitSet.set(i));
        int newStart = 0;
        int newMaxLen = 0;
        for (int i = 0; i <= newMax; i++) {
            if (newBitSet.get(i)) {
                if (i - start > newMaxLen) {
                    newMaxLen = i - start;
                    newStart = start + 1;
                }
            } else {
                start = i;
            }
        }
        return minStart == 0 && newStart == 1 ? maxLen + newMaxLen : maxLen > newMaxLen ? maxLen : newMaxLen;
    }

    public static void main(String[] args) {
        LongestConsecutiveSequence longestConsecutiveSequence = new LongestConsecutiveSequence();
        int[] nums = {9,1,4,7,3,-1,0,5,8,-1,6};
        System.out.println(longestConsecutiveSequence.longestConsecutive(nums));
    }

}
