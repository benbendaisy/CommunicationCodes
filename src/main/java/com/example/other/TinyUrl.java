package com.example.other;

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
    public String shorturl(int id, int base, Map<String, String> map) {
        StringBuilder res = new StringBuilder();
        while (id > 0) {
            int digit = id % base;
            res.append(map.get(digit));
            id /= base;
        }
        while (res.length() < 6) res.append(0);
        return res.reverse().toString();
    }
}
