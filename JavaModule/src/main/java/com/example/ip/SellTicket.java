package com.example.ip;

import java.util.*;

/**
 * Created by benbendaisy on 4/30/15.
 */
public class SellTicket {
    public int sellTicket(int[] arrs, int m) {
        if (null == arrs || arrs.length == 0) return 0;
        Queue<Integer> queue = new PriorityQueue<Integer>(m, Collections.reverseOrder());
        for (int i : arrs) {
            queue.add(i);
        }
        int res = 0;
        while (!queue.isEmpty() && m > 0) {
            int t = queue.poll();
            if (t > 0) queue.add(t - 1);
            res += t;
            m--;
        }
        return res;
    }

    public static void main(String[] args) {
        int[] arrs = {2, 5};
        SellTicket sellTicket = new SellTicket();
        System.out.println(sellTicket.sellTicket(arrs, 4));

        //heap pollution example refer to http://www.angelikalanger.com/GenericsFAQ/FAQSections/TechnicalDetails.html#FAQ050
        List ln = new ArrayList<Number>();
        List<String> ls = ln;  // unchecked warning
        ln.add(1);
        String s = ls.get(0); // ClassCastException
    }
}
