package com.example.ip;

/**
 * Created by benbendaisy on 3/21/15.
 *
 * introduce a Range class to hold lower and upper of range
 * At same time, override hashcode and equals to get unified results
 */


public class Range {
    private int lower;
    private int upper;
    public Range(int lower, int upper) {
        this.lower = lower;
        this.upper = upper;
    }

    public int getLower() {
        return lower;
    }

    public void setLower(int lower) {
        this.lower = lower;
    }

    public int getUpper() {
        return upper;
    }

    public void setUpper(int upper) {
        this.upper = upper;
    }

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 31 * hash + lower;
        hash = 31 * hash + upper;
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if(this == obj)
            return true;
        if((obj == null) || (obj.getClass() != this.getClass()))
            return false;
        Range range = (Range) obj;
        return lower == range.lower && upper == range.upper;
    }

    @Override
    public String toString() {
        return String.format("lower: %s, upper: %s", lower, upper);
    }
}
