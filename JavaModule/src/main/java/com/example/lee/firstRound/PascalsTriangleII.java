package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 1/1/15.
 * Given an index k, return the kth row of the Pascal's triangle.
 * For example, given k = 3,
 * Return [1,3,3,1].
 * Note:
 * Could you optimize your algorithm to use only O(k) extra space?
 */
public class PascalsTriangleII {

    //get the result by dp
    public List<Integer> getRow(int rowIndex) {
        List<Integer> li = new ArrayList<Integer>();
        if(rowIndex < 0){
            return li;
        }
        li = new ArrayList<Integer>(Arrays.asList(1));
        if(rowIndex == 0){
            return li;
        }

        li = new ArrayList<Integer>(Arrays.asList(1, 1));
        if(rowIndex == 1){
            return li;
        }

        rowIndex--;
        for(int i = 0; i < rowIndex; i++){
            for(int j = li.size() - 1; j > 0; j--){
                li.set(j, li.get(j-1) + li.get(j));
            }
            li.add(1);
        }
        return li;
    }

    //get result by using extra space
    public List<Integer> getRowI(int rowIndex) {
        List<Integer> li = new ArrayList<Integer>();
        if(rowIndex < 0){
            return li;
        }
        li = new ArrayList<Integer>(Arrays.asList(1));
        if(rowIndex == 0){
            return li;
        }

        li = new ArrayList<Integer>(Arrays.asList(1, 1));
        if(rowIndex == 1){
            return li;
        }

        rowIndex--;
        while(rowIndex > 0){
            List<Integer> newLi = new ArrayList<Integer>();
            newLi.add(li.get(0));
            for(int i = 0; i < li.size() - 1; i++){
                newLi.add(li.get(i) + li.get(i+1));
            }
            newLi.add(li.get(li.size() - 1));
            li = newLi;
            rowIndex--;
        }
        return li;
    }
}
