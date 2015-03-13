package com.example.lee.firstRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/19/15.
 *
 * Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
 *
 * You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
 *
 * Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
 *
 * For the last line of text, it should be left justified and no extra space is inserted between words.
 *
 * For example,
 * words: ["This", "is", "an", "example", "of", "text", "justification."]
 * L: 16.
 *
 * Return the formatted lines as:
 * [
 * "This    is    an",
 * "example  of text",
 * "justification.  "
 * ]
 * Note: Each word is guaranteed not to exceed L in length.
 */
public class TextJustification {
    public List<String> fullJustify(String[] words, int L) {
        List<String> ls = new ArrayList<String>();
        if(words == null || L <= 0){
            ls.add("");
            return ls;
        }
        fullJustify(words, L, 0, ls);
        return ls;
    }

    private void fullJustify(String[] words, int L, int index, List<String> ls) {
        if(index == words.length){
            return;
        }
        int[] array = new int[2];
        boolean isEnd = getLenth(words, L, index, array);
        if(!isEnd){
            int emptyCount = L - array[1];
            int currentWords = array[0] - index + 1;
            StringBuilder sb = new StringBuilder();

            //if line is one word
            if(currentWords == 1){
                sb.append(words[index]);
                for(int i = 0; i <= emptyCount; i++){
                    sb.append(" ");
                }
                ls.add(sb.toString());
                //if there is no space
            } else if(emptyCount < 0){
                for(int i = index; i < array[0]; i++){
                    sb.append(words[i]);
                    sb.append(" ");
                }
                sb.append(words[array[0]]);
                ls.add(sb.toString());
            } else{
                //there is extra space
                int[] space = new int[currentWords - 1];
                //extra space can be split into different words
                if(emptyCount % (currentWords - 1) == 0){
                    int eachSpace = emptyCount / (currentWords - 1);
                    for(int i = 0; i < currentWords - 1; i++){
                        //this is for default empty space
                        space[i] = eachSpace + 1;
                    }
                } else {
                    //extra space cannot be split into different words
                    int eachSpace = emptyCount / (currentWords - 1);
                    int leftSpace = emptyCount - eachSpace * (currentWords - 1);
                    for(int i = 0; i < currentWords - 1; i++){
                        if(leftSpace > 0){
                            space[i] = eachSpace + 2;
                            leftSpace--;
                        } else {
                            space[i] = eachSpace + 1;
                        }
                    }
                }
                for(int i = index; i < array[0]; i++){
                    sb.append(words[i]);
                    for(int j = 0; j < space[i - index]; j++){
                        sb.append(" ");
                    }
                }
                sb.append(words[array[0]]);
                ls.add(sb.toString());
            }
            fullJustify(words, L, array[0] + 1, ls);
        } else {
            //for the last line
            StringBuilder sb = new StringBuilder();
            int current = 0;
            for(int i = index; i < words.length; i++){
                sb.append(words[i]);
                current += words[i].length();
                if(current < L){
                    sb.append(" ");
                    current++;
                }
            }
            for(int i = current; i < L; i++){
                sb.append(" ");
            }
            ls.add(sb.toString());
        }
    }

    private boolean getLenth(String[] words, int L, int index, int[] array){
        int length = 0;
        for(int i = index; i < words.length; i++){
            if(length + words[i].length() <= L){
                length += words[i].length();
                //for empty space after the word
                length++;
            } else {
                array[0] = i - 1;
                //for the last empty space
                array[1] = length - 1;
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        String[] words = {"Here","is","an","example","of","text","justification."};
        TextJustification textJustification = new TextJustification();
        System.out.print(textJustification.fullJustify(words, 14));
    }
}
