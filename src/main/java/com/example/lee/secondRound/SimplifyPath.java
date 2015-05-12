package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 5/11/15.
 */
public class SimplifyPath {
    public String simplifyPath(String path) {
        if (null == path) return null;
        String[] fields = path.split("/", -1);
        List<String> list = new ArrayList<String>();
        for (int i = 0; i < fields.length; i++) {
            switch (fields[i]) {
                case ".":
                case "":    break;
                case "..": if (list.size() > 0) list.remove(list.size() - 1); break;
                default: list.add(fields[i]);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (String str : list) {
            sb.append("/" + str);
        }
        return sb.length() == 0 ? "/" : sb.toString();
    }

    public static void main(String[] args) {
        SimplifyPath sp = new SimplifyPath();
        System.out.println(sp.simplifyPath("/"));
    }
}
