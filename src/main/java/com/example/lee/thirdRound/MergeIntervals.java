package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

/**
 * Created by benbendaisy on 7/9/17.
 */
public class MergeIntervals {
    private static class Interval {
      int start;
      int end;
      Interval() { start = 0; end = 0; }
      Interval(int s, int e) { start = s; end = e; }
    }

    public List<Interval> merge(List<Interval> intervals) {
        if (intervals == null || intervals.size() < 2) {
            return intervals;
        }
        Comparator<Interval> comparator = (a, b) -> Integer.compare(a.start, b.start);
        intervals.sort(comparator);
        List<Interval> res = new ArrayList<>();
        Interval interval = intervals.get(0);
        for (int i = 1; i < intervals.size(); i++) {
            if (interval.end < intervals.get(i).start) {
                res.add(interval);
                interval = intervals.get(i);
            } else if (interval.end <= intervals.get(i).end) {
                interval.end = intervals.get(i).end;
            }
        }
        if (res.isEmpty() || res.get(res.size() - 1) != interval) {
            res.add(interval);
        }
        return res;
    }
}
