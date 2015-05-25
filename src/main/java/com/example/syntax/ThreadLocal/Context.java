package com.example.syntax.ThreadLocal;

/**
 * Created by benbendaisy on 5/19/15.
 */
public class Context {
    private String transactionId = null;

    public String getTransactionId() {
        return transactionId;
    }

    public void setTransactionId(String transactionId) {
        this.transactionId = transactionId;
    }
}
