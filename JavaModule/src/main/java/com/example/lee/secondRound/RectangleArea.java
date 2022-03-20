package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 6/9/15.
 *
 * Find the total area covered by two rectilinear rectangles in a 2D plane.
 *
 * Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
 *
 * Rectangle Area
 * Assume that the total area is never beyond the maximum possible value of int.
 *
 */
public class RectangleArea {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int areaA = (C-A)*(D-B);
        int areaB = (G-E)*(H-F);
        if (!overlap(A, B, C, D, E, F, G, H)) return areaA + areaB;
        int leftBar = E < A ? A : E;
        int rightBar = G > C ? C : G;
        int overLapWidth = rightBar-leftBar;
        int downBar = F < B ? B : F;
        int upBar = H > D ? D : H;
        int overLapHeight = upBar - downBar;
        return areaA -overLapHeight*overLapWidth + areaB;

    }

    private boolean overlap(int A, int B, int C, int D, int E, int F, int G, int H) {
        if (A > G || E > C) return false;
        if (H < B || F > D) return false;
        return true;
    }

    public static void main(String[] args) {
        RectangleArea area = new RectangleArea();
        System.out.println(area.computeArea(-2, -2, 2, 2, -2, -2, 2, 2));
    }
}
