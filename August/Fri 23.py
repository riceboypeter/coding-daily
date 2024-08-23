'''
Friday 23rd, 2024
Finished in about 40 minutes with distractions

Implement a stack that has the following methods:
•	push(val), which pushes an element onto the stack
•	pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
•	max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

# going off geeksforgeeks' stack implementation
# https://www.geeksforgeeks.org/stack-in-python/
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("head")
        self.size = 0
        # use a pseudo-stack to store the max value(s)
        self.maxval = []

    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-2]

    def getSize(self):
        return self.size
    
    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.isEmpty():
            return None
        return self.head.next.value

    def push(self, value):
        # sort the first value or >=max; >= to track multiple same value pushes
        if not self.maxval:
            self.maxval.append(value)
        elif value >= self.maxval[-1]:
            self.maxval.append(value)
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
        
    def pop(self):
        if self.isEmpty():
            return None
        remove = self.head.next
        self.head.next = remove.next
        self.size -= 1
        # remove max value 
        if remove.value == self.maxval[-1]:
            self.maxval.remove(self.maxval[-1])
        return remove.value
    
    # self explanatory
    def max(self):
        if not self.maxval:
            return None
        return self.maxval[-1]
    
stack = Stack()
for i in [1,2,3,5,5,4,7]:
    stack.push(i)
    assert stack.peek() == i, "Pushing the wrong number!"

print(stack)

assert stack.max() == 7, "Max is wrong!"
assert stack.pop() == 7, "Popped the wrong number!"
assert stack.peek() == 4, "Pop didn't pop!"
assert stack.max() == 5, "Max isn't working!"

print(stack)