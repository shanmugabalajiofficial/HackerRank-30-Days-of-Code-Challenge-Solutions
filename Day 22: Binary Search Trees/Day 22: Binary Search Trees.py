#Day 22: Binary Search Trees


class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

   
    def getHeight(self, root):
        if not root.right and not root.left:
            return 0
        r_h = self.getHeight(root.right) if root.right else 0
        r_l = self.getHeight(root.left) if root.left else 0
        return max(r_h, r_l) + 1

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)       
