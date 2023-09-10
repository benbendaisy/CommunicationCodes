from typing import List


class Solution:
    """
    There are n items each belonging to zero or one of m groups where group[i] is the group that the i-th item belongs to and it's equal to -1 if the i-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.

    Return a sorted list of the items such that:

    The items that belong to the same group are next to each other in the sorted list.
    There are some relations between these items where beforeItems[i] is a list containing all the items that should come before the i-th item in the sorted array (to the left of the i-th item).
    Return any solution if there is more than one solution and return an empty list if there is no solution.

    Example 1:

    Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
    Output: [6,3,4,1,5,2,0,7]
    Example 2:

    Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
    Output: []
    Explanation: This is the same as example 1 except that 4 needs to be before 6 in the sorted list.
    """
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        def topology_sort(nodes, pred, succ):
            order, no_pred = [], deque(node for node in nodes if not pred[node])
            while no_pred:
                node = no_pred.popleft()
                order.append(node)
                for s in succ[node]:
                    pred[s].discard(node)
                    if not pred[s]:
                        no_pred.append(s)
            return order if len(order) == len(nodes) else []
        
        group_to_items, new_group = defaultdict(set), m
        for item in range(n):
            if group[item] == -1:
                group[item] = new_group
                new_group += 1
            group_to_items[group[item]].add(item)
        intra_pred, intra_succ, inter_pred, inter_succ = defaultdict(set), defaultdict(set), defaultdict(set), defaultdict(set)
        for item in range(n):
            for before in beforeItems[item]:
                if group[item] == group[before]:
                    intra_pred[item].add(before)
                    intra_succ[before].add(item)
                else:
                    inter_pred[group[item]].add(group[before])
                    inter_succ[group[before]].add(group[item])
        groups_order = topology_sort(list(group_to_items.keys()), inter_pred, inter_succ)
        if not groups_order:
            return []
        items_order = []
        for grp in groups_order:
            order = topology_sort(group_to_items[grp], intra_pred, intra_succ)
            if not order:
                return []
            items_order.extend(order)
        return items_order

