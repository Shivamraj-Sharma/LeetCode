from typing import Optional
from collections import deque
"""

definition of binary tree node.
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def areAnagrams(self, node1 : Optional['Node'], node2 : Optional['Node']) -> bool:
        # code here
        q1, q2 = [node1], [node2]
        
        while q1 and q2:
            if len(q1) != len(q2):
                return False
            q1.sort(key=lambda n: n.data)
            q2.sort(key=lambda n: n.data)
            nq1, nq2 = [], []
            for i in range(len(q1)):
                x, y = q1[i], q2[i]
                if x.data != y.data:
                    return False
                if x.left:
                    nq1.append(x.left)
                if x.right:
                    nq1.append(x.right)
                if y.left:
                    nq2.append(y.left)
                if y.right:
                    nq2.append(y.right)
            q1, q2 = nq1, nq2
        return not q1 and not q2
        
        



#{ 
 # Driver Code Starts
class Node:
    def __init__(self,val):
        self.data=val
        self.right=None
        self.left=None

# Function to Build Tree
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

def inputTree():
    treeString=input().strip()
    root = buildTree(treeString)
    return root
def inorder(root):
    if (root == None):
       return
    inorder(root.left);
    print(root.data,end=" ")
    inorder(root.right)

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        node1 = inputTree();
        
        
        node2 = inputTree();
        
        obj = Solution()
        res = obj.areAnagrams(node1, node2)
        
        result_val = 1 if res else 0
        print(result_val)

# } Driver Code Ends