package com.example.ip;

import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

/**
 * Created by benbendaisy on 4/15/15.
 */
public class PrintTemplatesWithVariants {

    //String str = "{I, Bob, Frank} went to the {airport, movies, beach} last {saturday, sunday} afternoon.";

    //I went to the airport last sunday afternoon.
    //Frank went to the beach last saturday afternoon.

    // "1# went to the 2# last 3# afternoon."
    // Map<1#, Set<String>>

   // "{Henry} went to the {movies, beach, airport}."
   // {Henry, Frank}

    void printStrings(String str) throws Exception{
        if (null == str || str.length() < 2) return;
        Map<String, Set<String>> map = new HashMap<String, Set<String>>();
        int cnt = 0;
        int idx = 0;
        //iniate template string and variants
        String template = "";
        while (idx < str.length()) {
            if (str.charAt(idx) == '{') {
                idx++;
                int lIdx = str.indexOf(idx, '}');
                if (lIdx != -1) {
                    if (lIdx == idx) {
                        idx++;
                        continue;
                    }
                    String subStr = str.substring(idx, lIdx);
                    String[] array = subStr.split(",", -1);
                    Set<String> set = new HashSet<String>();
                    for (String str1 : array) {
                        set.add(str1);
                    }
                    String key = cnt + "#";
                    map.put(key, set); //{0#:{Henry, Frank}}
                    cnt++;
                    idx = lIdx + 1;
                    template += key;
                } else {
                    throw new Exception();
                }
            } else {
                template += str.charAt(idx);
                idx++;
            }
        }

        //{0#:{Henry, Frank}, 1#:{movies, beach, airport}}, template = "0# went to the 1#."
        printStrings(map, 0, template);

    }

    private void printStrings(Map<String, Set<String>> map, int cnt, String template) {
        if (cnt == map.size()) {
            System.out.println(template);
        }
        String key = (cnt + "#");
        Set<String> set = map.get(key);
        for (String str : set) {
            String t = template; //save the original template
            template.replaceAll(key, str);
            printStrings(map, cnt + 1, t);
            //template = t; //retrieve the original template

        }

    }

    public static void main(String[] args) {
        String[] tasks = "  ".split(" ", -1);
        System.out.println(tasks.length);
        System.out.println(VMTest.isValidInteger(""));
    }

}
