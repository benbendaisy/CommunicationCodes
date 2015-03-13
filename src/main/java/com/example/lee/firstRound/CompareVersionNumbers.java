package com.example.lee.firstRound;

/**
* Compare two version numbers version1 and version1.
* If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.
* You may assume that the version strings are non-empty and contain only digits and the . character.
* The . character does not represent a decimal point and is used to separate number sequences.
* For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.
* Here is an example of version numbers ordering:
* 0.1 < 1.1 < 1.2 < 13.37
* Created by benbendaisy on 12/19/14.
*/
public class CompareVersionNumbers {
    public int compareVersion(String version1, String version2) {
        if(version1 == null && version2 != null){
            return -1;
        } else if (version1 != null && version2 == null){
            return 1;
        } else if (version1 == null && version2 == null){
            return 0;
        }

        String[] versions1 = version1.split("\\.", -1);
        String[] versions2 = version2.split("\\.", -1);

        int length = versions1.length < versions2.length ? versions1.length : versions2.length;

        for(int i = 0; i < length; i++){
            int result = compareTwoStrings(dealWithZeros(versions1[i]), dealWithZeros(versions2[i]));
            if(result != 0){
                return result;
            }
        }

        if(versions1.length > length){
            for(int i = length; i < versions1.length; i++){
                if(!"0".equals(dealWithZeros(versions1[i]))){
                    return 1;
                }
            }
        }

        if(versions2.length > length){
            for(int i = length; i < versions2.length; i++){
                if(!"0".equals(dealWithZeros(versions2[i]))){
                    return -1;
                }
            }
        }

        return 0;

    }

    private int compareTwoStrings(String str1, String str2){
        if(isEmpty(str1)){
            return isEmpty(str2) ? 0 : -1;
        }

        if(isEmpty(str2)){
            return isEmpty(str1) ? 0 : 1;
        }
        if(str1.length() != str2.length()){
            return str1.length() < str2.length() ? -1 : 1;
        }
        int length = str1.length();

        for(int i = 0; i < length; i++){
            if(str1.charAt(i) < str2.charAt(i)){
                return -1;
            } else if(str1.charAt(i) > str2.charAt(i)){
                return 1;
            }
        }

        return 0;

    }

    private boolean isEmpty(String str){
        return null == str || "".equals(str);
    }

    private String dealWithZeros(String str){
        //deal with 0 that starting and ending with

        Character c = str.charAt(0);
        int index = 0;
        StringBuilder sb = new StringBuilder();
        while(c == '0' && ++index < str.length()){
            c = str.charAt(index);
        }
        for(int i = index; i < str.length(); i++){
            sb.append(str.charAt(i));
        }
        String result = sb.toString();
        if(result.length() == 0){
            return "0";
        } else if(result.charAt(0) == '.') {
            return "0" + result;
        } else {
            return result;
        }
    }

    public static void main(String[] args) {
        CompareVersionNumbers compareVersionNumbers = new CompareVersionNumbers();
        //System.out.println(Long.parseLong("001"));
        //System.out.println(compareVersionNumbers.isEmpty("1"));
        System.out.println(compareVersionNumbers.compareVersion("1.2", "1.10"));
        System.out.println(compareVersionNumbers.compareVersion("1", "1.10"));
        System.out.println(compareVersionNumbers.compareVersion("1.0", "1"));
        System.out.println(compareVersionNumbers.compareVersion("1.0.0", "1"));
    }
}
