package com.example.designPattern.singleton;

//import com.sun.tools.corba.se.idl.toJavaPortable.Helper;

/**
 * Created by benbendaisy on 4/21/15.
 */
public class Foo {
    private Foo helper;
    public Foo getHelper() {
        if (helper == null) {
            synchronized(this) {
                if (helper == null) {
                    helper = new Foo();
                }
            }
        }
        return helper;
    }

    // other functions and members...
}
