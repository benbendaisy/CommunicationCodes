package com.example.ip.apple;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by benbendaisy on 6/3/15.
 *
 * design a structure to mimic blood family relationships and check if two
 * person share the same blood, which only male can pass blood to his sons and
 * daughters
 *
 */
public class BloodGraph {
    private static class BloodNode {
        private String gender;
        private BloodNode dad;
        private BloodNode mother;
        private List<BloodNode> children;
        public BloodNode(String gender) {
            this.gender = gender;
        }
    }

    public boolean sharingAncester(BloodNode node1, BloodNode node2) {
        if (null == node1 || null == node2) return false;
//        for (BloodNode child : node1.children) {
//            if ("M".equals(child.gender) && isAncester(child, node2)) return true;
//            if (sharingAncester(child, node2)) return true;
//        }
//
//        for (BloodNode child : node2.children) {
//            if ("M".equals(child.gender) && isAncester(child, node1)) return true;
//            if (sharingAncester(child, node1)) return true;
//        }

        return isAncester(node1, node2);
    }

    private boolean isAncester(BloodNode node1, BloodNode node2) {
        if (null == node1 || null == node2) return false;
        Set<BloodNode> parent = new HashSet<>();
        while (node1 != null) {
            parent.add(node1);
            node1 = node1.dad;
        }
        while (node2 != null) {
            if (!parent.add(node2)) return true;
            node2 = node2.dad;
        }

        return false;
    }
}
