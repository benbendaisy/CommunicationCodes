package com.example.syntax.LambdaExpressions;

import java.util.List;

/**
 * Created by benbendaisy on 5/2/15.
 */
public class RoboContactMethods {
    public void callDrivers(List<ComparatorTest.Person> pl) {
        for (ComparatorTest.Person p : pl) {
            if (p.getAge() >= 16) {
                roboCall(p);
            }
        }
    }

    public void roboCall(ComparatorTest.Person p) {
        System.out.println("Calling " + p.getGivenName() + " " + p.getSurName() + " age " + p.getAge());
    }
}

