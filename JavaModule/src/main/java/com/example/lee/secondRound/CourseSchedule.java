package com.example.lee.secondRound;

import java.util.*;

/**
 * Created by benbendaisy on 5/6/15.
 *
 * There are a total of n courses you have to take, labeled from 0 to n - 1.
 *
 * Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
 *
 * Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
 *
 * For example:
 *
 * 2, [[1,0]]
 * There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.
 *
 * 2, [[1,0],[0,1]]
 * There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 */
public class CourseSchedule {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        if (null == prerequisites || numCourses < 1) return false;
        Map<Integer, Set<Integer>> map = new HashMap<Integer, Set<Integer>>();
        int row = prerequisites.length;
        if (row == 0) return true;
        int col = prerequisites[0].length;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j + 1 < col; j = j + 2) {
                if (prerequisites[i][j] == prerequisites[i][j + 1]) return false;
                if (map.containsKey(prerequisites[i][j])) {
                    map.get(prerequisites[i][j]).add(prerequisites[i][j + 1]);
                } else {
                    Set<Integer> set = new HashSet<Integer>(Arrays.asList(prerequisites[i][j + 1]));
                    map.put(prerequisites[i][j], set);
                }
            }
        }
        if (map.size() == numCourses) return false;
        Set<Integer> iSet = new HashSet<Integer>();
        while (map.size() > 0) {
            int i = 0;
            boolean isFinding = false;
            for (; i < numCourses; i++) {
                if (!map.containsKey(i) && iSet.add(i)) {
                    for(Iterator<Map.Entry<Integer, Set<Integer>>> it = map.entrySet().iterator(); it.hasNext(); ) {
                        Map.Entry<Integer, Set<Integer>> entry = it.next();
                        entry.getValue().remove(i);
                        if(entry.getValue().size() == 0) {
                            it.remove();
                        }
                    }
                    isFinding = true;
                }
            }
            if (!isFinding) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        CourseSchedule courseSchedule = new CourseSchedule();
        int[][] courses = {{0,1},{3,1},{1,3},{3,2}};
        System.out.println(courseSchedule.canFinish(4, courses));
    }
}
