class Stack:
    def __init__(self):
        self.items = []
    def push (self,item):
        self.items.append(item)  
    def pop (self):
        if len (self.items)>0:
            return self.items.pop()
        else:
            return "Stack is empty!"  
    def display(self):
        return self.items     

Stack = Stack() 
Stack.push(10)
Stack.push(20)
Stack.push(30)
Stack.push(40)
Stack.push(50)

print(f"stack items:{Stack.display()}\n")
print(f"Popped item:{Stack.pop()}")
print(f"Popped item:{Stack.pop()}\n")
print(f"stack items:{Stack.display()}")


