#12.08

"""

list can contain string,boolean,integer,float,complex number,tuple,list,dictionary,set

array is containing only one type of data.we  use array when we want to store multiple values of the same type in a single variable. 
Arrays are more efficient in terms of memory and performance compared to lists when dealing with large amounts of data of the same type.
it need less memory and are faster to access and manipulate.

queue first in first out (FIFO) data structure. It is used to store a collection of elements,
where the first element added to the queue will be the first one to be removed. 
Queues are commonly used in scenarios such as task scheduling, print spooling, and handling requests in web servers.
enqueue: adding an element to the end of the queue
dequeue: removing an element from the front of the queue


stack last in first out (LIFO) data structure. using in  scenarios such as function call management, 
expression evaluation, and undo/redo functionality in applications.structure list

deque double-ended queue, which allows elements to be added or removed from both ends. (appendleft / append).
used in queue + stack combined operations, fast insert remove elements. structure collections.deque



integer byte sizes

radros da rato

space complexsiti rashveba rogor time complecsity 


set (no indexing, no duplicates) used for unique, fast search, compare groups  

dictionary (key-value pair, no duplicates, indexing)

hash fingerprint number of each file
hashmap system that uses hashes to store data in key-value pairs, allowing for efficient retrieval
and storage of data based on unique keys.

linked list objects are stored in nodes, where each node contains value and link to next node(reference or pointer). 
Singly linked lists(one-next)
Doubly linked lists(two-next and previous)
Circular linked lists(last to head)
example how its connected to nextnode
Class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
use it when we need insertion and deletion of elements frequently, when we don't know the 
size of the data in advance, when we want to implement dynamic data structures like stacks 
and queues, when we want to implement complex data structures like graphs and trees, when we 
want to save memory by not allocating a fixed amount of memory for a data structure.


tree data structure stores data (child-parent).it may have zero or more child nodes. used for fie systems, XML/HTML parsing

binary tree each node has most two children. used for searching and sorting algorithms, expression parsing, 
decision-making processes, and hierarchical data representation. each node has  1 and 0. its type of tree. 

use cases

"""



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    
    def print_list(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
            
    def length(self):
        current=self.head
        c=0
        while current:
            c+=1
            current=current.next
        return c

    def search(self,item):
        current=self.head
        while current:
            if current.data == item:
                return True
            current=current.next
        return False
    
    def delete(self,key):
        if self.head is  None:
            return
        if self.head.data == key:
            self.head=self.head.next
            return
        current=self.head
        while current.next:
            if current.next.data == key:
                current.next=current.next.next
                return
            current=current.next


    def sum(self):
        current=self.head
        c=0
        while current:
            c+=current.data
            current=current.next
        return c





lk=LinkedList();
lk.append(10)
lk.append(101)
lk.append(102)
lk.print_list()
print(lk.search(101))
