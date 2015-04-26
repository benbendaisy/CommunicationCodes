package com.example.ip;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

/**
 * Created by pzhong1 on 4/17/15.
 */
public class SpreedSheet {
    /**
     *
     * @param str is a rpn
     * @return
     * @throws IllegalArgumentException
     *
     *
     * evaluate a math expression that is a rpn and contains double and operator
     */
    private double evalueateRpn(String str) throws IllegalArgumentException {
        if (null == str || str.length() < 1) throw new IllegalArgumentException();
        Stack<Double> stack = new Stack<Double>();
        String[] strs = str.split(" ", -1);
        for (int i = 0; i < strs.length; i++) {
            if (isValidDouble(strs[i])) {
                stack.push(Double.parseDouble(strs[i]));
            } else if (isOperator(strs[i])) {
                if (stack.isEmpty()) throw new IllegalArgumentException();
                double b = stack.pop();
                if (stack.isEmpty()) throw new IllegalArgumentException();
                double a = stack.pop();
                double res = execExpression(a, b, strs[i].charAt(0));
                stack.push(res);
            } else {
                throw new IllegalArgumentException();
            }
        }
        if (stack.isEmpty() || stack.size() > 1) throw new IllegalArgumentException();
        return stack.pop();
    }

    /**
     *
     * @param str
     * @return
     *
     *
     * check if the string str is a valid double
     */
    private boolean isValidDouble(String str) {
        try {
            Double.parseDouble(str);
        } catch (NumberFormatException e) {
            //not a double
            return false;
        }
        return true;
    }

    /**
     *
     * @param str
     * @return
     *
     *
     * check if the string str is a valid integer
     */
    private boolean isValidInteger(String str) {
        try {
            Integer.parseInt(str);
        } catch (NumberFormatException e) {
            //not a valid integer
            return false;
        }
        return true;
    }

    /**
     *
     * @param str
     * @return
     *
     *
     * check if string str only contains characters
     */
    private boolean isCharacters(String str) {
        char[] chars = str.trim().toUpperCase().toCharArray();
        for (char ch : chars) {
            if (ch < 'A' || ch > 'Z') return false;
        }
        return true;
    }

    /**
     *
     * @param str
     * @return
     *
     *
     * check if string str is an operator
     */
    private boolean isOperator(String str) {
        if (str.length() > 1) return false;
        char ch = str.charAt(0);
        switch (ch) {
            case '+':
            case '-':
            case '*':
            case '/':
                return true;
        }
        return false;
    }

    /**
     *
     * @param a
     * @param b
     * @param ch
     * @return
     * @throws ArithmeticException
     * @throws IllegalArgumentException
     *
     *
     * excecute the expression
     */
    private double execExpression(double a, double b, char ch) throws ArithmeticException, IllegalArgumentException {
        switch (ch) {
            case '+':
                return a + b;
            case '-':
                return a - b;
            case '*':
                return a * b;
            case '/': {
                //check if b equals 0
                if (b == 0) throw new ArithmeticException();
                return a / b;
            }
        }
        throw new IllegalArgumentException();
    }


    /**
     *
     * @param str
     * @return
     * @throws IllegalArgumentException
     *
     *
     * check if string only contains operators and numbers
     */
    private boolean isNumandOps(String str) throws IllegalArgumentException {
        if (null == str || str.length() < 1) {
            throw new IllegalArgumentException();
        }
        String[] strs = str.split(" ", -1);
        for (String string : strs) {
            if (!isOperator(string) && !isValidDouble(string)) return false;
        }
        return true;
    }

    /**
     *
     * @param res
     * @param str
     * @return
     * @throws IllegalArgumentException
     *
     *
     * get the cell (str) of matrix (res)
     */
    private double getCellValue(double[][] res, String str) throws IllegalArgumentException {
        if (str.length() < 2) throw new IllegalArgumentException();
        int row = str.toUpperCase().charAt(0) - 'A';
        int col = Integer.parseInt(str.substring(1)) - 1;
        if (row >= res.length && col < res[0].length) throw new IllegalArgumentException();
        return res[row][col];
    }

    /**
     *
     * @param metrix
     * @param str
     * @return
     * @throws IllegalArgumentException
     *
     *
     * get the cell (str) of matrix (metrix)
     */
    private String getCellValue(String[][] metrix, String str) throws IllegalArgumentException {
        if (str.length() < 2) throw new IllegalArgumentException();
        int row = str.toUpperCase().charAt(0) - 'A';
        int col = Integer.parseInt(str.substring(1)) - 1;
        if (row >= metrix.length && col < metrix[0].length) throw new IllegalArgumentException();
        return metrix[row][col];
    }

    /**
     *
     * @param res
     * @param str
     * @param val
     * @throws IllegalArgumentException
     *
     *
     * set the cell (str) of matrix res to right value (val)
     */
    private void setCellValue(double[][] res, String str, double val) throws IllegalArgumentException {
        if (str.length() < 2) throw new IllegalArgumentException();
        int row = str.toUpperCase().charAt(0) - 'A';
        int col = Integer.parseInt(str.substring(1)) - 1;
        if (row >= res.length && col < res[0].length) throw new IllegalArgumentException();
        res[row][col] = val;
    }

    /**
     *
     * @param str
     * @return
     *
     *
     * check if cell reference is valid. For example: A2
     */
    private boolean isValidCell(String str) {
        if (str.length() < 2) return false;
        if (str.charAt(0) < 'A' || str.charAt(0) > 'Z') return false;
        if (!isValidInteger(str.substring(1))) {
            return false;
        }
        return true;
    }

