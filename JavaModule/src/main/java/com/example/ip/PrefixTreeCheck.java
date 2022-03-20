package com.example.ip;

/**
 * Created by benbendaisy on 5/9/15.
 */
public class PrefixTreeCheck {
    public boolean check(int[] nodes) {
        return check(nodes, 0, nodes.length, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean check(int[] nodes, int start, int end, int min, int max) {
        if (start >= end) return true;
        int root = nodes[start];
        if (root <= min || root >= max) return false;
        int idx = start + 1;
        while (idx < end && nodes[idx] < root) {
            idx++;
        }
        return check(nodes, start + 1, idx, min, root) && check(nodes, idx, end, root, max);
    }

    public static void main(String[] args) {
        int h = 10, len = 199;
        System.out.println(h & (len - 1));
        System.out.println(hash(h));
        h = Integer.MAX_VALUE;
        System.out.println(h >>> 32);
    }

    private static int hash(int h) {
        h ^= (h >>> 20) ^ (h >>> 12);
        return h ^ (h >>> 7) ^ (h >>> 4);
    }
}
