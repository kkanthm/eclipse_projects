# '''
# Created on Dec 23, 2018
# 
# @author: Krishnakanth M
# '''
# class Node:
#         def __init__(self, data,left=None, right=None):
#             self.data = data;
#             self.left=left;
#             self.right=right;
#         def insertLeft(self,node):
#             newNode = node;
#             if self is None:
#                 self = newNode;
#             
#             else:
#                 if self.left == None:
#                     self.left=newNode;
#                 else:
#                     newNode.left=self.left;
#                     self.left=newNode;
#         def insertRight(self,node):
#             newNode = node
#             if self is None:
#                 self = newNode;
#             
#             else:
#                 if self.right == None:
#                     self.right=newNode;
#                 else:
#                     newNode.right=self.right;
#                     self.right=newNode;
# class Tree:
#     
#     
#     def __init__(self,Node=None):
#         self.root=Node;
# 
#     
#     def printTree(self, node):
#         if node != None:
#             print(node.data);
#             if node.left!=None:
#                 self.printTree(node.left);
#             if node.right!=None:
#                 self.printTree(node.right);
#     
#     
# 
# bt = Tree();
# ANode = Node('A',None,None)
# BNode = Node('B',None,None)
# CNode = Node('C',None,None)
# DNode = Node('D',None,None)
# ENode = Node('E',None,None)
# FNode = Node('F',None,None)
# GNode = Node('G',None,None)
# bt.root = ANode;
# ANode.insertLeft(BNode);
# ANode.insertRight(CNode);
# BNode.insertLeft(DNode);
# BNode.insertRight(ENode);
# CNode.insertLeft(FNode);
# CNode.insertRight(GNode);
# bt.printTree(ANode);
#                 
#         
#                 
#             
# 
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None
# class Tree:
#     def createNode(self, data):
#         return Node(data)
#     def insert(self, node, data, ch):
#         if node is None:
#             return self.createNode(data)
#         if (ch == 'L'):
#             node.left = self.insert(node.left, data, ch)
#             return node.left
#         else:
#             node.right = self.insert(node.right, data, ch)
#             return node.right
#     def search(self, lis, data):
#         # if root is None or root is the search data.
#         for i in lis:
#             if i.data == data:
#                 return i            
# def height(root):
#     if root==None:
#         return 0;
#     if root and root.left==None and root.right == None:
#         return 1
#     if root.left == None and root.right!=None:
#         return height(root.right)+1;
#     if root.left!=None and root.right==None:
#         return height(root.left)+1;
#     
#     if root.left!=None and root.right!=None:
#         LH = height(root.left);
#         RH = height(root.right);
#         
#         if LH>RH:
#             return LH+1;
#         else:
#             return RH+1;
# def countLeaves(root):
#     if root==None:
#         return 0;
#     if root and root.left==None and root.right == None:
#         return 1
#     if root.left == None and root.right!=None:
#         return countLeaves(root.right);
#     if root.left!=None and root.right==None:
#         return countLeaves(root.left);
#     
#     return countLeaves(root.left)+countLeaves(root.right);
#     
#     
# 
# root = None
# t = int(input())
# for i in range(t):
#     n = int(input())
#     arr = input().strip().split()
#     if n ==0:
#         print(0)
#         continue
#     dictTree = dict()
#     
#     for j in range(n):
#         if arr[3*j] not in dictTree:
#             dictTree[arr[3*j]] = Node(arr[3*j])
#             parent = dictTree[arr[3*j]]
#             if j is 0:
#                 root = parent
#             
#         else:
#             parent = dictTree[arr[3*j]]
            
#         child = Node(arr[3*j+1])
#         if (arr[3*j+2] == 'L'):
#             parent.left = child
#         else:
#             parent.right = child
#         dictTree[arr[3*j+1]] = child
#         
#     print(countLeaves(root))
# class Node:
#     def __init__(self,val):
#         self.right = None
#         self.data = val
#         self.left = None
# def inorderTraversalUtil(root):
#     # Code here
#     if root is None:
#         return
#     inorderTraversalUtil(root.left)
#     print(root.data, end=' ')    
#     inorderTraversalUtil(root.right)
# def inorderTraversal(root):
#     # Code here
#     inorderTraversalUtil(root)
#     print()
# #def swap(node1,node2):
#     
# def mirror(root):
#     if root is None:
#         return root;
#     node=root;
#     if node.left==None and node.right==None:
#         return node;
#      
#     mirror(node.left);
#     mirror(node.right);
#     
#     node.left,node.right = node.right,node.left;
#     
#     return root;
# 
# t = int(input())
# 
# for i in range(t):
#     n = int(input())
#     arr = input().strip().split()
#     if n == 0:
#         print(0)
#         continue
#     
#     root = None
#     dictTree = dict()
#     
#     for j in range(n):
#         if arr[3*j] not in dictTree:
#             dictTree[arr[3*j]] = Node(int(arr[3*j]))
#             parent = dictTree[arr[3*j]]
#             
#             if j is 0:
#                 root = parent
#         else:
#             parent = dictTree[arr[3*j]]
#         
#         child = Node(int(arr[3*j+1]))
#             
#         if(arr[3*j+2] == 'L'):
#             parent.left = child
#         else:
#             parent.right = child
#         dictTree[arr[3*j+1]] = child
#             
#     mirror(root)
#     
#     inorderTraversal(root)

