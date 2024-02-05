# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
    """
    @return True if this NestedInteger holds a single integer, rather than a nested list.
    """

    def getInteger(self) -> int:
    """
    @return the single integer that this NestedInteger holds, if it holds a single integer
    Return None if this NestedInteger holds a nested list
    """

    def getList(self) -> [NestedInteger]:
    """
    @return the nested list that this NestedInteger holds, if it holds a nested list
    Return None if this NestedInteger holds a single integer
    """

class NestedIterator:
    def traverse(self, nestedList: [NestedInteger]):
        for i in range(len(nestedList)):
            if nestedList[i].isInteger():
                self.arr.append(nestedList[i].getInteger())
            else:
                self.traverse(nestedList[i].getList())
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = []
        self.idx = 0
        self.traverse(nestedList)
        self.n = len(self.arr)
    
    def next(self) -> int:
        res = self.arr[self.idx]
        self.idx += 1
        return res
    
    def hasNext(self) -> bool:
        return self.idx < self.n