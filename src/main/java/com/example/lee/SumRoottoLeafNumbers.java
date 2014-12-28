package com.example.lee;

import com.example.lee.model.TreeNode;

/**
 * Created by benbendaisy on 12/27/14.
 */
public class SumRoottoLeafNumbers {
    private int sum = 0;
    public int sumNumbers(TreeNode root) {
        if(root != null){
            sumNumbersHelper(root, "");
        }
        return sum;
    }

    public void sumNumbersHelper(TreeNode root, String str) {
        if(root != null && root.left == null && root.right == null){
            str = str + root.val;
            sum += Integer.parseInt(str);
        } else {
            str = str + root.val;
            if(root.left != null){
                sumNumbersHelper(root.left, str);
            }

            if(root.right != null){
                sumNumbersHelper(root.right, str);
            }
        }
    }
}