    /**
     *
     * @param i
     * @param j
     * @return
     *
     *
     * convert the row and column to a cell string
     */
    private String convertToCell(int i, int j) {
        char ch = (char) ('A' + i);
        return String.format("%s%s", ch, j + 1);
    }

    /**
     *
     * @param exp
     * @param visited
     * @return
     *
     *
     * check if expression that contains cell reference can be calculated
     */
    private boolean canBeCalculated(String exp, Map<String, Double> visited) {
        String[] strs = exp.split(" ", -1);
        for (String str : strs) {
            if (isValidCell(str) && !visited.containsKey(str)) return false;
        }
        return true;
    }

    /**
     *
     * @param exp
     * @param res
     * @return
     *
     *
     * replace right value for cell reference
     */
    private String fillInRightValue(String exp, double[][] res) {
        String[] strs = exp.split(" ", -1);
        for (String str : strs) {
            if (isValidCell(str)) {
                exp = exp.replaceAll(str, String.valueOf(getCellValue(res, str)));
            }
        }
        return exp;
    }

    /**
     *
     * @param metrix
     * @param res
     *
     * Notice: assume there is a valid solution and not consider ther is no solution
     * two steps to handle metrix
     * first step is going to handle a string contains only number and operator
     * second step is going to handle reference
     */
    public void handleMetrix(String[][] metrix, double[][] res) {
        Map<String, Double> visited = new HashMap<String, Double>();

        //to hold unhandled cells
        Queue<String> queue = new LinkedList<String>();

        //first step handles the expression that consists of number and operator only
        for (int i = 0; i < metrix.length; i++) {
            for (int j = 0; j < metrix[0].length; j++) {
                //validate cells
                if (null == metrix[i][j] || metrix[i][j].length() == 0 || "null".equalsIgnoreCase(metrix[i][j].trim()))
                    throw new IllegalArgumentException();
                metrix[i][j] = metrix[i][j].trim().toUpperCase();
                if (isValidDouble(metrix[i][j])) {
                    //copy integer to result
                    res[i][j] = Double.parseDouble(metrix[i][j]);
                    visited.put(convertToCell(i, j), res[i][j]);
                } else if (isNumandOps(metrix[i][j])) {
                    res[i][j] = evalueateRpn(metrix[i][j]);
                    visited.put(convertToCell(i, j), res[i][j]);
                } else {
                    queue.add(convertToCell(i, j));
                }
            }
        }

        //second step handles the reference
        while (!queue.isEmpty()) {
            String str = queue.poll();
            String cell = getCellValue(metrix, str);
            //handle cycle
            Set<String> set = new HashSet<String>();
            set.add(str);
            if (isValidCell(cell)) {
                while (!visited.containsKey(cell) && isValidCell(cell)) {
                    if (!set.add(cell)) throw new IllegalArgumentException();
                    cell = getCellValue(metrix, cell);
                }

                if (visited.containsKey(cell)) {
                    double val = getCellValue(res, cell);
                    setCellValue(res, str, val);
                    visited.put(str, val);
                } else {
                    if (!set.add(cell)) throw new IllegalArgumentException();
                    queue.add(str);
                }
            } else if (canBeCalculated(cell, visited)) {
                cell = fillInRightValue(cell, res);
                double val = evalueateRpn(cell);
                setCellValue(res, str, val);
                visited.put(str, val);
            } else {
                queue.add(str);
            }
        }
    }

    /**
     *
     * @param res
     *
     *
     * left side align
     */
    public void printAll(double[][] res) {
        String[][] mtx = new String[res.length][res[0].length];
        int max = 0;
        for (int i = 0; i < res.length; i++) {
            for (int j = 0; j < res[0].length; j++) {
                mtx[i][j] = String.format("%.5f", res[i][j]);
                max = Math.max(max, mtx[i][j].length());
            }
        }

        //add 5 empty spaces
        max += 5;
        for (int k = 0; k < (max + 1) * res[0].length; k++) {
            System.out.print("-");
        }
        System.out.print("\n");

        for (int i = 0; i < res.length; i++) {
            for (int j = 0; j < res[0].length; j++) {
                int spaceCount = max - mtx[i][j].length();
                for (int k = 0; k < spaceCount; k++) {
                    mtx[i][j] += " ";
                }
                System.out.print(mtx[i][j] + "|");
            }
            System.out.print("\n");
            for (int k = 0; k < (max + 1) * res[0].length; k++) {
                System.out.print("-");
            }
            System.out.print("\n");
        }
    }

    public static void main(String[] args) {
        try {
            System.out.println("Please input in the number of columns and rows");
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
            String input = br.readLine();
            if (null == input) {
                System.out.println("Not a valid number of columns and rows");
            }
            String[] strs = input.split(" ", -1);
            if (strs.length != 2) {
                System.out.println("Not a valid number of columns and rows");
            }
            int m = Integer.parseInt(strs[1]);
            int n = Integer.parseInt(strs[0]);
            if (m > 26) {
                System.out.println("the number of rows can't bigger than 26");
            } else if (m < 1 || n < 1) {
                System.out.println("the number of columns and rows can't be less than 1");
            }
            String[][] metrix = new String[m][n];
            int count = m * n;
            System.out.println(String.format("Please input %s lines valid data", count));
            int row = 0, col = 0;
            while (count > 0 && (input = br.readLine()) != null) {
                metrix[row][col] = input;
                col++;
                if (col >= n) {
                    row++;
                    col = col % n;
                }
                count--;
            }
            double[][] res = new double[m][n];
            SpreedSheet spreedSheet = new SpreedSheet();
            spreedSheet.handleMetrix(metrix, res);
            spreedSheet.printAll(res);
        } catch (Exception ioe) {
            ioe.printStackTrace();
        }
    }
}
