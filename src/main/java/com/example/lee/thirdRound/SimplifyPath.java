package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

/**
 * Created by benbendaisy on 7/14/17.
 */
public class SimplifyPath {
    public String simplifyPath(String path) {
        if (path == null || path.length() < 1) {
            return path;
        }
        String[] fields = path.split("/", -1);
        int i = 0;
        List<String> list = new ArrayList<>();
        while (i < fields.length) {
            switch (fields[i]) {
                case "..": if (list.size() > 0) {
                    list.remove(list.size() - 1);
                };
                    break;
                case ".":
                case "":
                    break;
                default:
                    list.add(fields[i]);
            }
            i++;
        }
        return "/" + String.join("/", list);
    }

    public static void main(String[] args) {
        SimplifyPath simplifyPath = new SimplifyPath();
        System.out.println(simplifyPath.simplifyPath("/home/"));
        System.out.println(simplifyPath.simplifyPath("/a/./b/../../c/"));
    }
}
