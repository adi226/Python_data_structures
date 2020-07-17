# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 00:48:18 2020

@author: HP
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
if __name__ == '__main__':
    
    llst = LinkedList()
    llst.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    llst.head.next = second
    second.next = third
    
    llst.printList()