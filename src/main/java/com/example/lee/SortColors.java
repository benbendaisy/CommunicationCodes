package com.example.lee;

/**
 * Created by benbendaisy on 1/14/15.
 * Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
 *
 * Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
 *
 * Note:
 * You are not suppose to use the library's sort function for this problem.
 */
public class SortColors {

    //by three pointer
    public void sortColors(int[] A) {
        if(A == null || A.length < 2){
            return;
        }

        int left = 0, right = A.length - 1;
        while(left < A.length && A[left] == 0){
            left++;
        }
        int mid = left;

        while(mid <= right){
            while(mid < A.length && A[mid] == 1){
                mid++;
            }
            while(right >= 0 && A[right] == 2){
                right--;
            }
            if(mid < A.length && A[mid] == 0){
                swap(A, left, mid);
                left++;
                mid++;
            } else if(mid < right && A[mid] == 2){
                swap(A, mid, right);
                right--;
            }
        }
    }

    private void swap(int[] A, int left, int right){
        if(left < right){
            int temp = A[left];
            A[left] = A[right];
            A[right] = temp;
        }
    }

    //by bucket sorting
    public void sortColorsI(int[] A) {
        if(A == null || A.length < 2){
            return;
        }

        int[] color = new int[3];
        for(int i : A){
            color[i]++;
        }
        for(int i = 0; i < color[0]; i++){
            A[i] = 0;
        }
        for(int i = color[0]; i < color[0] + color[1]; i++){
            A[i] = 1;
        }
        for(int i = color[0] + color[1]; i < A.length; i++){
            A[i] = 2;
        }
    }

    public static void main(String[] args) {
        SortColors sortColors = new SortColors();
        int[] A = {1, 2, 0};
        sortColors.sortColors(A);
        for(int i : A){
            System.out.println(i);
        }
    }
}
