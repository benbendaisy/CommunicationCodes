package com.example.ip.L;

/**
 * Created by benbendaisy on 5/14/15.
 *
 * Question Description: You are to write an abstraction layer for a persistent
 * buffer. Provide an implementation of the following abstract class:
 *
*/

class Location{
    int eIdx; //block index
    int iIdx; //internal block index
    public Location(int eIdx, int iIdx){
        this.eIdx = eIdx;
        this.iIdx = iIdx;
    }
}

public abstract class PBuffer {

    protected final int BLOCK_SIZE = 1024;
    protected final int BLOCK_COUNT = 1024;

    // A sample 1mb buffer, to be allocated in 1k chunks.
    protected byte[] buffer = new byte[BLOCK_COUNT * BLOCK_SIZE];

    public PBuffer() {
        // Reads the buffer from file and dumps the contents into the array,
        // restoring the state to what it was when onShutdown() was called
        //fillBufferFromFile();
    }

    // Returns a Location for a free block of the buffer,
    // suitable for passing to put, get, and free
    public abstract Location allocate();

    // Stores up to BLOCK_SIZE bytes of data in location l.
    // Data beyond BLOCK_SIZE bytes should be truncated
    public abstract void put(Location l, byte[] data);

    // Returns the BLOCK_SIZE bytes of data stored at location l, or null if lis unallocated
    public abstract byte[] get(Location l);

    // Indicates that an area of the buffer is no longer needed, and can bereused
    public abstract void free(Location l);

    // Called on shutdown
    // writes the full contents of the buffer to disk,for reading when later
    // invoked by the constructor
    private void onShutdown() {
        //writeBufferToFile();
    }
}
