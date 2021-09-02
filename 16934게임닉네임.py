import sys
input = sys.stdin.readline
from collections import defaultdict


class Node:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:
    
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        same_nick[word] += 1
        node.word = True
    
    def search(self, word):
        node = self.root
        re_word = ''
        for char in word:
            re_word += char
            if char not in node.children:
                return re_word
            node = node.children[char]
            
        if node.word:
            re_word += str(same_nick[re_word]+1)
        return re_word
    
    
N = int(input())
tree = Trie()
same_nick = defaultdict(int)
for _ in range(N):
    word = input().rstrip()
    print(tree.search(word))
    tree.insert(word)

