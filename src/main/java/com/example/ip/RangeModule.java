// A Range Module is a module that tracks ranges of numbers.
// Your task is to design and implement an efficient version of
// this module that has less space and time complexity. Yes,
// of course, there can multiple implementations of this, but we
// are not looking at a single one. Make sure you choose the right
// data­structures so that your implementation is efficient.

package com.example.ip;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
import java.util.ListIterator;

public class RangeModule
{
    private List<Range> rangeList = new LinkedList<Range>();
    // AddRange: Given an input range it starts tracking the range.
    // Eg: AddRange(10, 200) – starts tracking range 10 – 200
    // AddRange(150, 180) – starts tracking range 150 – 180.
    // AddRange(250, 500) – starts tracking range 250 – 500.
    // Make sure that you efficiently track overlapping ranges.

    /*
     * need to merge the range if it is overlapped
     */
    public void AddRange(int lower, int upper)
    {
        //check if current range exists
        if (QueryRange(lower, upper)) {
            return;
        }

        //delete the exiting range
        DeleteRange(lower, upper);

        //insert the range
        ListIterator<Range> listIterator = rangeList.listIterator();
        /*
         * sort the range according to ascend order
         *
         * there are four cases:
         * 1, already exists this range (already covered by query range)
         * 2, partialy cover
         * 3, does not cover
         * 4, range list is empty
         *
         */

        while (listIterator.hasNext()) {
            Range currentRange = listIterator.next();
            //find the right place to add
            if (currentRange.getLower() >= lower && currentRange.getLower() <= upper
                    && currentRange.getUpper() >= upper) {
                currentRange.setLower(lower);
                return;
            } else if (currentRange.getLower() <= lower && currentRange.getUpper() >= lower
                    && currentRange.getUpper() <= upper) {
                currentRange.setUpper(upper);
                return;
            } else if (currentRange.getLower() >= upper) {
                Range range = new Range(lower, upper);
                rangeList.add(range);
                return;
            }
        }

        Range range = new Range(lower, upper);
        rangeList.add(range);

    }

    // QueryRange: Given an input range, this returns whether the range
    // is being tracked or not. Eg: QueryRange(50, 100) –
    // Returns TRUE as this is being tracked
    // QueryRange(180, 300) – Returns False as only a partial of this range
    // is being tracked QueryRange(600, 1000) – Returns False as this range is not tracked

    /*
     * as the range is ascendingly sorted when insert, it can be search iteratively
     */

    public boolean QueryRange(int lower, int upper)
    {
        if (rangeList.isEmpty()) {
            return false;
        }
        Iterator<Range> rangeIterator = rangeList.iterator();
        while (rangeIterator.hasNext()) {
            Range range = rangeIterator.next();
            if (range.getLower() <= lower && range.getUpper() >= upper) {
                return true;
            } else if (range.getLower() >= upper) {
                return false;
            }
        }
        return false;
    }

    // DeleteRange: Given input range is untracked after this call has been made.
    // If the range does not exists then it is a no­op.
    // Eg: DeleteRange(50, 150) – stops tracking range 50 – 150
    public void DeleteRange(int lower, int upper)
    {
        if (rangeList.isEmpty()) {
            return;
        }
        ListIterator<Range> rangeListIterator = rangeList.listIterator();
        while (rangeListIterator.hasNext()) {
            Range range = rangeListIterator.next();
            /*
             * there are three cases:
             * 1, delete the current range
             * 2, partially delete the range
             * 3, early terminate
             */
            if (range.getLower() >= lower && range.getUpper() <= upper) {
                rangeListIterator.remove();
            } else if (range.getLower() <= lower && range.getUpper() >= lower &&  range.getUpper() <= upper) {
                range.setUpper(lower);
            } else if (range.getLower() >= lower && range.getLower() <= upper && range.getUpper() >= upper) {
                range.setLower(upper);
            } else if (range.getLower() >= upper) {
                return;
            }
        }
    }

    // You do NOT need to make Range module persistent (writable/readable on disk).

    // In­memory implementation is fine.
    // You do NOT need to submit a test program that uses these APIs . However, feel free
    // to do so if it would be helpful to you in designing or debugging the API.

    // Make sure the work that you submit compiles. It is NOT mandatory that you implement
    // all the interfaces. But make sure that your design and choice of data structure is
    // good enough to implement all interfaces if you had considerably more time.

    // You may use the C standard library, but no other libraries.
    // All source code must be your own.
    // Please strive for:
    // 1. Clean design—Make your code readable and reuseable where possible; give thought
    // to your interface
    // 2. Efficiency—Try to make each functionality as fast as possible
    // 3. Robustness—Handle error sensibly; handle large or unusual sets of words.

    // Please briefly explain your design choices in your comments.


    /*
     * The basic idea is saving range based on lower of range
     * For range insert o(n):
     *
     * 1, check if current range exists o(n)
     * 2, delete exists range o(n)
     * 3, insert current range o(n)
     *
     * for range query o(n):
     * iteratively search the range as range is sorted based on lower of range
     * do some optimization to improve efficiency
     *
     * for range delete() o(n):
     * iteratively delete the range that is fully or partially covered by input
     * do some optimization to early terminate the process of delete
     *
     * To be done (as is not required):
     * implement thread Range Model: introducing synchronized, lock, ReentrantLock
     *
     * using hashmap to save some indexes to achieve o(1) solution. However, it require extra space.
     *
     */

    public void printAll() {
        for (Range range : rangeList) {
            System.out.println(range);
        }
    }

};
