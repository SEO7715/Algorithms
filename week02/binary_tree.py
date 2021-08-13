# 노드 생성
class Node: 
    def __init__(self, value): #비어있는 노드로 초기화
        self.value = value
        self.left = None #현재는 루트 노드에 자식 노드가 없으므로 None 으로 넣어주기
        self.right = None

# 노드 삽입
class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.root #current_node를 루트 노드로 초기화 시키기
        while True:
            if value < self.current_node.value: # 삽입하고자 하는 값이 current_node의 값보다 작을 경우
                if self.current_node.left != None: #current_node의 왼쪽 자식이 None이 아니면, (있으면)
                    self.current_node = self.current_node.left #current_node의 왼쪽 자식이 current_node가 됨 
                else:
                    self.current_node.left = Node(value) #current_node의 왼쪽 자식이 없으면, 노드 값을 넣어줌
                    break
            else: # 삽입하고자 하는 값이 current_node의 값보다 클 경우
                if self.current_node.right != None: #current_node의 오른쪽 자식이 None이 아니면(있으면)
                    self.current_node = self.current_node.right #current_node의 오른쪽 자식이 current_node가 됨
                else:
                    self.current_node.right = Node(value) #current_node의 왼쪽 자식이 없으면, 노드 값을 넣어줌
                    break

# 노드 탐색
def search(self, value):
    self.current_node = self.root #current_node를 루트 노드부터 탐색 시작
    while self.current_node : 
        if self.current_node == value: #current_node의 값이 찾고자 하는 값일 경우 True 리턴
            return True
        elif self.current_node.value > value: #current_node의 값이 찾고자 하는 value 값보다 더 큰 경우, 찾고자 하는 값은 현재 노드의 왼쪽에 있으므로
            self.current_node = self.current_node.left #current_node를 왼쪽 자식으로 갱신해주기
        else: #current_node의 값이 찾고자 하는 value 값보다 작은 경우, 찾고자 하는 값은 현재 노드의 오른쪽에 있으므로
            self.current_node = self.current_node.right #current_node를 오른쪽 자식으로 갱신해주기
    return False

# 노드 삭제
def delete(self, value):
    is_search = False     # 삭제할 노드가 있는지 검사하고 없으면 False 리턴
    self.current_node = self.root # 검사 후에는 삭제할 노드가 current_node, 
    self.parent = self.root # 삭제할 노드의 부모 노드가 parent가 됨
    while self.current_node:
        if self.current_node.value == value:
            is_search = True # current_node의 값이 찾고자 하는 값일 경우 True 리턴
            break
        elif value < self.current_node.value: # current_node의 값이 value보다 클 경우
            self.parent = self.current_node # current_node는 부모가 노드가 됨
            self.current_node = self.current_node.left # current_node의 왼쪽자식이 current_node가 됨
        else:
            self.parent = self.current_node 
            self.current_node = self.current_node.right 
    if is_search == False:
        return False


            
