class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def __str__(self):
        return str(self.val)

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, val):
    newNode = Node(val)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode

  def printLL(self):
    current = self.head
    while(current):
      print(current.val, '-> ', current.next)
      current = current.next

LL = LinkedList()
LL.insert(1)
LL.insert(2)
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
# class LinkedList:
#     def __init__(self, vals=None):
#         self.head = None
#         self.tail = None
#         if vals is not None:
#             self.add_multiple_nodes(vals)
            
#     def __str__(self):
#         return ' -> '.join([str(node) for node in self])
    
#     def __len__(self):
#         count = 0
#         node = self.head
#         while node:
#             count += 1
#             node = node.next
#         return count
    
#     def __iter__(self):
#         current = self.head
#         while current:
#             yield current
#             current = current.next
            
#     @property
#     def vals(self):
#         return [node.val for node in self]
    
#     def add_node(self, val):
#         if self.head is None:
#             self.tail = self.head = Node(val)
#         else:
#             self.tail.next = Node(val)
#             self.tail = self.tail.next
#         return self.tail
    
#     def add_multiple_nodes(self, vals):
#         for val in vals:
#             self.add_node(val)

#     def add_node_as_head(self, val):
#         if self.head is None:
#             self.tail = self.head = Node(val)
#         else:
#             self.head = Node(val, self.head)
#         return self.head

