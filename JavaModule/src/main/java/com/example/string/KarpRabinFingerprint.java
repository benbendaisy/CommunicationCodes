package com.example.string;

import java.math.BigInteger;
import java.util.Random;

/**
 * Created by benbendaisy on 5/22/15.
 *
 * this is related to rolling hash, which is going to build current hash value
 * based on previous string with o(1) operation
 *
 */
public class KarpRabinFingerprint {
    private static int d = 256;
    private static long q = longRandomPrime();

    public static int search(String p, String t) {
        if (null == p || null == t || p.length() > t.length()) return -1;
        int lenP = p.length(), lenT = t.length();
        long dM = 1, h1 = 0, h2 = 0;
        for (int i = 1; i < lenP; i++) {
            dM = (dM * d) % q;
        }
        h1 = hash(p, lenP);
        h2 = hash(t, lenP);
        if (h1 == h2 && check(p, t, 0)) return 0;
        for (int i = lenP; i < lenT; i++) {
            //removing the hash value of leading character
            h2 = (h2  - dM * t.charAt(i - lenP)) % q;
            //adding the current character
            h2 = (h2 * d + t.charAt(i)) % q;
            if (h1 == h2 && check(p, t, i - lenP + 1)) return i - lenP + 1;
        }
        return -1;
    }

    private static long hash(String key, int m) {
        long h = 0;
        for (int i = 0; i < m; i++) {
            h = (h * d + key.charAt(i)) % q;
        }
        return h;
    }

    private static boolean check(String p, String t, int idx) {
        for (int i = idx; i < p.length(); i++) {
            if (p.charAt(i - idx) != t.charAt(i)) return false;
        }
        return true;
    }

    /** generate a random 31 bit prime **/
    private static long longRandomPrime()
    {
        BigInteger prime = BigInteger.probablePrime(31, new Random());
        return prime.longValue();
    }

    public static void main(String[] args) {
        String p = "abc";
        String t = "geeks ababc";
        System.out.println(search(p, t));
    }
}
