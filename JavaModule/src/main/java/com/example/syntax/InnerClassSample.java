package com.example.syntax;

/**
 * Created by benbendaisy on 5/2/15.
 */
public class InnerClassSample {
    public int x = 0;
    class FirstLevel {
        public int x = 1;
        private int y = 1;
        void methodInFirstLevel(int x) {
            System.out.println("x = " + x);
            System.out.println("this.x = " + this.x);
            System.out.println("InnerClassSample.this.x = " + InnerClassSample.this.x);
        }
    }

    private void printY() {
        FirstLevel externClass = new FirstLevel();
        System.out.println(externClass.y);
    }
    public static void main(String... args) {
        InnerClassSample st = new InnerClassSample();
        InnerClassSample.FirstLevel fl = st.new FirstLevel();
        fl.methodInFirstLevel(23);
        st.printY();
    }
}
