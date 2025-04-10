class Solution:
    """
    You are given a 2D array of strings equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] means that Ai / Bi = values[i].

    Determine if there exists a contradiction in the equations. Return true if there is a contradiction, or false otherwise.

    Note:

    When checking if two numbers are equal, check that their absolute difference is less than 10-5.
    The testcases are generated such that there are no cases targeting precision, i.e. using double is enough to solve the problem.

    Example 1:

    Input: equations = [["a","b"],["b","c"],["a","c"]], values = [3,0.5,1.5]
    Output: false
    Explanation:
    The given equations are: a / b = 3, b / c = 0.5, a / c = 1.5
    There are no contradictions in the equations. One possible assignment to satisfy all equations is:
    a = 3, b = 1 and c = 2.
    Example 2:

    Input: equations = [["le","et"],["le","code"],["code","et"]], values = [2,5,0.5]
    Output: true
    Explanation:
    The given equations are: le / et = 2, le / code = 5, code / et = 0.5
    Based on the first two equations, we get code / et = 0.4.
    Since the third equation is code / et = 0.5, we get a contradiction.
    """
    def checkContradictions1(self, equations: List[List[str]], values: List[float]) -> bool:
        if not equations:
            return False
        
        graph = defaultdict(list)
        for i, (u, v) in enumerate(equations):
            graph[u].append((v, values[i]))
            graph[v].append((u, 1 / values[i]))

        # Dictionary to keep track of assigned values to each variable
        value_dict = {}
        
        # BFS queue
        queue = deque()
        
        # Iterate through all variables in the graph
        for node in graph:
            if node not in value_dict:
                # Assign a starting value (1.0) to the current node
                value_dict[node] = 1.0
                queue.append(node)
                
                while queue:
                    current = queue.popleft()
                    for neighbor, weight in graph[current]:
                        # Calculate the value for the neighbor based on current node's value
                        new_value = value_dict[current] / weight
                        
                        if neighbor in value_dict:
                            # Check if the calculated value contradicts the existing value
                            if not math.isclose(new_value, value_dict[neighbor], rel_tol=1e-9):
                                return True  # Contradiction found
                        else:
                            # Assign the new value and continue BFS
                            value_dict[neighbor] = new_value
                            queue.append(neighbor)
        
        return False  # No contradictions found
    
    def checkContradictions2(self, equations: List[List[str]], values: List[float]) -> bool:
        if not equations:
            return False
        
        graph = defaultdict(list)
        for (u, v), value in zip(equations, values):
            graph[u].append((v, value))
            graph[v].append((u, 1 / value))
        value_dict, que = {}, deque()
        for node in graph:
            if node not in value_dict:
                value_dict[node] = 1.0
                que.append(node)
                while que:
                    cur = que.popleft()
                    for neighbor, weight in graph[cur]:
                        new_value = value_dict[cur] / weight
                        if neighbor in value_dict:
                            if abs(new_value - value_dict[neighbor]) > 0.0000001:
                                return True
                        else:
                            value_dict[neighbor] = new_value
                            que.append(neighbor)
        return False
    
    def checkContradictions3(self, equations: List[List[str]], values: List[float]) -> bool:
        if not equations:
            return False
        
        graph = defaultdict(list)
        for (u, v), value in zip(equations, values):
            graph[u].append((v, value))
            graph[v].append((u, 1 / value))
        
        que, value_dict = deque(), {}
        for node in graph:
            if node not in value_dict:
                value_dict[node] = 1.0 # validate current node
                que.append(node) # use node as a start point to calculate the value with base value as 1.0
                while que:
                    cur = que.popleft()
                    for neighbor, weight in graph[cur]:
                        new_value = value_dict[cur] / weight # calculate the new value for the neighbor
                        if neighbor in value_dict: # if the value of neighbor already exists, compare the new value
                            if abs(value_dict[neighbor] - new_value) > 0.0001:
                                return True
                        else:
                            value_dict[neighbor] = new_value
                            que.append(neighbor)
        return False