class Solution:
    """
    A game on an undirected graph is played by two players, Mouse and Cat, who alternate turns.

    The graph is given as follows: graph[a] is a list of all nodes b such that ab is an edge of the graph.

    The mouse starts at node 1 and goes first, the cat starts at node 2 and goes second, and there is a hole at node 0.

    During each player's turn, they must travel along one edge of the graph that meets where they are.  For example, if the Mouse is at node 1, it must travel to any node in graph[1].

    Additionally, it is not allowed for the Cat to travel to the Hole (node 0).

    Then, the game can end in three ways:

    If ever the Cat occupies the same node as the Mouse, the Cat wins.
    If ever the Mouse reaches the Hole, the Mouse wins.
    If ever a position is repeated (i.e., the players are in the same position as a previous turn, and it is the same player's turn to move), the game is a draw.
    Given a graph, and assuming both players play optimally, return

    1 if the mouse wins the game,
    2 if the cat wins the game, or
    0 if the game is a draw.

    Example 1:

    Input: graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    Output: 0
    Example 2:

    Input: graph = [[1,3],[0],[3],[0,2]]
    Output: 1
    """
    def catMouseGame1(self, graph: List[List[int]]) -> int:
        n = len(graph)
        @cache
        def helper(mouse_pos: int, cat_pos: int, moves: int):
            if mouse_pos == 0:
                return 1

            if mouse_pos == cat_pos:
                return 2
            
            if moves >= 5 * n:
                return 0
            
            if moves % 2 == 0:
                res = 2
                for next_pos in graph[mouse_pos]:
                    next_res = helper(next_pos, cat_pos, moves + 1)
                    if next_res == 1:
                        res = 1
                        break
                    if next_res == 0:
                        res = 0
            else:
                res = 1
                for next_pos in graph[cat_pos]:
                    if next_pos == 0:
                        continue
                    next_res = helper(mouse_pos, next_pos, moves + 1)
                    if next_res == 2:
                        res = 2
                        break
                    if next_res == 0:
                        res = 0
            return res
        
        return helper(1, 2, 0)
    
    def catMouseGame2(self, graph: List[List[int]]) -> int:
        if not graph:
            return 0
        n = len(graph)
        @cache
        def helper(mouse_pos: int, cat_pos: int, moves: int) -> int:
            if mouse_pos == 0:
                return 1
            
            if mouse_pos == cat_pos:
                return 2
            
            if moves >= 5 * n:
                return 0
            
            if moves % 2 == 0:
                res = 2
                for next_pos in graph[mouse_pos]:
                    next_res = helper(next_pos, cat_pos, moves + 1)
                    if next_res == 1:
                        res = 1
                        break
                    if next_res == 0:
                        res = 0
            else:
                res = 1
                for next_pos in graph[cat_pos]:
                    if next_pos == 0:
                        continue
                    next_res = helper(mouse_pos, next_pos, moves + 1)
                    if next_res == 2:
                        res = 2
                        break
                    if next_res == 0:
                        res = 0
            return res
        return helper(1, 2, 0)