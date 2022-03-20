package com.example.dp;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.List;

/**
 * Created by benbendaisy on 5/2/15.
 */
public class WeightedJobScheduling {

    private static class WeightedJob implements Comparable<WeightedJob> {
        int start;
        int end;
        int weight;

        WeightedJob(int start, int end, int weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }

        @Override
        public int compareTo(WeightedJob o) {
            return this.end > o.end ? 1 : (this.end == o.end ? 0 : -1);
        }
    }

    //List<WeightedJob> weightedJobList = new ArrayList<WeightedJob>();
    int latestNonConfliction(List<WeightedJob> weightedJobList, int idx) {
        for (int j = idx - 1; j >= 0; j--) {
            if (weightedJobList.get(j).end <= weightedJobList.get(idx).start) {
                return j;
            }
        }
        return -1;
    }

    int findMaxProfit(List<WeightedJob> weightedJobList) {
        Collections.sort(weightedJobList);
        int len = weightedJobList.size();
        int[] dp = new int[len];
        for (int i = 1; i < len; i++) {
            int locWgt = weightedJobList.get(i).weight;
            int l = latestNonConfliction(weightedJobList, i);
            if (l != -1) locWgt += weightedJobList.get(l).weight;
            dp[i] = Math.max(locWgt, dp[i - 1]);
        }
        return dp[len - 1];
    }

    public static void main(String[] args) {
        WeightedJob job1 = new WeightedJob(3, 10, 20);
        WeightedJob job2 = new WeightedJob(1, 2, 50);
        WeightedJob job3 = new WeightedJob(6, 19, 100);
        WeightedJob job4 = new WeightedJob(2, 100, 200);
        List<WeightedJob> weightedJobList = new ArrayList<WeightedJob>();
        weightedJobList.add(job3);
        weightedJobList.add(job2);
        weightedJobList.add(job1);
        weightedJobList.add(job4);
        WeightedJobScheduling weightedJobScheduling = new WeightedJobScheduling();
        System.out.println(weightedJobScheduling.findMaxProfit(weightedJobList));
//        Collections.sort(weightedJobList);
//        for (WeightedJob job : weightedJobList) {
//            System.out.println(job.start + ":" + job.end + ":" + job.weight);
//        }
    }
}
