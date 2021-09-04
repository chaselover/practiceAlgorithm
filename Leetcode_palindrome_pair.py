from collections import defaultdict


class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.word_id = -1
        self.palindrome_word_ids = []

class Trie:
    # 삽입된 word와 id를 node를 생성. 노드는 자식, word_id, 펠린드롬 단어 id를 가짐.
    def __init__(self):
        self.root = Node()
    
    # 펠린드롬을 검사하는 메서드
    @staticmethod
    def is_palindrome(word):
        return word == word[::-1]
    
    # 결국 핵심은 
    def insert(self,index,word):
        node = self.root

        # 단어를 뒤집어 검사하는데 만약 뒤에서 일정부분 자른 word가 펠린드롬이면 펠린드롬 단어 ids 배열에 단어의 i를 넣어줌.
        for i, char in enumerate(reversed(word)):
            # 다른단어 + 왼쪽 펠린드롬 부분 + 오른쪽 부분을 만족하는 단어를 찾기위함.
            if self.is_palindrome(word[:len(word)-i]):
                node.palindrome_word_ids.append(index)
            node = node.children[char]
            # 노드의 children[char]이 있으면 node로 삼고 없으면 새로 노드를 만듦 
        # 다 끝나면 word_id를 i로 저장.(원배열에서 위치.)
        node.word_id = index

    def search(self,index,word):
        result = []
        node = self.root

        # word가 없어질때까지 순회
        while word:
            # 노드의 word_id가 0 이 아니다? = 단어가 있다.(오른쪽에 붙힐 단어)
            if node.word_id >= 0:
                # 단어가 펠린드롬을 만족한다?
                if self.is_palindrome(word):
                    # 결과에 단어의 idex와 거꾸로 뒤집혀 삽입된 단어의 id를 넣는다.
                    result.append([index,node.word_id])
            # word의 맨앞 글자가 node의 children에 없다면?
            if not word[0] in node.children:
                # 반환.
                return result
            # 다음 노드는 char의 아들
            node = node.children[word[0]]
            # word맨앞 글자는 제외.
            word = word[1:]
        
        # 다 끝났는데 단어의 id가 있다. 즉 온전히 펠린드롬을 이루는 단어가 있다면?그리고 같은 요소가 아니라면?
        # 두쌍은 펠린드롬을 이루므로 결과에 삽입.
        if node.word_id >= 0 and node.word_id != index:
            result.append([index, node.word_id])

        # 다 돌았는데 마지막노드에서 부분 펠린드롬을 이루는 녀석이 있었다면?(그 노드 앞쪽이 펠린드롬을 이룬다는 뜻.)
        # 그 노드에서 끝난 부분 trie에 펠린드롬 워드가 있다면? 워드 + trie에 저장된 펠린드롬 워드의 왼쪽 + 오른쪽이 펠린드롬을 이룬다는 뜻.
        for palindrome_word_id in node.palindrome_word_ids:
            result.append([index, palindrome_word_id])

        return result


# 단어 리스트에서 word[i] + word[j]가 펠린드롬이 되는 모든 인덱스 조합(i,j)를 구하라.
class Solution:
    def palindromePairs(self, words):
        trie = Trie()
        # 각 문자열에 index 부여.(구분을 위함) 트라이에 삽입.
        for i, word in enumerate(words):
            trie.insert(i, word)
        
        results = []

        for i, word in enumerate(words):
            results.extend(trie.search(i,word))
        
        return results




class Solution(object):
    def palindromePairs(self, words):
        ans = set()
        index = {word:i for i, word in enumerate(words)}
        
        for i, word in enumerate(words):
            for j in range(len(word)+1):
                # 좌우로 나눠 왼쪽이나 오픈쪽이 펠린드롬이라면 그부분 지워버리고 남은 부분을 뒤집은 게 index에 있다면 ans에 넣는다.(index쌍으로) - (왼쪽, 오른쪽)
                left = word[:j]
                right = word[j:]
                
                # check if any other word that concat to the left will make palindrome: "OTHER_WORD+`left`+`right`"
                # The above will be palindrome only if
                # 1. `left` is palindrome (left==left[::-1])
                # 2. Exit an "OTHER_WORD" in word in words that equals to the reverse of `right` (right[::-1] in index and index[right[::-1]]!=i).
                if left==left[::-1]:
                    if right[::-1] in index and index[right[::-1]]!=i:
                        ans.add((index[right[::-1]], i))
                
                # check if any other word that concat to the right will make palindrome: "`left`+`right`+OTHER_WORD"
                # The above will be palindrome only if
                # 1. `right` is palindrome (right==right[::-1])
                # 2. Exit an "OTHER_WORD" in words that equals to the reverse of `left` (left[::-1] in index and index[left[::-1]]!=i).
                if right==right[::-1]:
                    if left[::-1] in index and index[left[::-1]]!=i:
                        ans.add((i, index[left[::-1]]))
                        
        return ans


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        rmap={w[::-1]:i for i,w in enumerate(words)}
        res=[]
        for i,wrd in enumerate(words):
            rev=wrd[::-1]
            if wrd in rmap:                        # same length pair
                if rmap[wrd]!=i:                   # i and j should be distinct
                    res.append((i,rmap[wrd]))
            for j in range(1,len(wrd)+1):          # first or last j characters as palindrome, other part has pair
                if wrd[:-j] in rmap and wrd[-j:]==rev[:j]:
                    res.append((i,rmap[wrd[:-j]]))
                if wrd[j:] in rmap and wrd[:j]==rev[-j:]:
                    res.append((rmap[wrd[j:]],i))
        return res

