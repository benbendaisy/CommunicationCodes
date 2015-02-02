package com.example.lee;

import com.example.lee.model.Interval;

import java.util.*;

/**
 * Created by benbendaisy on 1/27/15.
 *
 * Given a collection of intervals, merge all overlapping intervals.
 *
 * For example,
 * Given [1,3],[2,6],[8,10],[15,18],
 * return [1,6],[8,10],[15,18].
 */
public class MergeIntervals {
    public List<Interval> merge(List<Interval> intervals) {
        if(intervals == null || intervals.size() < 2){
            return intervals;
        }
        List<Interval> list = new LinkedList<Interval>();
        Collections.sort(intervals, new IntervalComparator());
        list.add(intervals.get(0));
        ListIterator<Interval> iterator = intervals.listIterator(1);
        while(iterator.hasNext()){
            Interval interval = iterator.next();
            Interval interval1 = list.get(list.size() - 1);
            if((interval.start <= interval1.start && interval.end >= interval1.start)
                    || (interval.start <= interval1.end && interval.end >= interval1.end)
                    || (interval.start <= interval1.start && interval.end >= interval1.end)
                    || (interval.start >= interval1.start && interval.end <= interval1.end)){
                interval1.start = interval1.start < interval.start ? interval1.start : interval.start;
                interval1.end = interval1.end > interval.end ? interval1.end : interval.end;
            } else {
                list.add(interval);
            }
        }

        return list;
    }

    public static void main(String[] args) {
        MergeIntervals mergeIntervals = new MergeIntervals();
        Interval interval = new Interval(1, 4);
        Interval interval1 = new Interval(0, 4);
        List<Interval> li = new ArrayList<Interval>();
        li.add(interval);
        li.add(interval1);
        List<Interval> list = mergeIntervals.merge(li);

        for(Interval interval2 : list){
            System.out.println(interval2.start + ":" + interval2.end);
        }
    }

    private class IntervalComparator implements Comparator<Interval> {
        public int compare(Interval i1, Interval i2) {
            return i1.start < i2.start ? -1 : (i1.start == i2.start ? 0 : 1);
        }
    }
}


