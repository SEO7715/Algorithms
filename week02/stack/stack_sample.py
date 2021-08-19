class Stack():
    def __init__(self):
        self.stack = []
    
    def push(self, data): #list의 append 메소드 활용한 구현
        self.stack.append(data)
    
    def pop(self): #list의 pop 메소드 활용한 구현
        pop_object = None
        if self.isEmpty(): #먼저 isEmpty 메소드 활용하여 확인
            print("-1")
        else:
            pop_object = self.stack.pop()
        return pop_object 
    
    def top(self):
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]
        return top_object

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty
    