from sortedcontainers import SortedDict
from collections import defaultdict

class ListNode:

    def __init__(self, keys, freq=0, next=None, prev=None):
        self.keys = keys
        self.freq = freq
        self.next = next
        self.prev = prev


class AllOne:

    def __init__(self):
        self.key_store = {}
        self.head = ListNode(set())
        self.tail = ListNode(set())
        self.head.next = self.tail
        self.tail.prev = self.head

    def inc(self, key: str) -> None:
        if key in self.key_store:
            node = self.key_store[key]
            node.keys.remove(key)
        else: node = self.head
        if node.next.freq == node.freq + 1:
            self.key_store[key] = node.next
            node.next.keys.add(key)
        else:
            newn = ListNode({key}, node.freq+1, next=node.next, prev=node)
            node.next.prev = node.next = newn
            self.key_store[key] = newn
        if node != self.head and not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def dec(self, key: str) -> None:
        node = self.key_store[key]
        node.keys.remove(key)
        if node.freq == 1: self.key_store.pop(key)
        elif node.prev.freq + 1 == node.freq:
            node.prev.keys.add(key)
            self.key_store[key] = node.prev
        else:
            newn = ListNode({key}, node.freq-1, next=node, prev=node.prev)
            node.prev.next = node.prev = newn
            self.key_store[key] = newn
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev

    def getMaxKey(self) -> str:
        if self.tail.prev == self.head: return ""
        ans = self.tail.prev.keys.pop()
        self.tail.prev.keys.add(ans)
        return ans

    def getMinKey(self) -> str:
        if self.head.next == self.tail: return ""
        ans = self.head.next.keys.pop()
        self.head.next.keys.add(ans)
        return ans



class AllOne1:

    def __init__(self):
        self.word_to_count = {}
        self.count_to_words = SortedDict()

    def inc(self, key: str) -> None:
        if key not in self.word_to_count:
            self.word_to_count[key] = 1
            if 1 in self.count_to_words:
                self.count_to_words[1].add(key)
            else:
                self.count_to_words[1] = set()
                self.count_to_words[1].add(key)
        else:
            self.adjust_count(key, True)

    def adjust_count(self, key, is_inc):
        prev_count = self.word_to_count[key]
        new_count = prev_count + 1 if is_inc else prev_count - 1
        self.count_to_words[prev_count].remove(key)
        if not self.count_to_words[prev_count]:
            del self.count_to_words[prev_count]
        if new_count == 0:
            del self.word_to_count[key]
        else:
            if new_count in self.count_to_words:
                self.count_to_words[new_count].add(key)
            else:
                self.count_to_words[new_count] = set()
                self.count_to_words[new_count].add(key)
            self.word_to_count[key] = new_count


    def dec(self, key: str) -> None:
        if key in self.word_to_count:
            self.adjust_count(key, False)

    def getMaxKey(self) -> str:
        if self.count_to_words:
            data = self.count_to_words.peekitem()[1]
            return next(iter(data))
        return ""

    def getMinKey(self) -> str:
        if self.count_to_words:
            data = self.count_to_words.peekitem(index=0)[1]
            return next(iter(data))
        return ""
