'''
Created on 29-Jan-2017

@author: bhuvan
'''
from node import Node
class LinkedList(object):
    def __init__(self):
        self.head=None;
        self.counter=0;
    def traverse(self):
        endNode=self.head;
        while(endNode.nextnode!=None):
            print ("%d " % endNode.data)
            endNode=endNode.nextnode
        print ("%d " % endNode.data)
    #O(1)    
    def insertStart(self,data):
        newNode=Node(data)
        self.counter=self.counter+1;
        if self.head==None:
            self.head=newNode
        else:
            newNode.nextnode=self.head
            self.head=newNode    
    def size(self):
        return self.counter
    def insertEnd(self,data):
        newNode=Node(data);
        if self.head==None:
            self.insertStart(data);
        else:
            endNode=self.head
            while(endNode.nextnode!=None):
                endNode=endNode.nextnode
            endNode.nextnode=newNode
    def remove(self,data):
        if self.head:
            if self.head.data==data:
                self.head=self.head.nextnode
            else:
                self.head.remove(data,self.head)
        