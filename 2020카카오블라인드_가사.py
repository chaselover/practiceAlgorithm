class Node:
    def __init__(self):
        self.child = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        node = self.root

        for char in word:
            if char not in node.child:
                node.child[char] = Node()
            node.count += 1
            node = node.child[char]
        
    def startswitch(self,prefix):
        node = self.root

        for char in prefix:
            if char=='?':
                return node.count
            if char not in node.child:
                return 0
            node = node.child[char]
        return node.count

def solution(words, queries):
    trielength = {i: Trie() for i in range(1,10001)}
    re_trielength = {i: Trie() for i in range(1,10001)}
    answer = []

    for word in words:
        length = len(word)
        trielength[length].insert(word)
        re_trielength[length].insert(word[::-1])
    
    for query in queries:
        length = len(query)
        if query[0] !='?':
            answer.append(trielength[length].startswitch(query))
        else:
            answer.append(re_trielength[length].startswitch(query[::-1]))
    
    return answer