class Solution(object):
    def palindromePairs(self, words):
        result = set()
        d = {words[x]: x for x in range(len(words))}
        for i, w in enumerate(words):
            rev = w[::-1]
            l = len(w)
            for j in range(l + 1):
                if w[j:] == rev[:l-j]:
                    if rev[l-j:] in d:
                        result.add((i, d[rev[l-j:]]))
                if w[:l-j] == rev[j:]:
                    if rev[:j] in d:
                        result.add((d[rev[:j]], i))

        return [x for x in result if x[0] != x[1]]







class Solution:
    def palindromePairs(self, words):
        the_trie = trie(node(None))
        results = []
        for k, i in enumerate(words):
            the_trie.insert_word_into_trie(i, k)
        for k, i in enumerate(words):
            self.check_each_prefix(i, k, the_trie, results)
            self.check_each_suffix(i, k, the_trie, results)
        return results
    
    def check_each_prefix(self, word, index, the_trie, results):
        idx = 0
        while idx < len(word):
            if self.is_palindrome(word[:idx]):
                trie_results = the_trie.find_val_in_trie(word[idx:][::-1], index)
                for i in trie_results: results.append([i, index])
            idx += 1
                        
    def check_each_suffix(self, word, index, the_trie, results):
        idx = len(word) - 1
        while idx > -1:
            if self.is_palindrome(word[idx:]):
                suf = word[:idx][::-1]
                trie_results = the_trie.find_val_in_trie(suf, index)
                for i in trie_results:
                    results.append([index, i])
                    if suf == "": results.append([i, index])
            idx -= 1
    
    def is_palindrome(self, w):
        return w == w[::-1]

class node(object):
    def __init__(self, val):
        self.neighbors = {}
        self.suffixes_to_word_idx = set()

class trie(object):
    def __init__(self, root):
        self.root = root
        self.neighbors = {}

    def insert_word_into_trie(self, word, index):
        current_node = self.root    
        if word == "": # edge case with empty string in list
            n = node("")
            n.suffixes_to_word_idx.add(index)
            self.root.neighbors[""] = n
        for k, i in enumerate(word):
            if current_node.neighbors.get(i) is None:
                current_node.neighbors[i] = node(i)
            if k == len(word) - 1:
                current_node.neighbors[i].suffixes_to_word_idx.add(index)
            current_node = current_node.neighbors[i]
    
    def find_val_in_trie(self, word, index):
        current_node = self.root
        if word == "" and self.root.neighbors.get(""): # edge case with empty string in list
            c = self.root.neighbors[""].suffixes_to_word_idx.copy()
            if index in c:
                c.remove(index)
            return c
        for k, i in enumerate(word):
            if current_node.neighbors.get(i) is None:
                break
            if k == len(word) - 1:
                c = current_node.neighbors[i].suffixes_to_word_idx.copy()
                if index in c:
                    c.remove(index)
                return c
            current_node = current_node.neighbors[i]
        return []











class TrieNode:    
    def __init__(self):
        self.children = defaultdict(TrieNode)
        # self.word = None
        self.index = -1

class Solution:
    def _buildRevTrie(self, words):
        trie = TrieNode()
        for i, w in enumerate(words):
            p = trie
            rev = w[::-1]
            for c in rev:
                p = p.children[c]
            p.word = w
            p.index = i
        return trie
    
    def _isPalindrome(self, s):
        if len(s) == 0: return True
        lo, hi = 0, len(s)-1
        while lo <= hi:
            if s[lo] != s[hi]:
                return False
            lo += 1
            hi -= 1
        return True
        
    def _traverseTrie(self, root, prefix, results):
        # print("!")
        if root.index != -1 and self._isPalindrome(prefix):
            results.append(root.index)
        for i in root.children:
            self._traverseTrie(root.children[i], prefix+i, results)
            
    
    def _findPairs(self, idx):
        w = self.words[idx]
        p = self.trie
        ret = []
        i = -1
        c = ""
        for i, c in enumerate(w):
            if p.index != -1:
                # The case where the first word is longer
                if self._isPalindrome(w[i:]) and p.index != i:
                    ret.append(p.index)
            if c not in p.children:
                return ret
            p = p.children[c]
            
        if i == len(w) - 1:
            self._traverseTrie(p, "", ret)

        return [i for i in ret if i != idx]
        # return ret
        
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        self.trie = self._buildRevTrie(words)
        self.words = words
        
        ret = []
        for i in range(len(words)):
            for j in self._findPairs(i):
                ret.append([i, j])
            
        return ret
            