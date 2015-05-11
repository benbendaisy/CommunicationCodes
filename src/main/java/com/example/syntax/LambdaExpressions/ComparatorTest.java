package com.example.syntax.LambdaExpressions;

import com.example.lee.firstRound.SymmetricTree;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

/**
 * Created by benbendaisy on 5/2/15.
 */
public class ComparatorTest {
    static class Person {
        private String givenName;
        private String surName;
        private int age;
        public String getGivenName() {
            return givenName;
        }

        public String getSurName() {
            return surName;
        }

        public int getAge() {
            return age;
        }

        Person(String givenName, String surName, int age) {
            this.givenName = givenName;
            this.surName = surName;
            this.age = age;
        }

        static List<Person> createShortList() {
            List<Person> personList = new ArrayList<Person>();
            personList.add(new Person("tom", "ford", 10));
            personList.add(new Person("tom", "jonathan", 20));
            return personList;
        }

        private void printName() {
            System.out.println("surName: " + surName + ", givenName: " + givenName + ", age: " + age);
        }
    }

    public static void main(String[] args) {
        List<Person> personList = Person.createShortList();

        // Sort with anonymous Class
        Collections.sort(personList, new Comparator<Person>() {
            public int compare(Person p1, Person p2) {
                return p1.getSurName().compareTo(p2.getSurName());
            }
        });
        System.out.println("=== Sorted Asc SurName ===");
        for (Person p : personList) {
            p.printName();
        }

        // Use Lambda instead
        // Print Asc
        System.out.println("=== Sorted Asc SurName ===");
        Collections.sort(personList, (Person p1, Person p2) -> p1.getSurName().compareTo(p2.getSurName()));
        for (Person p : personList) {
            p.printName();
        }

        // Print Desc
        System.out.println("=== Sorted Desc SurName ===");
        Collections.sort(personList, (p1, p2) -> p2.getSurName().compareTo(p1.getSurName()));

        for (Person p : personList) {
            p.printName();
        }
    }
}
