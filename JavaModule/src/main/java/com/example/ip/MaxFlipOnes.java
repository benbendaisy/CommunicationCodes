package com.example.ip;

/**
 * Created by benben on 5/19/15.
 *
 * 给一个矩阵，只含有1,0 。可以翻转一次。可以翻转任意两个index之间所有的值，翻
 * 转就是
 * 1 -->0  0 -- >1
 * 要求只翻转一次，希望翻转之后的矩阵里面的1 的个数最多。 求翻转一次，矩阵里面1
 * 的数量的最大值。
 * 比如矩阵 1 0 0 1 0 0 1 0
 * 可以
 * 翻转 [1, 5] ⇒ 1 1 1 0 1 1 1 0
 * 或者
 * 翻转 [1, 7] ⇒ 1 1 1 0 1 1 0 1
 * 矩阵里面1的个数都是6，
 * 这个是一次翻转之后，矩阵1的个数的最大值。
 * 只用返回这个6就行了。
 *
 */
public class MaxFlipOnes {
    public int maxOneAfterFlip(int[] arry) {
        if (null == arry) return -1;
        int locSum = 0, max = 0, ones = 0;
        for (int i = 0; i < arry.length; i++) {
            ones += arry[i];
            locSum += arry[i] == 0 ? 1 : -1;
            if (locSum > max) {
                max = locSum;
            } else if (locSum < 0) {
                locSum = 0;
            }
        }
        return ones + max;
    }

    public static void main(String[] args) {
        int[] arry = {1, 0, 0, 1, 0, 0, 1, 0};
        MaxFlipOnes maxFlipOnes = new MaxFlipOnes();
        System.out.println(maxFlipOnes.maxOneAfterFlip(arry));
    }
}
