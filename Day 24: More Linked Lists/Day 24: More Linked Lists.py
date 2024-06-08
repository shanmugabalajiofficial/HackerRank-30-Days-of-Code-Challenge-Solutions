#Day 24: More Linked Lists


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

        #Write your code here
    def removeDuplicates(self, head):
        if not head or not head.next:
            return head
        
        curr = head
        prev = None
        last_seen = None
        while curr:
            if curr.data == last_seen:
                prev.next = curr.next
            else:
                last_seen = curr.data
                prev = curr
            curr = curr.next
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
