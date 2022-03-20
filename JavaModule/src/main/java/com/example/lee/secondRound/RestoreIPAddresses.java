package com.example.lee.secondRound;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 4/19/15.
 *
 * Given a string containing only digits, restore it by returning all possible valid IP address combinations.
 *
 * For example:
 * Given "25525511135",
 *
 * return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
 */
public class RestoreIPAddresses {
    public List<String> restoreIpAddresses(String s) {
        List<String> list = new ArrayList<String>();
        if (null == s || s.length() < 4 || s.length() > 12) return list;
        restoreIps(s, list, "", 4);
        return list;
    }

    private void restoreIps(String str, List<String> list, String ip, int level) {
        if (str.length() == 0 && level == 0) {
            list.add(ip.substring(0, ip.length() - 1));
            return;
        } else if (str.length() < level || str.length() == 0 || str.length() > level * 3) {
            return;
        }
        char ch = str.charAt(0);
        if (ch == '0') {
            restoreIps(str.substring(1), list, ip + ch + ".", level - 1);
        } else {
            restoreIps(str.substring(1), list, ip + ch + ".", level - 1);
            if (str.length() > 1) {
                restoreIps(str.substring(2), list, ip + str.substring(0, 2) + ".", level - 1);
                if (str.length() > 2 && ch > '0' && ch < '3') {
                    char c1 = str.charAt(1);
                    char c2 = str.charAt(2);
                    if ((ch == '2' && ((c1 >= '0' && c1 < '5') || (c1 == '5' && c2 >= '0' && c2 < '6'))) || ch == '1') {
                        restoreIps(str.substring(3), list, ip + str.substring(0, 3) + ".", level - 1);
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        RestoreIPAddresses restoreIPAddresses = new RestoreIPAddresses();
        System.out.println(restoreIPAddresses.restoreIpAddresses("172162541"));
    }
}
