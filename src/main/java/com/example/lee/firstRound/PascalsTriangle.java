package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * Created by benbendaisy on 1/1/15.
 * Given numRows, generate the first numRows of Pascal's triangle.
 * For example, given numRows = 5,
 * Return
 * [
 * [1],
 * [1,1],
 * [1,2,1],
 * [1,3,3,1],
 * [1,4,6,4,1]
 * ]
 */
public class PascalsTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> lli = new ArrayList<List<Integer>>();
        if(numRows <= 0){
            return lli;
        }
        List<Integer> li = new ArrayList<Integer>(Arrays.asList(1));
        lli.add(li);
        if(numRows == 1){
            return lli;
        }

        li = new ArrayList<Integer>(Arrays.asList(1, 1));
        lli.add(li);
        if(numRows == 2){
            return lli;
        }

        numRows -= 2;
        while(numRows > 0){
            List<Integer> newLi = new ArrayList<Integer>();
            newLi.add(li.get(0));
            for(int i = 0; i < li.size() - 1; i++){
                newLi.add(li.get(i) + li.get(i+1));
            }
            newLi.add(li.get(li.size() - 1));
            lli.add(newLi);
            li = newLi;
            numRows--;
        }
        return lli;
    }
}

