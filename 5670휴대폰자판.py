import sys
 
class Node:
    def __init__(self,chr):
        self.chr = chr
        self.child = {}
        self.check = False

class Trie:
    def __init__(self):
        self.root = Node('')

    def insert(self, word):
        node = self.root
        for w in word:
            if w not in node.child:
                new = Node(w)
                node.child[w] = new
                node = new
            else:
                node = node.child[w]
        node.check = True

    def contains(self, word):
        cnt = 0
        cur = self.root
        for w in word:
            cur = cur.child[w]
            if len(cur.child) > 1 or cur.check:
                cnt+=1
        return cnt

while 1:
    t = Trie()
    words = []
    try: N = int(sys.stdin.readline())
    except: break

    for _ in range(N):
        s = sys.stdin.readline().rstrip()
        t.insert(s)
        words.append(s)
    result = 0
    for word in words:
        result += t.contains(word)

    print("%.2f" % (result/N))

# 풀이2
import sys

DEBUG = False
def log(message):
    if DEBUG:
        print(message)

class Node():
    def __init__(self):
        self.is_terminated = False
        # self.key = key
        # self.data = data
        self.children = {}

class Trie():

    def __init__(self):
        self.head = Node()

    def insert(self, value):
        curr_node = self.head
        for char in value:
            if char not in curr_node.children:
                curr_node.children[char] = Node()
            curr_node = curr_node.children[char]
        curr_node.is_terminated = True

    def search(self, value):
        curr_node = self.head
        curr_node = curr_node.children[value[0]]
        search_num = 1
        for char in value[1:]:
            log(char)
            log(("curr_node.childen: ", curr_node.children))
            if (len(curr_node.children) != 1) or curr_node.is_terminated:
                search_num += 1
            else:
                pass
            curr_node = curr_node.children[char]
        log(("search_num:", search_num))
        return search_num

# keyb = Trie()

while 1:
    keyb = Trie()
    conti = sys.stdin.readline()
    # try:
    #     num_op = int(sys.stdin.readline())
    # except:
    #     break

    if (conti == ''):
        break
    num_op = int(conti)

    key_press_num = 0
    press_list = []


    for num in range(num_op):
        press_list.append(sys.stdin.readline().rstrip())
        keyb.insert(press_list[num])
    for num2 in range(num_op):
        key_press_num += keyb.search(press_list[num2])
    print("%.2f" %(key_press_num / num_op))



# 리스트 트라이?
import sys

lst_tri = list(map(str, range(ord('a'), ord('z') + 1)))
tri_t = [0] + [-1 for _ in range(len(lst_tri))]


def idx(chr_):
    return ord(chr_) - ord('a') + 1


def add(tri_, str_):
    idx_curr = 0
    for each_ in str_:
        idx_temp = idx(each_)
        if tri_[idx_curr][idx_temp] == -1:
            tri_[idx_curr][idx_temp] = len(tri_)
            tri_.append(tri_t.copy())
            tri_[idx_curr][0] += 1
        idx_curr = tri_[idx_curr][idx_temp]
    tri_[idx_curr][0] += 1


def find(tri_, str_):
    cnt_ = 1
    idx_curr = tri_[0][idx(str_[0])]
    for each_ in str_[1:]:
        if tri_[idx_curr][0] != 1:
            cnt_ += 1
        idx_temp = idx(each_)
        idx_curr = tri_[idx_curr][idx_temp]
    return cnt_


input_ = sys.stdin.readline()
while input_:
    N_ = int(input_)
    lst_ = []
    tri_ = [tri_t.copy()]
    for _ in range(N_):
        str_input = sys.stdin.readline().rstrip()
        lst_.append(str_input)
        add(tri_, str_input)
    cnt_ = 0
    for each_ in lst_:
        cnt_ += find(tri_, each_)
    print(format(cnt_ / N_, '.2f'))

    input_ = sys.stdin.readline()

exit()