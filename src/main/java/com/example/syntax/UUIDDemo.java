package com.example.syntax;

import java.util.HashMap;
import java.util.Map;
import java.util.UUID;

/**
 * Created by pzhong1 on 5/9/15.
 */
public class UUIDDemo {
    public static void main(String[] args) {
        // creating UUID
        UUID uid = UUID.fromString("38400000-8cf0-11bd-b23e-10b96e4ef00d");

        // checking the value of random UUID
        System.out.println("Random UUID value: "+uid.randomUUID());
        String str = "approach";
        System.out.println(getSortedString(str));
    }

    private static String getSortedStringI(String string) {
        Map<Character, Integer> map = new HashMap<>();
        for (char ch : string.toCharArray()) {
            if (map.containsKey(ch)) {
                map.put(ch, map.get(ch) + 1);
            } else {
                map.put(ch, 1);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (char ch : map.keySet()) {
            sb.append(ch);
            sb.append(map.get(ch));
        }
        return sb.toString();
    }

    private static String getSortedString(String string) {

        int[] chars = new int[26];
        for (char ch : string.toLowerCase().toCharArray()) {
            int idx = ch - 'a';
            chars[idx] = chars[idx] + 1;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            if (chars[i] != 0) {
                char ch = (char) (i + 'a');
                sb.append(ch);
                //sb.append(Character.toChars(i + 'a'));
                sb.append(chars[i]);
            }
        }
        return sb.toString();
    }
}
