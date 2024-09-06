# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        l3 = ListNode(0)
        curr = l3
        a = ""
        b = ""

        while l1 != None:
            a += str(l1.val)
            l1 = l1.next 
            
        while l2 != None:
            b += str(l2.val)
            l2 = l2.next
        
        c = int(a[::-1]) + int(b[::-1])
        c = str(c)
        for char in c[::-1]:
            new = ListNode(char)
            curr.next = new
            curr = new
        
        return l3.next