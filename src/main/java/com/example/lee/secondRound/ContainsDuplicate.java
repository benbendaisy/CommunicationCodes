package com.example.lee.secondRound;

import java.util.BitSet;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 5/24/15.
 *
 * Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
 *
 */
public class ContainsDuplicate {

    public boolean containsDuplicate(int[] nums) {
        if (null == nums || nums.length < 2) return false;
        Set<Integer> set = new HashSet<Integer>();
        for (int i : nums) {
            if (!set.add(i)) return true;
        }
        return false;
    }

    //BitSet cannot handle negative index
    public boolean containsDuplicateI(int[] nums) {
        if (null == nums || nums.length < 2) return false;
        BitSet bitSet = new BitSet();
        for (int i : nums) {
            if (bitSet.get(i)) {
                return true;
            } else {
                bitSet.set(i);
            }
        }
        return false;
    }
}
