package com.example.lee;

/**
 * Created by benbendaisy on 12/23/14.
 * There are N children standing in a line. Each child is assigned a rating value.
 * You are giving candies to these children subjected to the following requirements:
 * Each child must have at least one candy.
 * Children with a higher rating get more candies than their neighbors.
 * What is the minimum candies you must give?
 */
public class Candy {

    //We scan the array twice
    public int candy(int[] ratings) {
        if(ratings == null || ratings.length == 0){
            return 0;
        } else if (ratings.length == 1){
            return 1;
        }
        int count = 1;
        int total = 0;
        int len = ratings.length;
        int[] nums = new int[len];

        nums[0] = 1;
        for(int i = 1; i < len; i++){
            if(ratings[i] > ratings[i - 1]){
                nums[i] = nums[i - 1] + 1;
            } else {
                //when two neighbors have equal or less ratings. the second one can be 1
                nums[i] = 1;
            }
        }

        int current = 1;

        //deal with last element
        total += Math.max(nums[len - 1], current);

        for(int i = len - 2; i >= 0; i--){
            if(ratings[i] > ratings[i + 1]){
                current += 1;
            } else {
                current = 1;
            }
            total += Math.max(nums[i], current);
        }
        return total;
    }
}
