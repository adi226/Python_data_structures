# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:56:48 2020

@author: HP
"""

class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.data = data
        self.next = next
        self.previous = prev
        
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
    
    def insertAfter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.previous = prev_node
        
        if new_node.next is not None:
            new_node.next.previous = new_node
        
    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.previous = None
            self.head = new_node
            return
        last = self.head
        while(last.next is not None):
            last = last.next
            
        last.next = new_node
        new_node.previous = last
        
        return
    
    def printList(self, node):
        while(node is not None):
          #  print " % d" %(node.data),
            print(node.data)
            last = node
            node = node.next
            
        while(last is not None):
         #   print " % d " %(last.data),
            print(last.data)
            last = last.previous
    
llst = DoublyLinkedList()
llst.append(6)
llst.push(7)
llst.push(1)
llst.append(4)
llst.insertAfter(llst.head.next, 8)
llst.printList(llst.head)
        
        
        