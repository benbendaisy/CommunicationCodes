package com.example.syntax.ThreadLocal;

/**
 * Created by benbendaisy on 5/19/15.
 */
public class MyThreadLocal {
    public static final ThreadLocal userThreadLocal = new ThreadLocal();

    public static void set(Context user) {
        userThreadLocal.set(user);
    }

    public static void unset() {
        userThreadLocal.remove();
    }

    public static Context get() {
        return (Context) userThreadLocal.get();
    }
}
