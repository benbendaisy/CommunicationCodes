package com.example.lee;

import java.util.*;

/**
 * Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
 * If the fractional part is repeating, enclose the repeating part in parentheses.
 * For example,
 * Given numerator = 1, denominator = 2, return "0.5".
 * Given numerator = 2, denominator = 1, return "2".
 * Given numerator = 2, denominator = 3, return "0.(6)".
 * Created by benbendaisy on 12/18/14.
 * Implemented it by both recursive and iterative ways
 */
public class FractionToRecurringDecimal {
    public String fractionToDecimal1(int numerator, int denominator) {
        if(denominator == 0){
            return String.valueOf(numerator);
        } else if(numerator == 0){
            return "0";
        }

        long numeratorL = (long) numerator;
        long denominatorL = (long) denominator;
        boolean isNegative = false;

        if(numeratorL < 0){
            isNegative = !isNegative;
            numeratorL = (-1) * numeratorL;
        }

        if(denominatorL < 0){
            isNegative = !isNegative;
            denominatorL = (-1) * denominatorL;
        }

        //check if there is any point
        boolean isInteger = (numeratorL % denominatorL) == 0 ? true : false;
        Map<String, Long> map = new LinkedHashMap<String, Long>();
        long mul = -1, remainer = -1;
        int point = 0;

        //find the location of point, . will be the 2nd place if numerator < denominator
        if(numeratorL > denominatorL){
            long tempDenominator = denominatorL;
            while(numeratorL >= tempDenominator){
                tempDenominator = tempDenominator * 10;
                point++;
            }

            //handle integer part
            mul = numeratorL / denominatorL;
            remainer = numeratorL % denominatorL;
            map.put(mul + ":" + remainer, mul);
            numeratorL = remainer * 10;
        }

        return fractionToDecimalHelper(map, numeratorL, denominatorL, isNegative, isInteger, point);
    }

    public String fractionToDecimalHelper(Map<String, Long> map, long numeratorL, long denominatorL, boolean isNegative, boolean isInteger, int point){
        long mul = -1, remainer = -1;
        if(numeratorL == 0){
            mul = 0l;
            remainer = 0l;
            return formater(map, mul, remainer, isNegative, isInteger, point);
        }
        String key = "";

        if(numeratorL < denominatorL){
            key = "0:" + numeratorL;
            if(!map.containsKey(key)){
                map.put(key, 0l);
                remainer = numeratorL;
                numeratorL = numeratorL * 10;

            } else {
                remainer = numeratorL;
                mul = 0l;
                return formater(map, mul, remainer, isNegative, isInteger, point);
            }
            return fractionToDecimalHelper(map, numeratorL, denominatorL, isNegative, isInteger, point);
        }

        mul = (long) (numeratorL / denominatorL);
        remainer = numeratorL % denominatorL;
        numeratorL = remainer * 10;

        //use multiple and remainer as a key to judge if there is a recycle
        key = mul + ":" + remainer;
        if(!map.containsKey(key)){
            map.put(key, mul);
        } else {
            return formater(map, mul, remainer, isNegative, isInteger, point);
        }
        return fractionToDecimalHelper(map, numeratorL, denominatorL, isNegative, isInteger, point);
    }

    private String formater(Map<String, Long> map, long mul, long remainer, boolean isNegative, boolean isInteger, int point){
        StringBuilder sb = new StringBuilder();
        boolean isRepeating = false;
        //has repeating part
        if(remainer != 0){
            String reKey = mul + ":" + remainer;
            for(String key : map.keySet()){
                if(reKey.equals(key)){
                    if(!isRepeating){
                        sb.append("(");
                        isRepeating = true;
                    }
                    sb.append(map.get(key));
                } else {
                    sb.append(map.get(key));
                }
            }
            if(isRepeating){
                sb.append(")");
            }
        } else {
            for(String key : map.keySet()){
                sb.append(map.get(key));
            }
        }

        if(point > 0 && !isInteger){
            sb.insert(point, ".");
        } else if(!isInteger){
            sb.insert(1, ".");
        }

        String result = "";
        if(isNegative){
            result = "-";
        }

        return result + sb.toString();
    }

    public String fractionToDecimal(int numerator, int denominator) {
        if(denominator == 0){
            return String.valueOf(numerator);
        } else if(numerator == 0){
            return "0";
        }

        long numeratorL = (long) numerator;
        long denominatorL = (long) denominator;
        boolean isNegative = false;

        if(numeratorL < 0){
            isNegative = !isNegative;
            numeratorL = (-1) * numeratorL;
        }

        if(denominatorL < 0){
            isNegative = !isNegative;
            denominatorL = (-1) * denominatorL;
        }

        //check if there is any point
        boolean isInteger = (numeratorL % denominatorL) == 0 ? true : false;
        Map<String, Long> map = new LinkedHashMap<String, Long>();
        long mul = -1, remainer = -1;
        int point = 0;

        //find the location of point, . will be the 2nd place if numerator < denominator
        if(numeratorL > denominatorL){
            long tempDenominator = denominatorL;
            while(numeratorL >= tempDenominator){
                tempDenominator = tempDenominator * 10;
                point++;
            }

            //handle integer part
            mul = numeratorL / denominatorL;
            remainer = numeratorL % denominatorL;
            map.put(mul + ":" + remainer, mul);
            numeratorL = remainer * 10;
        }


        boolean isBreak = false;

        while(numeratorL != 0){

            while(numeratorL < denominatorL){
                String key = "0:" + numeratorL;
                if(!map.containsKey(key)){
                    map.put(key, 0l);
                    numeratorL = numeratorL * 10;
                } else {
                    remainer = numeratorL;
                    mul = 0l;
                    isBreak = true;
                    break;
                }
            }

            if(isBreak){
                break;
            }

            mul = (long) (numeratorL / denominatorL);
            remainer = numeratorL % denominatorL;
            numeratorL = remainer * 10;

            //use multiple and remainer as a key to judge if there is a recycle
            String key = mul + ":" + remainer;
            if(!map.containsKey(key)){
                map.put(key, mul);
            } else {
                break;
            }
        }

        StringBuilder sb = new StringBuilder();
        boolean isRepeating = false;


        //has repeating part
        if(remainer != 0){
            String reKey = mul + ":" + remainer;
            for(String key : map.keySet()){
                if(reKey.equals(key)){
                    if(!isRepeating){
                        sb.append("(");
                        isRepeating = true;
                    }
                    sb.append(map.get(key));
                } else {
                    sb.append(map.get(key));
                }
            }
            if(isRepeating){
                sb.append(")");
            }
        } else {
            for(String key : map.keySet()){
                sb.append(map.get(key));
            }
        }

        if(point > 0 && !isInteger){
            sb.insert(point, ".");
        } else if(!isInteger){
            sb.insert(1, ".");
        }

        String result = "";
        if(isNegative){
            result = "-";
        }

        return result + sb.toString();
    }

    public static void main(String[] args) {
        FractionToRecurringDecimal fractionToRecurringDecimal = new FractionToRecurringDecimal();
//        System.out.println(fractionToRecurringDecimal.fractionToDecimal1(2147483647, 37));
//        System.out.println(fractionToRecurringDecimal.fractionToDecimal1(1, Integer.MIN_VALUE));
//        System.out.println(fractionToRecurringDecimal.fractionToDecimal1(-2147483648, -10));
        System.out.println(fractionToRecurringDecimal.fractionToDecimal1(1, 6));
    }
}
