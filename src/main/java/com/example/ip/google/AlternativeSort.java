package com.example.ip.google;

/**
 * Created by benbendaisy on 6/16/15.
 * <p>
 * 对数组排序，使得a1<=a2>=a3<=a4>=... refer to: http://www.mitbbs.com/article_t/JobHunting/32575573.html
 */
public class AlternativeSort {
    public int[] sortArray(int[] s) {
        if (null == s || s.length < 3) return s;
        boolean flag = true;
        int current = s[0];
        for (int i = 0; i < s.length - 1; i++) {
            if ((flag && current > s[i + 1]) || (!flag && current < s[i + 1])) {
                s[i] = s[i + 1];
            } else {
                s[i] = current;
                current = s[i + 1];
            }
            flag = !flag;
        }
        s[s.length - 1] = current;
        return s;
    }

    public void reorder(int[] arr) {
        assert (arr != null);
        if (arr.length == 0) return;
        boolean smallHead = true;
        for (int i = 0; i < arr.length - 1; i++) {
            if (smallHead && arr[i] > arr[i + 1] || !smallHead && arr[i] < arr[i + 1]) {
                int tmp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = tmp;
            }
            smallHead = !smallHead;
        }
    }
}