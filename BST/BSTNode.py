'''
Created on 11-Feb-2017

@author: bhuvan
'''
from BST.Node import Node
class BST(object):
    def __init__(self):
        self.rootNode=None;
    def insert(self,data):
        if not self.rootNode:#rootnode is None.hence constructor o BST.Node will be called
            self.rootNode=Node(data)
        else:#rootnode is not None
            self.rootNode.insert(data)
    def remove(self,data):
        if self.rootNode:
            if self.rootNode.data==data:
                tempNode=Node(None)
                tempNode.leftchild=self.rootNode
                self.rootNode.remove(data,tempNode)
            else:
                self.rootNode.remove(data, None)
    def getMax(self):
        if self.rootNode:
            return self.rootNode.getMax()
    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()
    def traversInOrder(self):
        if self.rootNode:
            self.rootNode.traversInOrder() 
            
            
            