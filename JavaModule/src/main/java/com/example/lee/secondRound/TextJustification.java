package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/13/15.
 */
public class TextJustification {
    public List<String> fullJustify(String[] words, int maxWidth) {
        List<String> list = new ArrayList<String>();
        if (null == words || words.length < 1) return list;
        if (maxWidth == 0) {
            list.add("");
            return list;
        }
        int[] idxes = new int[2];
        idxes[0] = 0;
        idxes[1] = -1;
        while (idxes[1] < words.length) {
            int space = getSpaceCnt(words, idxes, maxWidth);
            int len = idxes[1] - idxes[0];
            int spc = len <= 0 ? space : (space / len);
            int lft = space - spc * len;
            String word = "";
            for (int i = idxes[0]; i < idxes[1]; i++) {
                word += words[i] + " ";
                if (idxes[1] != words.length) {
                    //for adding empty space
                    for (int j = 0; j < spc; j++) word += " ";
                    //for extra space
                    if (lft > 0) {
                        word += " ";
                        lft--;
                    }
                }
            }

            if(idxes[1] >= 0 && idxes[1] < words.length) word += words[idxes[1]];

            if (idxes[0] == idxes[1] || idxes[1] == words.length) {
                for (int i = 0; i < space; i++) word += " ";
            }

            list.add(word);
            if (idxes[1] == words.length - 1) return list;
        }
        return list;
    }

    private int getSpaceCnt(String[] words, int[] idxes, int maxL) {
        int st = idxes[1] + 1;
        int len = 0;
        idxes[0] = st;
        for (int i = st; i < words.length; i++) {
            len += words[i].length();
            if (len < maxL) {
                //adding one space
                len++;
            } else if (len == maxL) {
                //adding exact words
                idxes[1] = i;
                return 0;
            } else {
                //adding too much words
                len = len - words[i].length() - 1;
                idxes[1] = i - 1;
                return maxL - len;
            }
        }
        idxes[1] = words.length;
        return maxL - len;
    }

    public static void main(String[] args) {
        TextJustification tjf = new TextJustification();
        //String[] words = {"a","b","c","d","e"};
        //String[] words = {""};
        String[] words = {"Here","is","an","example","of","text","justification."};
        System.out.println(tjf.fullJustify(words, 14));
    }
}
