# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 21:52:49 2020

@author: HP
"""

class UF:
    
    def __init__(self, size):
        #number of elements in this union find
        self.size = size
        #size of each of the components, initally size of each is 1
        self.sz = [1] * size
        #id[i] points to parent of i, if id[i] = i ten i is a root node
        self.id = [i for i in range(size)]
        #track the number of components
        self.numComponents = size
     
    #given a node it finds which node it belongs to and does path compression
    def find(self, p):
        root = p
        #find the root of the component/set
        while(root != self.id[root]):
            root = self.id[root]
            
        #compress the path leading back to the root, path compression
        while(p!= root):
            next = self.id[p]
            self.id[p] = root
            p = next
        return root
    
    #return if elements p and q are in same component
    def connected(self, p, q):
        return self.find(p) == self.find(q)
    
    #return size of the component set p belongs to
    #root nodes are the one that contain the size
    def componentSize(self, p):
        return self.sz[self.find(p)]
    
    #return number of elements in disjoint set
    def size(self):
        return self.size
    
    #number of remaining components
    def components(self):
        self.numComponents
    
    #we are treating p and q as integers as we map what maps to objects
    def unify(self, p, q):
        root1 = self.find(p)
        root2 = self.find(q)
        
        #if the elements are already in the same group
        if root1 == root2:
            return
        #merger two components together
        #merge smaller component to larger component
        if(self.sz[root1] < self.sz[root2]):
            self.sz[root2] += self.sz[root1]
            self.id[root1] = self.root2
        else:
            self.sz[root1] += self.sz[root2]
            self.id[root2] = self.root1
            
        #since the roots found are different and we merged so the size must have decreased
        self.numComponents -= 1
        
    
        