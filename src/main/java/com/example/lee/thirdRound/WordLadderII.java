package com.example.lee.thirdRound;

import java.util.*;

/**
 * both two methods passed leetcode although it bothered me long time ago
 * the key point is that do remove all visited words from dict when each level is complete
 */
public class WordLadderII {

    public List<List<String>> findLadders(String beginWord, String endWord, List<String> wordList) {
        if (beginWord == null || endWord == null
                || beginWord.length() != endWord.length()
                || beginWord.equals(endWord) || !wordList.contains(endWord)) {
            return Collections.emptyList();
        }
        Queue<String> queue = new LinkedList<>();
        queue.add(beginWord);
        queue.add(null);
        Map<String, Set<String>> cached = new HashMap<>();
        Set<String> visited = new HashSet<String>();
        Set<String> unvisited = new HashSet<String>();
        unvisited.addAll(wordList);
        int level = 1;
        boolean isEnd = false;
        while (!queue.isEmpty()) {
            if (queue.peek() == null) {
                if (isEnd) {
                    List<List<String>> res = new ArrayList<>();
                    getLadders(cached, beginWord, endWord, level, new ArrayList<>(), res);
                    return res;
                }
                queue.poll();
                if (queue.isEmpty()) {
                    return Collections.emptyList();
                }
                unvisited.removeAll(visited);
                visited = new HashSet<>();
                level++;
                queue.add(null);
            }
            String str = queue.poll();
            for (int i = 0; i < str.length(); i++) {
                char[] words = str.toCharArray();
                char ch = str.charAt(i);
                for (char j = 'a'; j <= 'z'; j++) {
                    if (ch != j) {
                        words[i] = j;
                        String temp = new String(words);
                        if (unvisited.contains(temp)) {
                            queue.add(temp);
                            Set<String> prevSet = cached.getOrDefault(temp, new HashSet<>());
                            prevSet.add(str);
                            cached.put(temp, prevSet);
                            visited.add(temp);
                            if (endWord.equals(temp)) {
                                isEnd = true;
                            }
                        }
                    }
                }
                words[i] = ch;
            }
        }
        return Collections.emptyList();
    }

    private void getLadders(Map<String, Set<String>> cached,
                                          String startWord, String endWord, int level,
                                          List<String> candidateList, List<List<String>> res) {
        candidateList.add(0, endWord);
         if (level < 0) {
             return;
         } else if (startWord.equals(endWord)) {
             res.add(new ArrayList<>(candidateList));
             return;
         } else if (!cached.containsKey(endWord)) {
             return;
         }
         for (String prevStr : cached.get(endWord)) {
             getLadders(cached, startWord, prevStr,
                     level - 1, new ArrayList<>(candidateList), res);
         }
    }

    public List<List<String>> findLaddersI(String beginWord, String endWord, List<String> wordList) {
        if (beginWord == null || endWord == null
                || beginWord.length() != endWord.length() || beginWord.equals(endWord) || !wordList.contains(endWord)) {
            return Collections.emptyList();
        }
        Queue<String> queue = new LinkedList<>();
        Queue<List<String>> listQueue = new LinkedList<>();
        queue.add(beginWord);
        queue.add(null);
        listQueue.add(Arrays.asList(beginWord));
        listQueue.add(null);
        List<List<String>> res = new ArrayList<>();
        Set<String> visited = new HashSet<String>();
        Set<String> unvisited = new HashSet<String>();
        unvisited.addAll(wordList);
        String str = null;
        boolean isEnd = false;
        while (!queue.isEmpty()) {
            if (queue.peek() == null) {
                if (isEnd) {
                    return res;
                }
                queue.poll();
                listQueue.poll();
                if (queue.isEmpty()) {
                    return res;
                }
                queue.add(null);
                listQueue.add(null);
                unvisited.removeAll(visited);
                visited = new HashSet<>();
            }
            str = queue.poll();
            List<String> list = listQueue.poll();
            char[] words = str.toCharArray();
            for (int i = 0; i < str.length(); i++) {
                char ch = str.charAt(i);
                for (char j = 'a'; j <= 'z'; j++) {
                    if (ch == j) {
                        continue;
                    }
                    words[i] = j;
                    String temp = new String(words);
                    if (unvisited.contains(temp)) {
                        List<String> newList = new ArrayList<>(list);
                        newList.add(temp);
                        if (endWord.equals(temp)) {
                            isEnd = true;
                            res.add(newList);
                        } else {
                            queue.add(temp);
                            listQueue.add(newList);
                        }
                        visited.add(temp);
                    }
                    words[i] = ch;
                }
            }
        }
        return Collections.emptyList();
    }

