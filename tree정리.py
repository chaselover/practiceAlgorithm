# 이진트리
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left  == None : self.inorderTraversal(node.left)
        print(node, end='')
        if not node.right == None : self.inorderTraversal(node.right)
    
    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end='')

    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node

if __name__ == "__main__":
    node = []
    node.append(Node('-'))
    node.append(Node('*'))
    node.append(Node('/'))
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D'))

    m_tree = Tree()
    for i in range(int(len(node)/2)):
        m_tree.makeRoot(node[i],node[i*2+1],node[i*2+2])

    print(       '전위 순회 : ', end='') ; m_tree.preorderTraversal(m_tree.root)
    print('\n' + '중위 순회 : ', end='') ; m_tree.inorderTraversal(m_tree.root)
    print('\n' + '후위 순회 : ', end='') ; m_tree.postorderTraversal(m_tree.root)



    # 스레드 이진트리
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.is_thread_right = None

    def __str__(self):
        return str(self.data)

class ThreadTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self, node):
        while not node.left == None:
            node = node.left
        print(node, end='')
        while True:
            node = self.findThread(node)
            print(node, end='')
            if node.right == None:
                break

    def findThread(self, node):
        pre_node = node
        node = node.right
        if node == None:
            return node
        if pre_node.is_thread_right:
            return node
        while not node.left == None:
            node = node.left
        return node

    def makeRoot(self, node, left_node, right_node, thread):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node
        node.is_thread_right = thread

if __name__ == "__main__":
    node = []
    node.append(Node('-'))
    node.append(Node('*'))
    node.append(Node('/'))
    node.append(Node('A'))
    node.append(Node('B'))
    node.append(Node('C'))
    node.append(Node('D'))

    m_tree = ThreadTree()
    for i in range(int(len(node)/2)):
        m_tree.makeRoot(node[i],node[i*2+1],node[i*2+2], False)

    m_tree.makeRoot(node[3], None, None, True)
    m_tree.makeRoot(node[4], None, None, True)
    m_tree.makeRoot(node[5], None, None, True)

    node[3].right = node[1]
    node[4].right = node[0]
    node[5].right = node[2]
    
    print('중위 순회 : ', end='') ; m_tree.inorderTraversal(m_tree.root)

    # 이진탐색트리
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)

class SearchTree:
    def __init__(self):
        self.root = None

    def insertElement(self, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node
        
        node = self.root
        while True:
            pre_node = node
            if node.data > new_node.data:
                node = node.left
                if node == None:
                    node = new_node
                    pre_node.left = node
            elif node.data < new_node.data:
                node = node.right
                if node == None:
                    node = new_node
                    pre_node.right = node
            else: return

    def searchElement(self, data):
        node = self.root
        while True:
            if node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
            elif node.data == data:
                break
            else:
                return Node('탐색 결과 없음')
        
        return node

    def preorderTraversal(self, node):
        print(node, end=' ')
        if not node.left  == None : self.preorderTraversal(node.left)
        if not node.right == None : self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left  == None : self.inorderTraversal(node.left)
        print(node, end=' ')
        if not node.right == None : self.inorderTraversal(node.right)
    
    def postorderTraversal(self, node):
        if not node.left  == None : self.postorderTraversal(node.left)
        if not node.right == None : self.postorderTraversal(node.right)
        print(node, end=' ')

if __name__ == "__main__":
    m_tree = SearchTree()

    m_tree.insertElement(250)
    for i in range(20):
        m_tree.insertElement(random.randint(0,500))
    
    print(       '전위 순회 : ', end='') ; m_tree.preorderTraversal(m_tree.root)
    print('\n' + '중위 순회 : ', end='') ; m_tree.inorderTraversal(m_tree.root)
    print('\n' + '후위 순회 : ', end='') ; m_tree.postorderTraversal(m_tree.root)

    node = m_tree.searchElement(250)
    print('\n' + '탐색한 노드의 값 :', node)
    print(       '노드의 왼쪽 서브 트리 :', node.left)
    print(       '노드의 오른쪽 서브 트리 :', node.right)

    node = m_tree.searchElement(node.left.data)
    print('\n' + '탐색한 노드의 값 :', node)
    print(       '노드의 왼쪽 서브 트리 :', node.left)
    print(       '노드의 오른쪽 서브 트리 :', node.right)


    # 힙구조
class Heap:
    def __init__(self):
        self.array = []

    def __str__(self):
        return str(self.array)

    def insertElement(self, data):
        self.array.append(data)
        length = len(self.array)
        if length > 1:
            node_num = length - 1
            while True:
                next_node_num = int(node_num/2)
                if self.array[next_node_num] < self.array[node_num]:
                    temp = self.array[node_num]
                    self.array[node_num] = self.array[next_node_num]
                    self.array[next_node_num] = temp
                else:
                    break
                node_num = int(node_num/2)
                if node_num == 0:
                    break

    def deleteRoot(self):
        root_value = self.array[0]
        del self.array[0]

        last_index = len(self.array) - 1
        if last_index < 0:
            return root_value
        tail_value = self.array[last_index]
        del self.array[last_index]

        self.array.insert(0, tail_value)
        now_index = 0
        next_index = 0
        while True:
            now_index = next_index
            next_index *= 2
            if next_index + 2 > last_index:
                break
            if self.array[next_index + 1] > self.array[next_index + 2]:
                next_index += 1
            else:
                next_index += 2
            if self.array[now_index] < self.array[next_index]:
                temp = self.array[now_index]
                self.array[now_index] = self.array[next_index]
                self.array[next_index] = temp
        return root_value

if __name__ == '__main__':
    m_heap = Heap()
    m_heap.insertElement(2)
    m_heap.insertElement(4)
    m_heap.insertElement(5)
    m_heap.insertElement(8)
    m_heap.insertElement(2)
    m_heap.insertElement(3)
    print('Heap :', m_heap)
    print('Delete Root :', m_heap.deleteRoot())
    print('Delete Root :', m_heap.deleteRoot())
    print('Delete Root :', m_heap.deleteRoot())
    print('Heap :', m_heap)