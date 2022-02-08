#priority heap based on the max heap and min heap
class heap(object):
    def __init__(self):
        self.heap=[0]
        self.size=0
    """NOTE:In adding new elements we need to know if the element should move up the tree/list"""
    def float(self,k):
        while k//2:
            if self.heap[k]<self.heap[k//2]:
                self.heap[k],self.heap[k//2]=self.heap[k//2],self.heap[k]
            k//=2
    #to insert elements in the tree
    def insert(self,item):
        self.heap.append(item)
        self.size+=1
        self.float(self.size)
    #when we need to pop the root node , a new root is found as the last element. how ever it needs to sink to find the actual node
    def min_index(self,k):
        """we first find the min index"""
        if k*2+1>self.size:
            return k*2
        elif self.heap[k*2]<self.heap[k*2+1]:
            return k*2
        else:
            return k*2+1
    def sink(self,k):
        while k*2 <= self.size:
            mi=self.min_index(k)
            if self.heap[k]>self.heap[mi]:
                self.heap[k],self.heap[mi]=self.heap[mi],self.heap[k]
                self.heap[k]
            k=mi
    #now we pop the elements o , not pills lmaooo
    def pop(self):
        item=self.heap[1]
        self.heap[1]=self.heap[self.size]
        self.size-=1
        self.heap.pop()
        self.sink(1)
        return item