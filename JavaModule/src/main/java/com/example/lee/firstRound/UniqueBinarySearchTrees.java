package com.example.lee.firstRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 1/5/15.
 *
 * Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
 *
 * For example,
 * Given n = 3, there are a total of 5 unique BST's.
 *
 * 1         3     3      2      1
 *  \       /     /      / \      \
 *   3     2     1      1   3      2
 *  /     /       \                 \
 *  2     1         2                 3
 *
 *  refer to http://blog.sina.com.cn/s/blog_71d59f9a01017irg.html
 */
public class UniqueBinarySearchTrees {

    //recursive + memorization
    public int numTrees(int n) {
        if(n == 0){
            return 0;
        } else if(n == 1){
            return 1;
        }
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        return numTrees(n, map);
    }

    public int numTrees(int n, Map<Integer, Integer> map){
        if(n == 0 || n == 1){
            return 1;
        } else if(map.containsKey(n)){
            return map.get(n);
        }
        int count = 0;
        for(int i = 1; i <= n; i++){
            int left = numTrees(i - 1, map);
            int right = numTrees(n - i, map);
            count += left * right;
        }
        map.put(n, count);
        return count;
    }

    //dp
    public int numTreesI(int n) {
        if(n == 0 || n == 1){
            return 1;
        }

        int dp[] = new int[n + 1];
        dp[0] = 1;
        dp[1] = 1;
        for(int i = 2; i <= n; i++){
            for(int j = 1; j <= i; j++){
                dp[i] += dp[i - j] * dp[j - 1];
            }
        }
        return dp[n];
    }

    //卡塔兰数通项公式 http://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0
    public int numTreesII(int n) {
        if(n == 0 || n == 1){
            return 1;
        }

        int c = 1;
        for(int i = 2; i <= n; i++){
            c = 2 * (2 * i - 1) * c / (i + 1);
        }
        return c;
    }
    public static void main(String[] args) {
        UniqueBinarySearchTrees unique = new UniqueBinarySearchTrees();
        System.out.print(unique.numTrees(2));
    }
}
