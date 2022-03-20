package com.example.lee.thirdRound;

import java.util.*;
import java.util.stream.Collectors;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class LetterCombinationsofPhoneNumber {
    public List<String> letterCombinations(String digits) {
        if (digits == null || digits.length() == 0) {
            return Collections.emptyList();
        }
        Map<Character, List<String>> keyBoards = new HashMap<>();
        keyBoards.put('2', Arrays.asList("a", "b", "c"));
        keyBoards.put('3', Arrays.asList("d", "e", "f"));
        keyBoards.put('4', Arrays.asList("g", "h", "i"));
        keyBoards.put('5', Arrays.asList("j", "k", "l"));
        keyBoards.put('6', Arrays.asList("m", "n", "o"));
        keyBoards.put('7', Arrays.asList("p", "q", "r", "s"));
        keyBoards.put('8', Arrays.asList("t", "u", "v"));
        keyBoards.put('9', Arrays.asList("w", "x", "y", "z"));
        List<String> results = new ArrayList<>();
        int idx = 0;
        while (!keyBoards.containsKey(digits.charAt(idx))) {
            idx++;
        }
        results.addAll(keyBoards.get(digits.charAt(idx)));
        idx++;
        while (idx < digits.length()) {
            char ch = digits.charAt(idx);
            results = results.stream()
                    .flatMap(str -> {
                        if (!keyBoards.containsKey(ch)) {
                            return null;
                        }
                        return keyBoards.get(ch).stream()
                                .map(string -> str + string)
                                .collect(Collectors.toList()).stream();
                    })
                    .filter(Objects::nonNull)
                    .collect(Collectors.toList());
            idx++;
        }
        return results;
    }
}
