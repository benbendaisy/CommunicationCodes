package com.example.syntax;

import com.google.common.collect.MinMaxPriorityQueue;

import java.util.Collections;
import java.util.Iterator;
import java.util.Random;

/**
 * Created by benbendaisy on 5/10/15.
 */
public class PQMinMax {
    static class Data implements Comparable<Data> {
        public int first;
        public int second;
        @Override
        public int compareTo(Data other){
            // for smaller values having higher priority
            if ( this.second > other.second ) return 1;
            else if ( this.second < other.second ) return -1;
            return 0;
        }
    }

    public static void main(String[] args) {

        Random generator = new Random();

        // set the max size to 5
        //MinMaxPriorityQueue<Data> pq = MinMaxPriorityQueue.orderedBy(Collections.reverseOrder()).maximumSize(5).create();
        MinMaxPriorityQueue<Data> pq = MinMaxPriorityQueue.maximumSize(5).create();

        // pq.contains(); // <= certainly, this method is linear time, don't use it!

        System.out.println("adding data:");
        for ( int a = 0; a < 10; a++ ) {
            Data tmp = new Data();
            tmp.first = generator.nextInt() % 1000;
            tmp.second = generator.nextInt() % 1000;
            System.out.println(tmp.first + " " + tmp.second);
            pq.add(tmp);
        }

        System.out.println("all data:");
        Iterator<Data> iter = pq.iterator();
        while (iter.hasNext()) {
            Data tmp = iter.next();
            System.out.println(tmp.first + " " + tmp.second);
        }

        System.out.println("prioritised data:");
        Data tmp = pq.poll();
        while ( tmp != null ) {
            System.out.println(tmp.first + " " + tmp.second);
            tmp = pq.poll();
        }
    }
}
