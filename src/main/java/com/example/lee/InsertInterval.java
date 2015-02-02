package com.example.lee;

import com.example.lee.model.Interval;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/**
 * Created by benbendaisy on 1/23/15.
 *
 * Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
 *
 * You may assume that the intervals were initially sorted according to their start times.
 *
 * Example 1:
 * Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
 *
 * Example 2:
 * Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].
 *
 * This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
 */
public class InsertInterval {
    public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
        if(intervals == null || newInterval == null){
            return intervals;
        }

        Iterator<Interval> iterator = intervals.iterator();
        int index = 0;
        while(iterator.hasNext()){
            Interval interval = iterator.next();
            if((interval.start <= newInterval.end && interval.start >= newInterval.start) || (interval.end >= newInterval.start && interval.end <= newInterval.end)
                    || (interval.start <= newInterval.start && interval.end >= newInterval.end)
                    || (interval.start >= newInterval.start && interval.end <= newInterval.end)){
                newInterval.start = newInterval.start < interval.start ? newInterval.start : interval.start;
                newInterval.end = newInterval.end > interval.end ? newInterval.end : interval.end;
                iterator.remove();
            }
        }

        int len = intervals.size();
        boolean inserted = false;
        for(int i = 0; i < len; i++){
            if(intervals.get(i).start > newInterval.start){
                intervals.add(i, newInterval);
                inserted = true;
                break;
            }
        }

        if(!inserted){
            intervals.add(newInterval);
        }

        return intervals;
    }

    public static void main(String[] args) {
        InsertInterval insertInterval = new InsertInterval();
        Interval interval = new Interval(1, 5);
        Interval interval1 = new Interval(2, 3);
        List<Interval> list = new ArrayList<Interval>();
        list.add(interval);
        //list.add(interval1);
        insertInterval.insert(list, interval1);
        for(Interval interval2 : list){
            System.out.println(interval2.start + ":" + interval2.end);
        }
    }
}
