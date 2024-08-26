class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        up_element_del = self.stack.pop()
        return up_element_del

    def peek(self):
        up_element = self.stack[-1]
        return up_element

    def size(self):
        len_stack = len(self.stack)
        return len_stack
























