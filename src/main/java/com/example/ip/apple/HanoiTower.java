package com.example.ip.apple;

/**
 * Created by benbendaisy on 6/3/15.
 */
public class HanoiTower {
    public void hanoi(int n, String start, String hanOver, String end) {
        if (n == 1) {
            System.out.println("moving one from " + start + " to " + end);
        } else {
            hanoi(n - 1, start, end, hanOver);
            System.out.println("moving one from " + start + " to " + end);
            hanoi(n - 1, hanOver, start, end);
        }
    }

    public static void main(String[] args) {
        HanoiTower hanoiTower = new HanoiTower();
        hanoiTower.hanoi(5, "start", "hanOver", "end");
    }
}
