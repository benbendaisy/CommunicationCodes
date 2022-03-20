package com.example.ip.L;

import java.util.BitSet;

/**
 * Created by pzhong1 on 5/14/15.
 */
public class PBufferImp extends PBuffer{
    BitSet bitSet = new BitSet(1024);
    @Override
    public Location allocate() {
        return null;
    }

    @Override
    public void put(Location l, byte[] data) {

    }

    @Override
    public byte[] get(Location l) {
        return new byte[0];
    }

    @Override
    public void free(Location l) {

    }
}
