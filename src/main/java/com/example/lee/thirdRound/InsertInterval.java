package com.example.lee.thirdRound;

import com.example.lee.model.Interval;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 7/9/17.
 */
public class InsertInterval {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        if (intervals == null) {
            if (newInterval != null) {
                return Arrays.asList(newInterval);
            }
        }
        List<Interval> res = new ArrayList<>();
        for (int i = 0; i < intervals.size(); i++) {
            Interval cur = intervals.get(i);
            if (cur.end < newInterval.start) {
                res.add(cur);
            } else if (cur.start <= newInterval.start && newInterval.start <= cur.end && newInterval.end >= cur.end) {
                newInterval.start = cur.start;
            } else if (cur.start >= newInterval.start && cur.start <= newInterval.end && newInterval.end <= cur.end) {
                newInterval.end = cur.end;
            } else if (cur.start < newInterval.start && cur.end > newInterval.end) {
                newInterval = cur;
            } else if (cur.start > newInterval.end) {
                res.add(newInterval);
                newInterval = cur;
            }
        }

        if (res.isEmpty() || res.get(res.size() - 1).end < newInterval.start) {
            res.add(newInterval);
        }
        return res;
    }
}
