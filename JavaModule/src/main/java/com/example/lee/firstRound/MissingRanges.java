package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 3/14/15.
 *
 * Given a sorted integer array where the range of elements are [0, 99] inclusive, return its missing ranges.
 * For example, given [0, 1, 3, 50, 75], return [“2”, “4->49”, “51->74”, “76->99”]
 */
public class MissingRanges {
    public List<String> findMissingRanges(int[] vals, int start, int end) {
        if (null == vals) {
            return null;
        }
        List<String> list = new ArrayList<String>();
        int l = start - 1, r = 0;
        for (int i = 0; i < vals.length; i++) {
            if (l == vals[i]) {
                l++;
            } else if (vals[i] <= end) {
                r = vals[i] - 1;
                if (l == r) {
                    list.add(getRange(l, r));
                } else {
                    list.add(getRange(l, r));
                }
                //reset
                l = vals[i] + 1;
            }
        }

        if (vals[vals.length - 1] < end) {
            list.add(getRange(vals[vals.length - 1], end));
        }

        return list;
    }

    public List<String> findMissingRangesI(int[] vals, int start, int end) {
        if (null == vals) {
            return null;
        }

        List<String> list = new ArrayList<String>();
        int prev = start;
        for (int i = 0; i < vals.length; i++) {
            if (vals[i] < end) {
                int cur = vals[i] - 1;
                if (cur - prev >= 2) {
                    list.add(getRange(prev, cur));
                }
                prev = vals[i] + 1;
            } else {
                break;
            }
        }
        if (vals[vals.length - 1] < end) {
            list.add(getRange(vals[vals.length - 1], end));
        }
        return list;
    }

    private String getRange(int from, int to) {
        return (from == to) ? String.valueOf(from) : from + "->" + to;
    }
}
