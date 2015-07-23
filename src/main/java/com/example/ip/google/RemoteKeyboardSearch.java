package com.example.ip.google;

/**
 * Created by benbendaisy on 7/22/15.
 * <p>
 * 题目：像apple tv，chrome tv之类的，用户可以搜索电影名字，但只能用remote在一
 * 个虚拟的keyboard上搜索，只能在虚拟键盘上下左右移动。现在给定键盘如下：
 * <p>
 * a  b  c  d  e
 * f  g  h  i  j
 * k  l  m  n  o
 * p  q  r  s  t
 * u  v  w  x  y
 * z
 * <p>
 * 如果用户要搜索电影名字为 cars，那么需要先往右走两步到c，输入enter，再往左走
 * 两步到a，输入enter，再往下走3步往右走2步到r，输入enter，再往右走一步到s，输
 * 入enter。现在规定L，R，U，D分部代表左，右，上，下移动一步，！代表输入enter，
 * 那么用户动作可以表示成 RR!LL!DDDRR!R!
 * <p>
 * 要求写一个函数，输入为一个string代表电影名字，输出为一个string代表用户的动作。
 */
public class RemoteKeyboardSearch {
    public static String boardMove(String s, char c, int n) {
        StringBuilder res = new StringBuilder();
        for (int i = 0; i < s.length(); ++i) {
            move(c, s.charAt(i), n, res);
            c = s.charAt(i);
        }
        return res.toString();
    }

    static void move(char c1, char c2, int n, StringBuilder res) {
        int a = c1 - 'a', b = c2 - 'a';
        int x1 = a / n, x2 = b / n, y1 = a % n, y2 = b % n;
        int dx = Math.abs(x1 - x2), dy = Math.abs(y1 - y2);
        char v = x1 < x2 ? 'D' : 'U';
        char h = y1 < y2 ? 'R' : 'L';
        for (int i = 0; i < dy; ++i)
            res.append(h);
        for (int i = 0; i < dx; ++i)
            res.append(v);
        res.append('!');
    }

    public static void main(String[] args) {
        System.out.println(boardMove("cars", 'a', 5));
    }
}
