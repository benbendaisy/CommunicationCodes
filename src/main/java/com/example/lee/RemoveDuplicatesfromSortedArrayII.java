package com.example.lee;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Follow up for "Remove Duplicates":
 * What if duplicates are allowed at most twice?
 *
 * For example,
 * Given sorted array A = [1,1,1,2,2,3],
 *
 * Your function should return length = 5, and A is now [1,1,2,2,3].
 */
public class RemoveDuplicatesfromSortedArrayII {
    public int removeDuplicates(int[] A) {
        if(A == null || A.length == 0){
            return 0;
        } else if(A.length <= 2){
            return A.length;
        }
        int currentCount = 1;
        int len = 1;
        int index = 1;
        int currentLen = A.length;
        while(index < currentLen){
            if(A[index] == A[index-1]){
                if(currentCount >= 2){
                    int lIndex = index;
                    while(lIndex < A.length && A[index - 1] == A[lIndex]){
                        for(int j = lIndex; j < A.length - 1; j++){
                            A[j] = A[j + 1];
                        }
                        lIndex++;
                        currentLen--;
                    }

                    //index = lIndex;
                } else {
                    index++;
                    currentCount++;
                    len++;
                }
            } else {
                index++;
                len++;
                currentCount = 1;
            }
        }

        return len;
    }

    public static void main(String[] args) {
        RemoveDuplicatesfromSortedArrayII removeDuplicatesfromSortedArrayII = new RemoveDuplicatesfromSortedArrayII();
        int[] A = {-3,-1,-1,0,0,0,0,0,2};
        System.out.println(removeDuplicatesfromSortedArrayII.removeDuplicates(A));

    }
}
