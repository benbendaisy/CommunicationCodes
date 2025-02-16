class MinStack1:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int val) pushes the element val onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.
    You must implement a solution with O(1) time complexity for each function.

    Example 1:

    Input
    ["MinStack","push","push","push","getMin","pop","top","getMin"]
    [[],[-2],[0],[-3],[],[],[],[]]

    Output
    [null,null,null,null,-3,null,0,-2]

    Explanation
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin(); // return -3
    minStack.pop();
    minStack.top();    // return 0
    minStack.getMin(); // return -2
    """

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

class MinStack:
    def __init__(self):
        self.stack = []
    
    class Node:
        def __init__(self, val, min_val):
            self.val = val
            self.min_val = min_val
    
    def push(self, val: int) -> None:
        node = self.Node(val, val)
        if not self.stack:
            self.stack.append(node)
        else:
            top_node = self.stack[-1]
            if node.min_val > top_node.min_val:
                node.min_val = top_node.min_val
            self.stack.append(node)
    
    def pop(self) -> None:
        self.stack.pop()
    
    def top(self) -> int:
        return self.stack[-1].val
    
    def getMin(self) -> int:
        return self.stack[-1].min_val