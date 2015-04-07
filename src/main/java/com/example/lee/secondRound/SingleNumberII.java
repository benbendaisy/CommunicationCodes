package com.example.lee.secondRound;

import java.util.LinkedHashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 4/4/15.
 */
public class SingleNumberII {
    public int singleNumber(int[] A) {
        if (null == A) {
            return 0;
        } else if (A.length < 3) {
            return A[0];
        }
        int res = 0;
        for (int i = 31; i >= 0; i--) {
            int cnt = 0;
            for (int j = 0; j < A.length; j++) {
                if ((A[j] >> i & 1) == 1) cnt++;
            }
            cnt = cnt % 3;
            res = res << 1;
            res |= cnt;
        }
        return res;
    }

    public int singleNumberI(int[] A) {
        if (null == A) {
            return 0;
        } else if (A.length < 3) {
            return A[0];
        }
        Map<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();
        for (int i : A) {
            if (map.containsKey(i)) {
                map.put(i, map.get(i) + 1);
            } else {
                map.put(i, 1);
            }
        }

        for (int i : map.keySet()) {
            if (map.get(i) != 3) return i;
        }
        return 0;
    }

}
