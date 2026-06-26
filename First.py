
from collections import deque

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue: #support_queue (waiting line)
    def __init__(self):
        self.head=None
    
    def enqueue(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node
    
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


support_queue = Queue()
resolved_stack = Stack()

#costumers arrive
support_queue.enqueue("Ticket #1: Password Reset")
support_queue.enqueue("Ticket #2: Billing Error")
support_queue.enqueue("Ticket #3: App Crashing")

print("--- INITIAL WAITING QUEUE ---")
support_queue.print()


#finish ticket 1
done_ticket1 = support_queue.dequeue()
resolved_stack.push(done_ticket1)

done_ticket2=support_queue.dequeue()
resolved_stack.push(done_ticket2)

print("\n--- QUEUE AFTER AGENT WORKS ---")
support_queue.print()

print("\n--- RECENTLY RESOLVED HISTORY (STACK) ---")
resolved_stack.print()