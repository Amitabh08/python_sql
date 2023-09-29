class Node:
    def __init__(self, value,next=None, previous=None):
        self._value=value
        self._next=next
        self._previous=previous
        
class LinkedList:
    def __init__(self):
        self._first=None

    def append(self, value):
        if self._first==None: # list is empty
            self._first=Node(value)
        else: # add to the end of a non-empty list
            n=self._first
            while n._next:
                n=n._next
            n._next=Node(value, previous=n)

    def info(self):
        if self._first==None: 
            return "LinkedList(empty)"
        str="LinkedList(\t"
        n=self._first
        while n:
            str+=f'{n._value}\t'
            n=n._next
        str+=")"
        return str
    def size(self):
        c=0
        n=self._first
        while n:
            c+=1
            n=n._next
        return c
            
    def get(list,index):
       n = list.redundant_function(index)
       return n.__value if n else None


    def set(list,index,value):
            n = list.redundant_function(index)
            if n:
                n._value=value

    def insert(list, index, value):
        y = list.redundant_function(index)
            
        x=y._previous if y else None

        new_node=Node(value,previous=x,next=y)
        
        if x:
            x._next=new_node
        else:
            list._first=new_node

        y._previous=new_node

    def remove(list, index):
        n = list.redundant_function(index)
        if not n:
            return
        x= n._previous
        y= n._next

        if x:
            x._next=y
        else:
            list._first=y

        if y:
            y._previous=x
        return n._value
    
    def redundant_function(index):
        n=list._first
        for i in range(index):
            n=n._next
            if n is None:
                return None
            else:
                return n

l=LinkedList()
for n in range(10,101,10):
    l.append(n)

print(l.info())

l.insert(6,55)
print(l.info())