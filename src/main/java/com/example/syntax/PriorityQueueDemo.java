package com.example.syntax;

//import com.google.common.collect.MinMaxPriorityQueue;

import java.util.Collections;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Queue;

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
                if (lhs.equals(rhs)) return 0;
                return -1;
            }
        });

        //MinMaxPriorityQueue pqueue = MinMaxPriorityQueue.maximumSize(5).create();
    }
}
