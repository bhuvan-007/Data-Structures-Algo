'''
Created on 29-Jan-2017

@author: bhuvan
'''
class Node(object):
    def __init__(self,data):
        self.data=data;
        self.leftchild=None;
        self.rightchild=None;
    def insert(self,data):
        if data<self.data:
            if not self.leftchild:
                self.leftchild=Node(data)
            else:
                self.leftchild.insert(data)
        else:
            if not self.rightchild:
                self.rightchild= Node(data)
            else:
                self.rightchild.insert(data)
    def getMin(self):
        if self.leftchild is None:
            return self.data
        else:
            return self.leftchild.getMin()
    def getMax(self):
        if self.rightchild is None:
            return self.data
        else:
            return self.rightchild.getMax()
    def remove(self,data,parentNode):
        if data<self.data:#left subtree contains to be deleted node
            if self.leftchild is not None:
                self.leftchild.remove(data,self)#self becomes parent node nd remove operation applied on self.leftchild
        elif data>self.data:#right subtree contains to be deleted node
            if self.rightchild is not None:
                self.rightchild.remove(data,self)#self becomes parent node nd remove operation applied on self.rightchild
        else:
            if self.leftchild is not None and self.rightchild is not None:#has both left and right subtree
                self.data=self.rightchild.getMin()()#swap with max value in left subtree or min value in right subtree
                self.rightchild.remove(self.data,self)#remove the node with max or min vlaue and make self as parentnode 
            elif parentNode.leftchild==self:  #has only left subtree
                if self.leftchild is not None:
                    print parentNode.data
                    tempNode=self.leftchild
                else:
                    tempNode=self.rightchild
                    print parentNode.data
                parentNode.leftchild=tempNode
            elif parentNode.rightchild==self:  #has only right subtree
                if self.leftchild is not None:
                    print "parentNode.data"+str(parentNode.data)
                    print "self "+str(self.data)
                    tempNode=self.leftchild
                else:
                    tempNode=self.rightchild
                    print "parentNode.data "+str(parentNode.data)
                    print "self "+str(self.data)
                    print "self.rightChild= "+str(tempNode) 
                parentNode.rightchild=tempNode
    def traversInOrder(self):
        print "self.data= "+str(self.data)
        if self.leftchild is not None:
            print "self.data= "+str(self.data)+" has left node"
            print "(self.leftchild.traversInOrder()) called on self.leftchild.data= "+str(self.leftchild.data)
            self.leftchild.traversInOrder() 
        print "element= "+str(self.data)
        if self.rightchild is not None:
            print "self.data= "+str(self.data)+" has right node"
            print "(self.rightchild.traversInOrder()) called on self.rightchild.data=" +str(self.rightchild.data)
            self.rightchild.traversInOrder()           
                  
        