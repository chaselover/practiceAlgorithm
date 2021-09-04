import sys
input = sys.stdin.readline

class Node:
    def __init__(self):
        self.child = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self,word):
        node = self.root

        for char in word:
            if char not in node.child:
                node.child[char] = Node()
            node = node.child[char]
        node.word = True

    def search(self,word,n):
        node = self.root

        for i in range(n):
            if word[i] not in node.child:
                return i if node.word else 0
            node = node.child[word[i]]

C, N = map(int, input().split())
c_trie = Trie()
n_trie = Trie()
for _ in range(C):
    c_trie.insert(input().rstrip())
for _ in range(N):
    n_trie.insert(input().rstrip()[::-1])

for _ in range(int(input())):
    query = input().rstrip()
    n = len(query)
    idx1 = c_trie.search(query,n)
    if not idx1:
        print('No')
        continue
    idx2 = n_trie.search(query[::-1], n)
    print('Yes'if idx1+idx2==n else 'No')
