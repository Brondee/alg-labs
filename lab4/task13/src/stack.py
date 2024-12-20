class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None 

    def isEmpty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            return None
        popped_node = self.top
        self.top = self.top.next
        return popped_node.data

    def display(self):
        if self.isEmpty():
            return
        current = self.top
        while current:
            print(current.data, end=", ")
            current = current.next
        print("None")

if __name__ == "__main__":
    print("task 13.1")
    stack = Stack()
    print("Стек пуст:", stack.isEmpty())
    stack.push(10)
    stack.display()
    print("Извлечён элемент:", stack.pop())
    stack.display()
    print("Стек пуст:", stack.isEmpty())
    print('\n')

