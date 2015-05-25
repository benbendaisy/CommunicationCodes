package com.example.syntax.ThreadLocal;

/**
 * Created by benbendaisy on 5/19/15.
 */
public class BusinessService {
    public void businessMethod() {
        // get the context from thread local
        Context context = MyThreadLocal.get();
        System.out.println(context.getTransactionId());
    }
}
