'''
Created on 29-Jan-2017

@author: bhuvan
'''
class Node(object):
    def __init__(self,data):
        self.data=data;
        self.nextnode=None;#nextnode is for reference for last node it is None
    def remove(self,data,prev_node):#prev_node is also a node
        if data==self.data:
            prev_node.nextnode=self.nextnode
            del self.data
            del self.nextnode
        else:
            if  self.nextnode is not None:
                self.nextnode.remove(data,self)#now make self as previous node and next node as self
                
            