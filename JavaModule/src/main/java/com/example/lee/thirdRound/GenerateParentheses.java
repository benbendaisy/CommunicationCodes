package com.example.lee.thirdRound;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        if (n < 1) {
            return Collections.emptyList();
        }
        List<String> result = Arrays.asList("()");
        while (n > 1)  {
            result = result.stream()
                    .flatMap(str -> IntStream.range(0, str.length())
                                .boxed()
                                .map(idx -> str.substring(0, idx) + "()" + str.substring(idx))
                                .collect(Collectors.toList())
                                .stream())
                    .distinct()
                    .collect(Collectors.toList());
            n--;
        }
        return result;
    }
}
