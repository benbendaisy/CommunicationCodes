package com.example.lee.secondRound;

import com.example.lee.model.Interval;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/26/15.
 */
public class InsertInterval {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        if (null == intervals) return intervals;
        List<Interval> list = new ArrayList<Interval>();
        if (intervals.size() == 0) {
            list.add(newInterval);
            return list;
        }
        boolean isInsert = false;
        boolean inserted = false;
        for (int i = 0; i < intervals.size(); i++) {
            Interval itv = intervals.get(i);
            if (itv.end < newInterval.start) {
                list.add(itv);
            } else if ((itv.start <= newInterval.start && itv.end >= newInterval.start) || (itv.start >= newInterval.start && itv.start <= newInterval.end)) {
                newInterval.start = Math.min(newInterval.start, itv.start);
                newInterval.end = Math.max(newInterval.end, itv.end);
                isInsert = true;
            } else if (isInsert) {
                list.add(newInterval);
                list.add(itv);
                isInsert = false;
                inserted = true;
            } else if (!inserted) {
                list.add(newInterval);
                list.add(itv);
                inserted = true;
            } else {
                list.add(itv);
            }
        }
        if (isInsert || !inserted) list.add(newInterval);
        return list;
    }
}
