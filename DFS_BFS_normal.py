def DFS(start_node):
    	# 1) stack 에 첫 번째 노드 넣으면서 시작
    stack = [start_node, ]
        
    while True:
            # 2) stack이 비어있는지 확인 
        if len(stack) == 0:
            	print('All node searched.')
            return None
                
            # 3) stack에서 맨 위의 노드를 pop
        node = stack.pop()
                
            # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
            print('The target found.')
            return node
            
            # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)
            
            # 6) children을 stack에 쌓기
        stack.extend(children)
            
            # 7) 이렇게 target을 찾거나, 전부 탐색해서 stack이 빌 때까지 while문 반복
def BFS(start_node):
    	# 1) queue 에 첫 번째 노드 넣으면서 시작
    queue = [start_node, ]
        
    while True:
        # 2) queue가 비어있는지 확인 
        if len(queue) == 0:
        	print('All node searched.')
            return None
            
        # 3) queue에서 맨 앞의 노드 를 dequeue (0번 인덱스를 pop)
        node = queue.pop(0)
            
        # 4) 만약 node가 찾고자 하는 target이라면 서치 중단!
        if node == TARGET:
        	print('The target found.')
            return node
        
        # 5) node의 자식을 expand 해서 children에 저장
        children = expand(node)
        
        # 6) children을 stack에 쌓기
        queue.extend(children)
        
        # 7) 이렇게 target을 찾거나, 전부 탐색해서 queue가 빌 때까지 while문 반복