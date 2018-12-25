'''
Created on Dec 23, 2018

@author: Krishnakanth M
'''
class Node:
        def __init__(self, data,left=None, right=None):
            self.data = data;
            self.left=left;
            self.right=right;
        def insertLeft(self,node):
            newNode = node;
            if self is None:
                self = newNode;
            
            else:
                if self.left == None:
                    self.left=newNode;
                else:
                    newNode.left=self.left;
                    self.left=newNode;
        def insertRight(self,node):
            newNode = node
            if self is None:
                self = newNode;
            
            else:
                if self.right == None:
                    self.right=newNode;
                else:
                    newNode.right=self.right;
                    self.right=newNode;
class Tree:
    
    
    def __init__(self,Node=None):
        self.root=Node;

    
    def printTree(self, node):
        if node != None:
            print(node.data);
            if node.left!=None:
                self.printTree(node.left);
            if node.right!=None:
                self.printTree(node.right);
    
    

bt = Tree();
ANode = Node('A',None,None)
BNode = Node('B',None,None)
CNode = Node('C',None,None)
DNode = Node('D',None,None)
ENode = Node('E',None,None)
FNode = Node('F',None,None)
GNode = Node('G',None,None)
bt.root = ANode;
ANode.insertLeft(BNode);
ANode.insertRight(CNode);
BNode.insertLeft(DNode);
BNode.insertRight(ENode);
CNode.insertLeft(FNode);
CNode.insertRight(GNode);
bt.printTree(ANode);
                
        
                
            
            