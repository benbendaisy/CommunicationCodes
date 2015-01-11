package com.example.lee;

import java.util.ArrayList;
import java.util.List;

/**
 * Created by benbendaisy on 1/8/15.
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
        if(s == null || s.isEmpty()){
            return list;
        }
        restoreIpAddresses(s, "", list, 4);
        return list;
    }

    private void restoreIpAddresses(String s, String ip, List<String> list, int level){
        //check if it is a valid split
        if(s.isEmpty() && level == 0){
            list.add(ip);
            return;
        } else if(level == 0){
            return;
        }
        int len = s.length();

        //check if the string still valid
        if(len > level * 3){
            return;
        }
        for(int i = 1; i <= len; i++){
            String str = s.substring(0, i);

            //make sure it is a valid number
            if(s.substring(0, i).startsWith("00") || (str.length() > 1 && str.startsWith("0"))){
                return;
            }

            int newIp = Integer.parseInt(str);
            //check if it is in a valid range
            if(newIp <= 255 && newIp >= 0){
                if(ip.isEmpty()){
                    restoreIpAddresses(s.substring(i), ip + newIp, list, level - 1);
                } else {
                    restoreIpAddresses(s.substring(i), ip + "." + newIp, list, level - 1);
                }
            } else {
                return;
            }
        }
    }

    public static void main(String[] args) {
        RestoreIPAddresses rip = new RestoreIPAddresses();
        System.out.println(rip.restoreIpAddresses("010010"));
    }
}