    public static void main(String[] args) {
        WordLadderII wordLadderII = new WordLadderII();
        List<String> wordList = Arrays.asList("kid","tag","pup","ail","tun","woo",
                "erg","luz","brr","gay","sip","kay","per","val","mes","ohs","now",
                "boa","cet","pal","bar","die","war","hay","eco","pub","lob","rue",
                "fry","lit","rex","jan","cot","bid","ali","pay","col","gum","ger",
                "row","won","dan","rum","fad","tut","sag","yip","sui","ark","has",
                "zip","fez","own","ump","dis","ads","max","jaw","out","btu","ana",
                "gap","cry","led","abe","box","ore","pig","fie","toy","fat","cal",
                "lie","noh","sew","ono","tam","flu","mgm","ply","awe","pry","tit",
                "tie","yet","too","tax","jim","san","pan","map","ski","ova","wed",
                "non","wac","nut","why","bye","lye","oct","old","fin","feb","chi",
                "sap","owl","log","tod","dot","bow","fob","for","joe","ivy","fan",
                "age","fax","hip","jib","mel","hus","sob","ifs","tab","ara","dab",
                "jag","jar","arm","lot","tom","sax","tex","yum","pei","wen","wry",
                "ire","irk","far","mew","wit","doe","gas","rte","ian","pot","ask",
                "wag","hag","amy","nag","ron","soy","gin","don","tug","fay","vic",
                "boo","nam","ave","buy","sop","but","orb","fen","paw","his","sub",
                "bob","yea","oft","inn","rod","yam","pew","web","hod","hun","gyp",
                "wei","wis","rob","gad","pie","mon","dog","bib","rub","ere","dig",
                "era","cat","fox","bee","mod","day","apr","vie","nev","jam","pam",
                "new","aye","ani","and","ibm","yap","can","pyx","tar","kin","fog",
                "hum","pip","cup","dye","lyx","jog","nun","par","wan","fey","bus",
                "oak","bad","ats","set","qom","vat","eat","pus","rev","axe","ion",
                "six","ila","lao","mom","mas","pro","few","opt","poe","art","ash",
                "oar","cap","lop","may","shy","rid","bat","sum","rim","fee","bmw",
                "sky","maj","hue","thy","ava","rap","den","fla","auk","cox","ibo",
                "hey","saw","vim","sec","ltd","you","its","tat","dew","eva","tog",
                "ram","let","see","zit","maw","nix","ate","gig","rep","owe","ind",
                "hog","eve","sam","zoo","any","dow","cod","bed","vet","ham","sis",
                "hex","via","fir","nod","mao","aug","mum","hoe","bah","hal","keg",
                "hew","zed","tow","gog","ass","dem","who","bet","gos","son","ear",
                "spy","kit","boy","due","sen","oaf","mix","hep","fur","ada","bin",
                "nil","mia","ewe","hit","fix","sad","rib","eye","hop","haw","wax",
                "mid","tad","ken","wad","rye","pap","bog","gut","ito","woe","our",
                "ado","sin","mad","ray","hon","roy","dip","hen","iva","lug","asp",
                "hui","yak","bay","poi","yep","bun","try","lad","elm","nat","wyo",
                "gym","dug","toe","dee","wig","sly","rip","geo","cog","pas","zen",
                "odd","nan","lay","pod","fit","hem","joy","bum","rio","yon","dec",
                "leg","put","sue","dim","pet","yaw","nub","bit","bur","sid","sun",
                "oil","red","doc","moe","caw","eel","dix","cub","end","gem","off",
                "yew","hug","pop","tub","sgt","lid","pun","ton","sol","din","yup",
                "jab","pea","bug","gag","mil","jig","hub","low","did","tin","get",
                "gte","sox","lei","mig","fig","lon","use","ban","flo","nov","jut",
                "bag","mir","sty","lap","two","ins","con","ant","net","tux","ode",
                "stu","mug","cad","nap","gun","fop","tot","sow","sal","sic","ted",
                "wot","del","imp","cob","way","ann","tan","mci","job","wet","ism",
                "err","him","all","pad","hah","hie","aim","ike","jed","ego","mac",
                "baa","min","com","ill","was","cab","ago","ina","big","ilk","gal",
                "tap","duh","ola","ran","lab","top","gob","hot","ora","tia","kip",
                "han","met","hut","she","sac","fed","goo","tee","ell","not","act",
                "gil","rut","ala","ape","rig","cid","god","duo","lin","aid","gel",
                "awl","lag","elf","liz","ref","aha","fib","oho","tho","her","nor",
                "ace","adz","fun","ned","coo","win","tao","coy","van","man","pit",
                "guy","foe","hid","mai","sup","jay","hob","mow","jot","are","pol",
                "arc","lax","aft","alb","len","air","pug","pox","vow","got","meg",
                "zoe","amp","ale","bud","gee","pin","dun","pat","ten","mob");
//        List<String> wordList = Arrays.asList("hot","dot","dog","lot","log","cog");
        wordLadderII.findLaddersI("cet", "ism", wordList).stream()
                .forEach(System.out::println);
    }
}
