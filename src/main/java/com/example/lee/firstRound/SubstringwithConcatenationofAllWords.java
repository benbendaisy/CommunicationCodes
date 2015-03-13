package com.example.lee.firstRound;

import java.util.*;

/**
 * Created by benbendaisy on 2/26/15.
 *
 * You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.
 *
 * For example, given:
 * S: "barfoothefoobarman"
 * L: ["foo", "bar"]
 *
 * You should return the indices: [0,9].
 * (order does not matter).
 */
public class SubstringwithConcatenationofAllWords {

    //refers to http://blog.csdn.net/linhuanmars/article/details/20342851
    public List<Integer> findSubstring(String S, String[] L) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == S || S.length() < 1 || null == L || L.length < 1) {
            return list;
        }

        Map<String, Integer> dict = new HashMap<String, Integer>();
        for (String str : L) {
            if (dict.containsKey(str)) {
                dict.put(str, dict.get(str) + 1);
            } else {
                dict.put(str, 1);
            }
        }
        int len = L[0].length();
        for (int i = 0; i < len; i++) {
            Map<String, Integer> map = new HashMap<String, Integer>();
            int left = i;
            int count = 0;
            for (int j = i; j <= S.length() - len; j += len) {
                String str = S.substring(j, j + len);
                if (dict.containsKey(str)) {
                    if (map.containsKey(str)) {
                        map.put(str, map.get(str) + 1);
                    } else {
                        map.put(str, 1);
                    }

                    if (map.get(str) <= dict.get(str)) {
                        count++;
                    } else {
                        while (map.get(str) > dict.get(str)) {
                            String subStr = S.substring(left, left + len);
                            if (map.containsKey(subStr)) {
                                map.put(subStr, map.get(subStr) - 1);
                                if (map.get(subStr) < dict.get(subStr)) {
                                    count--;
                                }
                            }
                            left += len;
                        }
                    }
                    if (count == L.length) {
                        list.add(left);
                        String subStr = S.substring(left, left + len);
                        if (map.containsKey(subStr)) {
                            map.put(subStr, map.get(subStr) - 1);
                        }
                        count--;
                        left += len;
                    }
                } else {
                    map.clear();
                    count = 0;
                    left = j + len;
                }
            }
        }
        return list;
    }

    //find all possible word combinations and find its index. However, cannot pass with ttl
    public List<Integer> findSubstringI(String S, String[] L) {
        List<Integer> list = new ArrayList<Integer>();
        if (null == S || null == L || S.length() == 0 || L.length == 0) {
            return list;
        }

        Set<String> set = new HashSet<String>();
        permutation(L, set, 0);
        for (String str : set) {
            int idx = S.indexOf(str);
            while (idx != -1) {
                list.add(idx);
                idx = S.indexOf(str, idx + 1);
            }
        }
        return list;
    }

    private void permutation(String[] L, Set<String> set, int idx) {
        if (idx == L.length) {
            StringBuilder sb = new StringBuilder();
            for (String str : L) {
                sb.append(str);
            }
            set.add(sb.toString());
            return;
        }
        for (int i = idx; i < L.length; i++) {
            swap(L, i, idx);
            permutation(L, set, i + 1);
            swap(L, i, idx);
        }
    }

    private void swap(String[] L, int i, int j) {
        String tempStr = L[i];
        L[i] = L[j];
        L[j] = tempStr;
    }

    public static void main(String[] args) {
        SubstringwithConcatenationofAllWords substringwithConcatenationofAllWords = new SubstringwithConcatenationofAllWords();
        String str = "dlmogiklbqfggokuonfgugiyammwvwhbjvrqgdbjtipcwzwmobtjjdhmpvknrsqbpjtvmwfifukbwgokjjvvmeheatttljwdupygofotcywygmksvipkmyqmrjifueiouiukoldqlzquocojkdvzdlnuuvbqajewubgiolazmsvaujmfohervtorppipbolvrtdfefhqxcrrofycmewjykbnzjeazrxrkayohfgekzwyewctbyczidokoskojihvkflslryxruvxrzquytvgyjsndddmnkhzrstclsbeowchwsbwnwemhxbkcgwpqfqjzmmlenpumrckmdgzcmnjjqulwscoytyxhkklzahntjzfphhruwadnwpjptypmwovizijzqzuzycogjhahkdugugxoemccbymagvbyuxytzobkwbsigoobuoraatedrqfamiyigydhpeslhmvoajrxzixabcfvslxgvvpbwujlzdygptureloetogxslsmyrtuokxkeivflvmcoiutwkzryfoqsidtzypqkmaqxywktknisjdoteisjykdhpyipnyzcbqzzolsyycsjfjdjrxupjayzyhqohqqiirjyccwdgoomxtxqqugcwedwntkxlcfvvrtatpfbgtnfnnwfjchfikdwgotrsanorgqmyvoeqdldshldlsiufoslencwprmhyevwzlcqrpvlzgpkbzggnytrnxqdpekpjhnivraogwzfeoqfoynbzgvmelpvpbkyjxjgojuwhtcmkurysfbrnwerjvozxazixionukkbfonpihpcorwbpcvzxjaukzejksxeejhkxxzhgpjuihvxjqyhaydmaivkcuqhdztcyulelvyteutokrxmscasmwepswyyxrawnmazjbsnvndhfcwzfwrruxinvilsbnopbroksiapwfydkwcptvipstepbphffyugrktlsvaqaatkxxbssmhmhmbidjpijjravklofnghnaumxvesjoeqcibhtqsccjextpnaeuhtwdgvbknkaubccemvuezyndwiujkyftrbxxzykmkkilpkrdhohgmwjigduqdbjvdgueggqrtbeknwnvkubysnjysdowgztjipnowghpjmbwkorwkvuckfaciqaprvazlqqjyxahlbdxpxvzusdexfiivlzogbotrgerfeathgqydmxzgcddhnleykthmjcfphzwnzpvfgtkutjavoffcrjcdejrpoxevydkxsffabruwbwtrcytvkyyqhqgvpmsnpdmiktinlflmdffffzcrxbigtqeicyxudlcofmdqtpexwjebkhtjidsdtwlvwkpavtqaitsbkyagifiumdewgwzzumwqyoqtjgwrcqvmpvtzadtogxmmvnlrzjixxathjpylhvzwruvtxpkdowrmkedlonjloeuxtvkcqjzjeuddlnhalamvfrhvfsitwdsryetqnu";
        String[] strs = {"pbolvrtdfefhqxcrrofyc","mewjykbnzjeazrxrkayoh","fgekzwyewctbyczidokos","kojihvkflslryxruvxrzq","uytvgyjsndddmnkhzrstc","lsbeowchwsbwnwemhxbkc","gwpqfqjzmmlenpumrckmd","gzcmnjjqulwscoytyxhkk","lzahntjzfphhruwadnwpj","ptypmwovizijzqzuzycog","jhahkdugugxoemccbymag","vbyuxytzobkwbsigoobuo","raatedrqfamiyigydhpes","lhmvoajrxzixabcfvslxg","vvpbwujlzdygptureloet","ogxslsmyrtuokxkeivflv","mcoiutwkzryfoqsidtzyp","qkmaqxywktknisjdoteis","jykdhpyipnyzcbqzzolsy","ycsjfjdjrxupjayzyhqoh","qqiirjyccwdgoomxtxqqu","gcwedwntkxlcfvvrtatpf","bgtnfnnwfjchfikdwgotr","sanorgqmyvoeqdldshldl","siufoslencwprmhyevwzl","cqrpvlzgpkbzggnytrnxq"};
        System.out.println(substringwithConcatenationofAllWords.findSubstring(str, strs));
    }
}
