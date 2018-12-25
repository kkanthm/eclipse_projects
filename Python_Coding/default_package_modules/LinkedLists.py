'''
Created on Nov 14, 2018

@author: Krishnakanth M
'''


class Node:
    
    def __init__(self,data,nextNode=None):
        self.data = data;
        self.nextNode = nextNode;

def findMiddle(head):
    fastRunner = head;
    slowRunner = head;
          
    tick = False
    while fastRunner:
        fastRunner = fastRunner.nextNode;
        if tick:
            slowRunner = slowRunner.nextNode;
        tick = not tick;
    return slowRunner.data;
def printList(head):
    currentNode = head;

    while currentNode != None:
        print(currentNode.data, end=" ");
        currentNode = currentNode.nextNode;
def removeElement(head, Element):
    
    if(head.data == Element):
        head.data = None;
        head = head.nextNode;
        return
       
    currentNode = head;
    while currentNode != None:
        if currentNode.nextNode!= None and currentNode.nextNode.data==Element:
            currentNode.nextNode.data= None;
            currentNode.nextNode = currentNode.nextNode.nextNode;
            break;
        elif currentNode.nextNode == None and currentNode.data == Element:
            currentNode.data = None;
            break;
        
        currentNode = currentNode.nextNode
    else:
        print("Not Found")
        
            
    return
Node1 = Node(5);
Node2 = Node(6);
Node3 = Node(7);
Node4 = Node(8);
Node5 = Node(9);

Node1.nextNode = Node2;
Node2.nextNode = Node3;
Node3.nextNode = Node4;
Node4.nextNode = Node5;

printList(Node1)

print()
print(findMiddle(Node1)) 

removeElement(Node1, 5)

printList(Node1)