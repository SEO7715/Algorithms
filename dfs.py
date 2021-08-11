
def dfs(graph, start_node): 
    visit = list() # 방문했던 노드 목록 순차 저장할 리스트
    stack = list() # 다음으로 방문할 노드 목록 순차 저장할 리스트(스택)
    
    stack.append(start_node) #처음엔 시작 노드를 스택에 넣어줌

    while stack: #스택 목록이 바닥날 때까지(더 이상 방문할 노드가 없을 때까지) 루프 돌리기
        node = stack.pop() #스택의 맨 마지막에 있는 노드 가져오기
        if node not in visit: #노드가 방문했던 목록에 없다면, 
            visit.append(node) #방문 목록에 추가
            stack.extend(graph[node]) #해당 노드의 자식 노드를 스택에 추가 
    return visit


