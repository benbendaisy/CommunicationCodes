package com.example.other;

import java.util.*;

/**
 * Created by benbendaisy on 6/12/15.
 */
public class ListUnionAndIntersect <T> {
    public List<T> union(List<T> list1, List<T> list2) {
        Set<T> set = new HashSet<>();
        set.addAll(list1);
        set.addAll(list2);
        return new ArrayList<>(set);
    }

    public List<T> intersect(List<T> list1, List<T> list2) {
        Set<T> set = new HashSet<>(list1);
        List<T> list = new ArrayList<>();
        Iterator<T> iterator = list2.iterator();
        while (iterator.hasNext()) {
            T t = iterator.next();
            if (set.add(t)) {
                list.add(t);
            }
        }
        return list;
    }
}
