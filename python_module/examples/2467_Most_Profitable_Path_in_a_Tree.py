class Solution:
    """
    
    """
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        if not edges:
            return -1
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bob_path = []
        def find_bob(node: int, parent: int):
            bob_path.append(node)
            if node == 0:
                return True
            for next_node in graph[node]:
                if next_node != parent and find_bob(next_node, node):
                    return True
            bob_path.pop()
            return False
        
        find_bob(bob, -1)
        bob_times = {node: time for time, node in enumerate(bob_path)}

        def dfs(node: int, parent: int, time: int, income: int):
            curr_amount = amount[node]
            if node in bob_times and bob_times[node] == time:
                curr_amount //= 2
            elif node in bob_times and bob_times[node] < time:
                curr_amount = 0
            
            income += curr_amount

            if len(graph[node]) == 1 and graph[node][0] == parent:
                return income
            
            max_income = float("-inf")
            for next_node in graph[node]:
                if next_node != parent:
                    max_income = max(max_income, dfs(next_node, node, time + 1, income))
            return max_income
        
        return dfs(0, -1, 0, 0)