package com.example.syntax;

//import com.google.common.collect.MinMaxPriorityQueue;

import java.util.*;

/**
 * Created by benbendaisy on 5/10/15.
 */
public class PriorityQueueDemo {
    public static void main(String[] args) {
        Queue<Integer> queue = new PriorityQueue<Integer>(4, Collections.reverseOrder());
        for (int i = 0; i < 10; i++) {
            queue.add(i);
        }
        while (!queue.isEmpty()) {
            int i = queue.poll();
            System.out.println(i);
        }

        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(10, new Comparator<Integer>() {
            @Override
            public int compare(Integer lhs, Integer rhs) {
                if (lhs > rhs) return 1;
                if (lhs == rhs) return 0;
                return -1;
            }
        });

        Map<Integer, Integer> map = new LinkedHashMap<Integer, Integer>();
        map.put(1, 1);
        map.put(3, 3);
        map.put(2, 2);
        Set<Integer> set = map.keySet();

        for (int i : set) {
            System.out.println(i);
        }

        //MinMaxPriorityQueue pqueue = MinMaxPriorityQueue.maximumSize(5).create();
    }
}
