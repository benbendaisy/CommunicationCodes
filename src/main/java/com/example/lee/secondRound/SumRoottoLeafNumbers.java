package com.example.lee.secondRound;

import com.example.lee.model.TreeNode;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/6/15.
 *
 * given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.
 *
 * An example is the root-to-leaf path 1->2->3 which represents the number 123.
 *
 * Find the total sum of all root-to-leaf numbers.
 *
 * For example,
 *
 *   1
 *  / \
 * 2   3
 * The root-to-leaf path 1->2 represents the number 12.
 * The root-to-leaf path 1->3 represents the number 13.
 *
 * Return the sum = 12 + 13 = 25.
 *
 */
public class SumRoottoLeafNumbers {
    public int sumNumbers(TreeNode root) {
        if (null == root) return 0;
        List<String> list = new ArrayList<String>();
        getAllNumbers(root, list, "");
        int res = 0;
        for (String str : list) {
            res += Integer.parseInt(str);
        }
        return res;
    }

    private void getAllNumbers(TreeNode root, List<String> list, String str) {
        String newStr = str + root.val;
        if (null == root.left && null == root.right) {
            list.add(newStr);
        } else {
            if (null != root.left) getAllNumbers(root.left, list, newStr);
            if (null != root.right) getAllNumbers(root.right, list, newStr);
        }
    }
}
