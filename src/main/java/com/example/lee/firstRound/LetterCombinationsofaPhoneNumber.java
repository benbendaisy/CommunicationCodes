package com.example.lee.firstRound;

import java.util.*;

/**
 * Created by benbendaisy on 3/2/15.
 *
 * Given a digit string, return all possible letter combinations that the number could represent.
 *
 * A mapping of digit to letters (just like on the telephone buttons) is given below.
 */
public class LetterCombinationsofaPhoneNumber {
    public List<String> letterCombinations(String digits) {
        List<String> list = new ArrayList<String>();
        if (null == digits) {
            return list;
        }
        Map<Character, String> map = new HashMap<Character, String>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        for (int i = 0; i < digits.length(); i++) {
            char ch = digits.charAt(i);
            if (map.containsKey(ch)) {
                String mapStr = map.get(ch);
                List<String> newList = new ArrayList<String>();
                if (list.isEmpty()) {
                    for (int j = 0; j < mapStr.length(); j++) {
                        String newStr = "" + mapStr.charAt(j);
                        newList.add(newStr);
                    }
                } else {
                    ListIterator<String> listIterator = list.listIterator();
                    while (listIterator.hasNext()) {
                        String str = listIterator.next();
                        for (int j = 0; j < mapStr.length(); j++) {
                            String newStr = str + mapStr.charAt(j);
                            newList.add(newStr);
                        }
                    }
                }
                if (!newList.isEmpty()) {
                    list.clear();
                    list.addAll(newList);
                }
            }
        }
        return list;
    }

    public List<String> letterCombinationsI(String digits) {
        List<String> list = new ArrayList<String>();
        if (null == digits) {
            return list;
        }
        Map<Character, String> map = new HashMap<Character, String>();
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");
        for (int i = 0; i < digits.length(); i++) {
            char ch = digits.charAt(i);
            if (map.containsKey(ch)) {
                String mapStr = map.get(ch);
                if (list.isEmpty()) {
                    for (int j = 0; j < mapStr.length(); j++) {
                        String newStr = "" + mapStr.charAt(j);
                        list.add(newStr);
                    }
                } else {
                    ListIterator<String> listIterator = list.listIterator();
                    while (listIterator.hasNext()) {
                        String str = listIterator.next();
                        listIterator.remove();
                        for (int j = 0; j < mapStr.length(); j++) {
                            String newStr = str + mapStr.charAt(j);
                            listIterator.add(newStr);
                        }
                    }
                }
            }
        }
        return list;
    }

    public static void main(String[] args) {
        LetterCombinationsofaPhoneNumber letterCombinationsofaPhoneNumber = new LetterCombinationsofaPhoneNumber();
        System.out.println(letterCombinationsofaPhoneNumber.letterCombinations("2"));
    }
}
