class Node: 
    def __init__(self): 
        self.word = False 
        self.children = {} 

class Trie: 
    def __init__(self): 
        self.root = Node() 
    
    def insert(self, word: str) -> None: 
        node = self.root 
        for char in word: 
            if char not in node.children: 
                node.children[char] = Node() 
            node = node.children[char] 
        node.word = True 
    
    def search(self, word: str) -> bool: 
        node = self.root 
        for char in word: 
            if char not in node.children: 
                return False 
            node = node.children[char] 
        
        return node.word 
    
    def startsWith(self, prefix: str) -> bool: 
        node = self.root 
        for char in prefix: 
            if char not in node.children: 
                return False 
            node = node.children[char] 
        
        return True
    
    def travel(self, level: int, node: Node) -> None: 
        if node.word: 
            return 
        
        cur_children = sorted(node.children) 
        
        for child in cur_children: 
            print("--"*level + child) 
            self.travel(level+1, node.children[child])
