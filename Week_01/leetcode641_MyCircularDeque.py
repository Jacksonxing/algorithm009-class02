class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        
        self.capacity = k
        self.size = 0
        
        self.circular_deque = [ 0 ] * k
        
        self.rear = 0
        self.front = k-1
        
        
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.size+1 <= self.capacity:
            
            self.circular_deque[ self.front ] = value
            self.front = (self.front-1)%self.capacity
            self.size += 1
        
            return True
        else:
            return False
        

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        
        if self.size+1 <= self.capacity:
            
            self.circular_deque[ self.rear ] = value
            self.rear = (self.rear+1)%self.capacity
            self.size += 1
        
            return True
        
        else:
            return False
        
        
        
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        
        if self.size != 0:
            
            self.front = (self.front+1)%self.capacity
            self.size -= 1
            return True
        
        else:
            return False
        
        

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """

        if self.size != 0:
            
            self.rear = (self.rear-1)%self.capacity
            self.size -= 1
            return True
        
        else:
            return False        
        
        

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        
        if self.size != 0:
            return self.circular_deque[ (self.front+1)%self.capacity ]
        else:
            return -1
        

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        
        if self.size != 0:
            return self.circular_deque[ (self.rear-1)%self.capacity ]
        else:
            return -1
        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        
        return self.size == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        
        return self.size == self.capacity

# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()