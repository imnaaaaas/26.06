
from collections import deque

#client comes goes into queue. when agent is done with client, it goes to stack.
#if we want to see last operaiton we do pop.
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue: #support_queue (waiting line)
    def __init__(self):
        self.head=None
        self.tail=None

    #we use tail for optimization O(1) head looks at first,and tail look at last. its add automaticly at back
    def enqueue(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            return
        self.tail.next=new_node #looks after none of last client
        self.tail=new_node #rewrite last to new last user
        """before
        if self.head is None:
            self.head=new_mode
            return
        current=self.head
        while current.next is not None: while loop was O(n) without it it becomes O(1)
            current=current.next
        current.next=new_node
        """

    #working on prioratization



    def dequeue(self):
        if self.head is None:
            return "No users"
        dl_data =self.head.data
        self.head=self.head.next
        return dl_data
    
    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next



class Stack: #resolved_stack 
    def __init__(self):
        self.head=None
    
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if self.head is None:
            return "No Users"
        popped_data=self.head.data
        self.head=self.head.next
        return popped_data
    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next



def reopen_ticket(Queue, Stack):
    return_client = Stack.pop()
    if return_client != "No User:":
        Queue.enqueue(return_client)
        print(f" '{return_client}' reopen and is in queue!")
    else:
        print("history clean, cant add any")


support_queue = Queue()
resolved_stack = Stack()

#costumers arrive
support_queue.enqueue("Ticket #1: Password Reset")
support_queue.enqueue("Ticket #2: Billing Error")
support_queue.enqueue("Ticket #3: App Crashing")



print("--- INITIAL WAITING QUEUE ---")
support_queue.print()


#finish ticket 1
done_ticket1 = support_queue.dequeue() #gives first in queue
resolved_stack.push(done_ticket1) #becomes head

done_ticket2=support_queue.dequeue()#gives second in queue
resolved_stack.push(done_ticket2) #becomes head

print("\n--- QUEUE AFTER AGENT WORKS ---")
support_queue.print() #rigshi dganan

print("\n--- RECENTLY RESOLVED HISTORY (STACK) ---")
resolved_stack.print() #already done clients


#if we want redo and client goes again in queeu
#reopen_ticket(support_queue, resolved_stack)






        #study for 
#space time complexity amortimes time complexity recursions
# memoization 
#dynamic progrmainc algorithm
# divede and cobquer
#duvude
