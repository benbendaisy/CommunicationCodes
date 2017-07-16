package com.example.lee.thirdRound;

import javafx.util.Pair;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.IntStream;

/**
 * Created by benbendaisy on 7/13/17.
 */
public class TextJustification {
    public List<String> fullJustify(String[] words, int maxWidth) {
        if (words == null || words.length == 0 || maxWidth < 0) {
            return Collections.emptyList();
        }

        int idx = 0;
        List<String> res = new ArrayList<>();
        while (idx < words.length) {
            int len = 0;
            int lastWord = idx;
            while (len - 1 <= maxWidth && lastWord < words.length) {
                len += words[lastWord].length() + 1;
                lastWord++;
            }
            // remove last words
            if (len - 1 > maxWidth) {
                lastWord--;
                len = len - words[lastWord].length() - 1;
            }
            StringBuilder sb = new StringBuilder();
            sb.append(words[idx]);
            int addedLen = words[idx].length();
            idx++;
            if (lastWord == words.length) {
                while (idx < lastWord) {
                    sb.append(" ");
                    sb.append(words[idx]);
                    addedLen += words[idx].length() + 1;
                    idx++;
                }
                sb.append(getGivenEmptyString(maxWidth - addedLen));
                res.add(sb.toString());
                return res;
            }

            if (idx < lastWord) {
                int leftEmptySpaces = maxWidth - (len - 1);
                int emptySpace = leftEmptySpaces / (lastWord - idx) + 1;
                int remainingSpace = leftEmptySpaces % (lastWord - idx);
                while (idx < lastWord) {
                    int spaceStr = emptySpace;
                    if (remainingSpace > 0) {
                        spaceStr += 1;
                    }
                    sb.append(getGivenEmptyString(spaceStr));
                    sb.append(words[idx]);
                    addedLen += words[idx].length() + spaceStr;
                    idx++;
                    remainingSpace--;
                }
            }

            sb.append(getGivenEmptyString(maxWidth - addedLen));
            res.add(sb.toString());
        }
        return res;
    }

    private String getGivenEmptyString(int num) {
        StringBuilder stringBuilder = new StringBuilder();
        IntStream.range(0, num).boxed().forEach(i -> stringBuilder.append(" "));
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        TextJustification textJustification = new TextJustification();
        String[] words = {"My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."};
        textJustification.fullJustify(words, 20).stream().forEach(System.out::println);
    }
}
