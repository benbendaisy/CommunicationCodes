package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/7/17.
 */
public class MultiplyStrings {
    public String multiply(String num1, String num2) {
        if (num1 == null || num1 == null || num1.length() == 0 || num2.length() == 0) {
            return "";
        } else if ("0".equals(num1) || "0".equals(num2)) {
            return "0";
        }
        int idx1 = num1.length() - 1;
        String res = "0";
        int tens = 0;
        while (idx1 >= 0) {
            int idx2 = num2.length() - 1;
            int carrier = 0;
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < tens; i++) {
                sb.append("0");
            }
            while (idx2 >= 0) {
                int mul = (num1.charAt(idx1) - '0') * (num2.charAt(idx2) - '0') + carrier;
                int rem = mul % 10;
                carrier = mul / 10;
                sb.append(rem);
                idx2--;
            }
            if (carrier != 0) {
                sb.append(carrier);
            }
            res = addTwoStrings(res, sb.reverse().toString());
            idx1--;
            tens++;
        }

        return res;
    }

    private String addTwoStrings(String num1, String num2) {
        int idx1 = num1.length() - 1;
        int idx2 = num2.length() - 1;
        StringBuilder sb = new StringBuilder();
        int carrier = 0;
        while (idx1 >= 0 && idx2 >= 0) {
           int res = (num1.charAt(idx1) - '0') + (num2.charAt(idx2) - '0') + carrier;
           int rem = res % 10;
           sb.append(rem);
           carrier = res / 10;
           idx1--;
           idx2--;
        }
        while (idx1 >= 0) {
           int res = (num1.charAt(idx1) - '0') + carrier;
           int rem = res % 10;
           sb.append(rem);
           carrier = res / 10;
           idx1--;
        }
        while (idx2 >= 0) {
            int res = (num2.charAt(idx2) - '0') + carrier;
            int rem = res % 10;
            sb.append(rem);
            carrier = res / 10;
            idx2--;
        }
        if (carrier != 0) {
            sb.append(carrier);
        }
        return sb.reverse().toString();
    }

    public String multiplyI(String num1, String num2) {
        if (num1 == null || num2 == null || num1.length() == 0 || num2.length() == 0) {
            return "";
        }

        num1 = new StringBuilder(num1).reverse().toString();
        num2 = new StringBuilder(num2).reverse().toString();
        int[] nums = new int[num1.length() + num2.length()];
        for (int i = 0; i < num1.length(); i++) {
            for (int j = 0; j < num2.length(); j++) {
                nums[i + j] += (num1.charAt(i) - '0') * (num2.charAt(j) - '0');
            }
        }
        StringBuilder sb = new StringBuilder();
        int carrier = 0;
        for (int i = 0; i < nums.length; i++) {
            nums[i] += carrier;
            int mod = nums[i] % 10;
            carrier = nums[i] / 10;
            nums[i] = mod;
            sb.insert(0, mod);
        }
        while (sb.charAt(0) == '0' && sb.length() > 1) {
            sb.deleteCharAt(0);
        }
        return sb.toString();
    }
    public static void main(String[] args) {
        MultiplyStrings multiplyStrings = new MultiplyStrings();
        System.out.println(multiplyStrings.multiply("98", "9"));
    }
}
