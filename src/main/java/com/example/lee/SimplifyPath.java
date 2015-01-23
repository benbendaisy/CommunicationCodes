package com.example.lee;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/14/15.
 *
 * Given an absolute path for a file (Unix-style), simplify it.
 *
 * For example,
 * path = "/home/", => "/home"
 * path = "/a/./b/../../c/", => "/c"
 */
public class SimplifyPath {
    //analyze the path directly
    public String simplifyPath(String path) {
        if(path == null || path.isEmpty()){
            return path;
        }
        int index = 0;
        List<String> ls = new ArrayList<String>();
        String preStr = "";
        while (index < path.length()) {
            String str = getStringBetweenBackSlash(path, index);
            switch (str) {
                case ".":
                case "": break;
                case "..": if(ls.size() > 0) ls.remove(ls.size() - 1); break;
                default: ls.add(str); break;
            }
            index += str.length() + 1;
        }

        StringBuilder sb = new StringBuilder();
        for(String str : ls){
            sb.append("/");
            sb.append(str);
        }
        return sb.length() == 0 ? "/" : sb.toString();
    }

    private String getStringBetweenBackSlash(String path, int index){
        if(index >= path.length()){
            return "";
        } else {
            int idx1 = path.indexOf("/", index);
            if(idx1 != -1 && idx1 < path.length() - 1){
                int idx2 = path.indexOf("/", idx1 + 1);
                if(idx2 != -1){
                    return path.substring(idx1 + 1, idx2);
                } else {
                    return path.substring(idx1 + 1);
                }
            }
        }
        return "";
    }

    //analyze the path by split
    public String simplifyPathI(String path) {
        if(path == null || path.isEmpty()){
            return path;
        }
        int index = 0;
        List<String> ls = new ArrayList<String>();
        String preStr = "";
        String[] fields = path.split("/", -1);
        for(String str : fields){
            switch (str) {
                case ".":
                case "": break;
                case "..": if(ls.size() > 0) ls.remove(ls.size() - 1); break;
                default: ls.add(str); break;
            }
        }

        StringBuilder sb = new StringBuilder();
        for(String str : ls){
            sb.append("/");
            sb.append(str);
        }
        return sb.length() == 0 ? "/" : sb.toString();
    }

    public static void main(String[] args) {
        SimplifyPath simplifyPath = new SimplifyPath();
        System.out.println(simplifyPath.simplifyPathI("/a/./b/../../c/"));
    }
}
