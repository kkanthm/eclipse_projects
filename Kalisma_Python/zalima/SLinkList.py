'''
Created on Nov 19, 2018

@author: Krishnakanth M
'''

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep1):
    while node:
        print(str(node.data), end=sep1)

        node = node.next

        

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    
    
    llist3 = SinglyLinkedList();
    while(head1 and head2):
        
        if(head1.data < head2.data):
            llist3.insert_node(head1.data);
            head1= head1.next;
        elif(head1.data > head2.data):
            llist3.insert_node(head2.data);
            head2 = head2.next;
        else:
            llist3.insert_node(head1.data);
            llist3.insert_node(head2.data);
            head1 = head1.next
            head2 = head2.next
            
    if not head1 and head2:
        llist3.insert_node(head2.data);
    if not head2 and head1:
        llist3.insert_node(head1.data);
    return llist3.head;


def getNode(head, positionFromTail):
    list1 = []
    if head is None:
        return head;
    while head:
        list1.append(head.data);
        head=head.next;
    list1.reverse()
    return list1[positionFromTail]

def has_cycle(head):
    return

def findMergeNode(head1, head2):
    
    lengthOfHead1, lengthOfHead2 = 0,0;
    curr1, curr2 = head1, head2;
    while curr1:
        lengthOfHead1 += 1;
        curr1=curr1.next
    
    while curr2:
        lengthOfHead2 += 1;
        curr2=curr2.next
    curr1, curr2 = head1, head2;
    #diff1 = lengthOfHead1 if (lengthOfHead1>=lengthOfHead2)  else lengthOfHead2;
    diff = abs(lengthOfHead1-lengthOfHead2);
    
    if(lengthOfHead1>lengthOfHead2):
        index=0;
        while(index<diff):
            curr1=curr1.next;
            index=index+1;
    elif(lengthOfHead2>lengthOfHead1):
        index=0;
        while(index<diff):
            curr2=curr2.next;
            index=index+1;
    
    while curr1 and curr2:
        curr1=curr1.next
        curr2=curr2.next
        if(curr1==curr2):
            return curr1;
    return 
    
    
tests = int(input())

for tests_itr in range(tests):
    index = int(input())

    llist1_count = int(input())

    llist1 = SinglyLinkedList()

    for _ in range(llist1_count):
        llist1_item = int(input())
        llist1.insert_node(llist1_item)
        
    llist2_count = int(input())

    llist2 = SinglyLinkedList()

    for _ in range(llist2_count):
        llist2_item = int(input())
        llist2.insert_node(llist2_item)
        
    ptr1 = llist1.head;
    ptr2 = llist2.head;

    for i in range(llist1_count):
        if i < index:
            ptr1 = ptr1.next
            
    for i in range(llist2_count):
        if i != llist2_count-1:
            ptr2 = ptr2.next

    ptr2.next = ptr1

    result = findMergeNode(llist1.head, llist2.head)
    print((str(result) + '\n'));




