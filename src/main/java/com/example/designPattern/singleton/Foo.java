package com.example.designPattern.singleton;

import com.sun.tools.corba.se.idl.toJavaPortable.Helper;

/**
 * Created by pzhong1 on 4/21/15.
 */
public class Foo {
    private Helper helper;
    public Helper getHelper() {
        if (helper == null) {
            synchronized(this) {
                if (helper == null) {
                    helper = new Helper();
                }
            }
        }
        return helper;
    }

    // other functions and members...
}