#Initial Template for Python 3
# def isBalanced(root):
#     
#     if root==None:
#         return 1;
#     if root and root.left==None and root.right==None:
#         return 1;
#     if root.left==None and root.right!=None:
#         if root.right.left!=None or root.right.right!=None:
#             return 0;
#     if root.left!=None and root.right==None:
#         if root.left.left!=None or root.left.right!=None:
#             return 0;
#     return isBalanced(root.left) and isBalanced(root.right);
# if __name__=='__main__':
#     
#     root = None
#     t = int(input())
#     for i in range(t):
#         #root = None
#         n = int(input())
#         arr = input().strip().split()
#         if n ==0:
#             print(0)
#             continue
#         dictTree = dict()
#         
#         for j in range(n):
#             if arr[3*j] not in dictTree:
#                 dictTree[arr[3*j]] = Node(arr[3*j])
#                 parent = dictTree[arr[3*j]]
#                 if j is 0:
#                     root = parent
#                 
#             else:
#                 parent = dictTree[arr[3*j]]
#                 
#             child = Node(arr[3*j+1])
#             if (arr[3*j+2] == 'L'):
#                 parent.left = child
#             else:
#                 parent.right = child
#             dictTree[arr[3*j+1]] = child
#             
#         if isBalanced(root):
#             print(1) 
#         else:
#             print(0) 


# 
# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.data = value
#         self.right = None
# class Tree:  # Binary tree Class
#     def createNode(self, data):
#         return Node(data)
#     
#     def insert(self, node, data, ch):
#         if node is None:
#             return self.createNode(data)
#         if (ch == 'L'):
#             node.left = self.insert(node.left, data, ch)
#             return node.left
#         else:
#             node.right = self.insert(node.right, data, ch)
#             return node.right
#     def search(self, lis, data):
#         # if root is None or root is the search data.
#         for i in lis:
#             if i.data == data:
#                 return i
#     def traverseInorder(self, root):
#         if root is not None:
#             self.traverseInorder(root.left)
#             print(root.data, end=" ")
#             self.traverseInorder(root.right)
# 
# def findPath(root, node, pathArray):
#     if root == None:
#         return False;
#     pathArray.append(root.data);
#     
#     if root.data==node:
#         return True;
#     
#     if (root.left!=None and findPath(root.left, node, pathArray)) or (root.right!=None and findPath(root.right, node, pathArray)):
#         return True;
#     
#     pathArray.pop();
#     return False;
# def findLCA(root, n1, n2):
#     path1=[]
#     path2=[]
#     
# 
#    
#     if not findPath(root, n1, path1) or not findPath(root, n2, path2):
#         return Node(-1);
#     
#     i=0;
#     while i<len(path1) and i<len(path2):
#         if path1[i]!=path2[i]:
#             break;
#         i=i+1;
#     return Node(path1[i-1]);
#     
# 
# t=int(input())
# for i in range(t):
#     n=int(input())
#     arr = input().strip().split()
#     tree = Tree()
#     lis=[]
#     root = None
#     root = tree.insert(root, int(arr[0]), 'L')
#     lis.append(root)
#     k=0
#     for j in range(n):
#         ptr = None
#         ptr = tree.search(lis, int(arr[k]))
#         lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
#         k+=3
#     n1,n2 = list(map(int, input().strip().split()))
#     print(findLCA(root, n1, n2).data)


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
class Tree:
    def createNode(self, data):
        return Node(data)
    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right
    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i
# Driver Program
# def height(root,finalAnswer):
#     if root==None:
#         return 0;
#     leftHeight = height(root.left,finalAnswer);
#     rightHeight = height(root.right,finalAnswer);
# 
#     
#     finalAnswer[0] = max(finalAnswer[0],1+leftHeight+rightHeight);
#     
#     return 1+max(leftHeight,rightHeight);
#     
# def diameter(root):
#     finalAnswer=[0]
#     if root == None:
#         return root;
#     
#     height(root,finalAnswer);
#     return finalAnswer[0];
def leftHelper(root,level,maxLevel):
    if root==None:
        return
    if maxLevel[0]<level:
        print(root.data,end=' ')
        maxLevel[0]=level;
    leftHelper(root.left, level+1, maxLevel)
    leftHelper(root.right, level+1, maxLevel)
    
def printLeftView(root):
    
    
    if root==None:
        return
    maxLevel = [0];
    print(root.data,end=' ')
    return leftHelper(root,0,maxLevel)
    

    
'''
1
5
1 2 L 1 3 R 2 4 L 2 5 R 5 6 L

lever order traversal
def leftnodeInEveryLevel():


'''

t=int(input())
for i in range(t):
    n=int(input())
    arr = input().strip().split()
    if n ==0:
        print('')
        continue
    tree = Tree()
    lis=[]
    root = None
    root = tree.insert(root, int(arr[0]), 'L')
    lis.append(root)
    k=0
    for j in range(n):
        ptr = None
        ptr = tree.search(lis, int(arr[k]))
        lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
        k+=3
    printLeftView(root)
    print('')

