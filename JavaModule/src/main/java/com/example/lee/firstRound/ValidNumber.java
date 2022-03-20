package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 1/19/15.
 *
 * Validate if a given string is numeric.
 *
 * Some examples:
 * "0" => true
 * " 0.1 " => true
 * "abc" => false
 * "1 a" => false
 * "2e10" => true
 * Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
 */
public class ValidNumber {
    public boolean isNumber(String s) {
        if (null == s || s.length() == 0) {
            return false;
        }
        int index = 0;
        int len = s.length();
        boolean symble = false;
        boolean point = false;
        boolean e = false;

        char c0 = s.charAt(index);
        //filter out + or -
        if(index < len && (c0 == '+' || c0 == '-')){
            index++;
            if(index < len){
                c0 = s.charAt(index);
            } else {
                return false;
            }
        }

        //filter space if the string does not start with + -
        if(index == 0){
            while(index < len && c0 == ' '){
                index++;
                if(index < len){
                    c0 = s.charAt(index);
                } else {
                    return false;
                }
            }
        }

        //in case string starts as empty space like " -29.3"
        if(index < len && (c0 == '+' || c0 == '-')){
            index++;
            if(index < len){
                c0 = s.charAt(index);
            } else {
                return false;
            }
        }

        //handle the case string ends as e
        if(index < len && (s.substring(index).trim().startsWith("e") || s.substring(index).trim().endsWith("e") || s.substring(index).startsWith(" ") || ".".equals(s.substring(index).trim()))){
            return false;
        }
        s = s.substring(index).trim();
        index = 0;
        len = s.length();

        while (index < len) {
            char ch = s.charAt(index);
            switch (ch) {
                case '0':case '1':case '2':case '3':case '4':
                case '5':case '6':case '7':case '8':case '9': index++; break;
                //check if there is point after e or two points
                case '.': if(point || e){return false;} else {point = true;}; index++; break;
                case 'e': {
                    //check if there is two e in string
                    if(e){
                        return false;
                    } else {
                        e = true;
                    };
                    if(index < len && index < 2 && s.charAt(index - 1) == '.'){
                        return false;
                    }
                    index++;
                    //trying to filter out - or + after e
                    if(index < len){
                        char c = s.charAt(index);
                        if(c == '+' || c == '-'){
                            index++;
                        }
                    }
                    if(index == len){
                        return false;
                    }
                    break;
                }
                default: return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        ValidNumber validNumber = new ValidNumber();
        System.out.println(validNumber.isNumber(" 005047e+6"));
    }
}
