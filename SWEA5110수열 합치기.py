# class Node:
#     # 초기화 메소드
#     def __init__(self, data):
#         self.data = data
#         self.link = None

# class LinkedList:
#     # 초기화 메소드
#     def __init__(self):
#         new_node = Node('head')
#         self.head = new_node
#         self.tail = new_node
#         self.before = None
#         self.current = None
#         self.num_of_data = 0

#     def append(self, data):
#         new_node = Node(data) # 새 노드 생성
#         self.tail.link = new_node # 연결
#         self.tail = new_node # tail 갱신
#         self.num_of_data += 1

#     def first(self):
#         if self.num_of_data == 0: # 빈 리스트이면 None 리턴
#             return None
#         self.before = self.head
#         self.current = self.head.link
#         return self.current.data

#     def next(self):
#         self.before = self.current
#         self.current = self.current.link
#         if self.current == None:
#             return None
#         return self.current.data

#     def insertlist(self, new_list):
#         insert_num = new_list.first()
#         num = self.first()
#         # 수열 2의 첫 숫자 보다 큰 수자를 수열 1에서 찾아 그 앞에 수열 2를 끼워 넣는다.
#         for _ in range(self.num_of_data):
#             if num > insert_num:
#                 self.before.link = new_list.head.link
#                 new_list.tail.link = self.current
#                 self.num_of_data += new_list.num_of_data
#                 break
#             num = self.next()
#         else: # 큰 숫자가 없는 경우 맨 뒤에 붙인다.
#             self.tail.link = new_list.head.link
#             self.num_of_data += new_list.num_of_data

#     # 빈 리스트에 링크드리스트data 담아서 마지막 10요소 출력
#     def my_result(self):
#         lst = []
#         num = self.first()
#         for i in range(self.num_of_data):
#             lst.append(num)
#             num = self.next()
#         return ' '.join(map(str, lst[-1:-11:-1]))

# # main 함수
# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())

#     # 빈 LinkedList 생성
#     Seq1 = LinkedList()

#     # LinkedList 입력받기
#     for i in map(int, input().split()):
#         Seq1.append(i)

#     for _ in range(M - 1):
#         # 빈 LinkedList 생성
#         Seq2 = LinkedList()
#         # LinkedList 입력받기
#         for j in map(int, input().split()):
#             Seq2.append(j)
#         # Seq1에 Seq2 삽입
#         Seq1.insertlist(Seq2)
    
#     print('#{} {}'.format(test_case, Seq1.my_result()))

for test in range(1,int(input())+1):
    N, M = map(int, input().split())
    arr = [float('inf')]
    cnt = 0
    for _ in range(M):
        a = list(map(int, input().split()))
        for i in range(N*cnt+1):
            if a[0] < arr[i]:
                arr[i:i] = a
                break
        cnt +=  1
    print(f'#{test}',end=' ')
    print(*arr[-11:-1][::-1])