package com.example.other;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 3/17/15.
 *
 * What is tinyurl?
 *
 * tinyurl is a URL service that users enter a long URL and then the service return a shorter and unique url such as "http://tiny.me/5ie0V2".
 *
 * The highlight part can be any string with 6 letters containing [0-9, a-z, A-Z]. That is, 62^6 ~= 56.8 billions unique strings.
 *
 * Basically, we need a Bijective function f(x) = y such that
 * Each x must be associated with one and only one y;
 * Each y must be associated with one and only one x.
 */

//refer to http://n00tc0d3r.blogspot.com/2013/09/big-data-tinyurl.html
//refer to http://stackoverflow.com/questions/742013/how-to-code-a-url-shortener
public class TinyUrl {

    public String shorturl(int id, int base, Map<Integer, Character> map) {
        StringBuilder res = new StringBuilder();
        while (id > 0) {
            int digit = id % base;
            res.append(map.get(digit));
            id /= base;
        }
        while (res.length() < 6) res.append(0);
        return res.reverse().toString();
    }

    public int longurl(String url, int base, Map<Character, Integer> map) {
        if (null == url || url.length() == 0) return 0;
        int res = 0;
        int idx = 0;

        //remove leading '0'
        while (url.charAt(idx) == '0') {
            idx++;
        }
        for (int i = idx; i < url.length(); i++) {
            res = res * base + map.get(url.charAt(i));
        }
        return res;
    }

    public static void main(String[] args) {
        Map<Integer, Character> map = new HashMap<Integer, Character>();
        for (int i = 0; i < 26; i++) {
            map.put(i, (char)('a' + i));
        }
        for (int i = 26; i < 52; i++) {
            map.put(i, (char)('A' + i - 26));
        }
        for (int i = 52; i < 62; i++) {
            map.put(i, (char)(i - 52 + '0'));
        }

        TinyUrl tinyUrl = new TinyUrl();
        System.out.println(tinyUrl.shorturl(123456, 62, map));

        Map<Character, Integer> rMap = new HashMap<Character, Integer>();
        for (Integer it : map.keySet()) {
            rMap.put(map.get(it), it);
        }
        System.out.println(tinyUrl.longurl(tinyUrl.shorturl(123456, 62, map), 62, rMap));
    }
}
