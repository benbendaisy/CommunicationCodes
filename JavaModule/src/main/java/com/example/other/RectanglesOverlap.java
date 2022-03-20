package com.example.other;

import java.awt.*;

/**
 * Created by benbendaisy on 5/25/15.
 */
public class RectanglesOverlap {
    public static boolean doOverlap(Point l1, Point r1, Point l2, Point r2) {
        //check if one rectangle is left to the other
        if (r1.x < l2.x || r2.x < l1.x) return false;

        // If one rectangle is above other
        if (l1.y < r2.y || r1.y > l2.y) return false;
        return true;
    }

    public static void main(String[] args) {
        Point l1 = new Point(0, 10);
        Point r1 = new Point(10, 0);
        Point l2 = new Point(5, 5);
        Point r2 = new Point(15, 0);
        if (doOverlap(l1, r1, l2, r2))
            System.out.println("Rectangles Overlap");
        else
            System.out.println("Rectangles Don't Overlap");
    }
}
