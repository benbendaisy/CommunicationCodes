package com.example.lee.thirdRound;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class RestoreIPAddresses {
    public List<String> restoreIpAddresses(String s) {
        if (s == null || s.length() < 1) {
            return Collections.emptyList();
        }
        List<String> res = new ArrayList<>();
        restoreIpAddressesHelper(s, new StringBuilder(), res, 0);
        return res;
    }

    private void restoreIpAddressesHelper(String str, StringBuilder sb, List<String> list, int addedNum) {
        if (str.length() == 0) {
            if (addedNum == 4) {
                list.add(sb.toString());
            }
            return;
        } else if (str.length() != 0 && addedNum >= 4) {
            return;
        }
        for (int i = 1; i <= str.length() && i < 4; i++) {
            StringBuilder newSb = new StringBuilder(sb);
            String subStr = str.substring(0, i);
            if (subStr.startsWith("0") && subStr.length() > 1) {
                break;
            }
            int num = Integer.parseInt(subStr);
            if (num >= 0 && num <= 255) {
                if (addedNum != 0) {
                    newSb.append(".");
                }
                newSb.append(subStr);
                restoreIpAddressesHelper(str.substring(i), newSb, list, addedNum + 1);
            } else {
                break;
            }
        }
    }

    public static void main(String[] args) {
        RestoreIPAddresses restoreIPAddresses = new RestoreIPAddresses();
        System.out.println(restoreIPAddresses.restoreIpAddresses("0000"));
    }
}
