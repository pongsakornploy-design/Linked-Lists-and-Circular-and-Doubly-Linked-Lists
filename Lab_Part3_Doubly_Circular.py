class DoublyNode:

  def __init__(self, data):

      self.data = data

      self.next = None

      self.prev = None

 

class Node:

  def __init__(self, data):

      self.data = data

      self.next = None

 

def traverse_forward(head):

  currentNode = head

  while currentNode:

      print(currentNode.data, end=" -> ")

      currentNode = currentNode.next

  print("null") #[cite: 1]

 

def traverse_backward(tail):

  currentNode = tail

  while currentNode:

      print(currentNode.data, end=" -> ")

      currentNode = currentNode.prev

  print("null") #[cite: 1]

 

def traverse_circular_singly(head):

  if not head:

      return

  currentNode = head

  startNode = head

  print(currentNode.data, end=" -> ")

  currentNode = currentNode.next

  while currentNode != startNode:

      print(currentNode.data, end=" -> ")

      currentNode = currentNode.next

  print("...") #[cite: 1]

 

def traverse_circular_doubly_forward(head):

  if not head:

      return

  currentNode = head

  startNode = head

  print(currentNode.data, end=" -> ")

  currentNode = currentNode.next

  while currentNode != startNode:

      print(currentNode.data, end=" -> ")

      currentNode = currentNode.next

  print("...") #[cite: 1]

 

def traverse_circular_doubly_backward(tail):

  if not tail:

      return

  currentNode = tail

  startNode = tail

  print(currentNode.data, end=" -> ")

  currentNode = currentNode.prev

  while currentNode != startNode:

      print(currentNode.data, end=" -> ")

      currentNode = currentNode.prev

  print("...") #[cite: 1]

 

print("--- ผลลัพธ์ส่วนที่ 3: Doubly & Circular ---")

print("\n[Doubly Linked List]")

dnode1 = DoublyNode(3)

dnode2 = DoublyNode(5)

dnode3 = DoublyNode(13)

 

dnode1.next = dnode2

dnode2.prev = dnode1

dnode2.next = dnode3

dnode3.prev = dnode2 #[cite: 1]

 

print("Traversing forward:")

traverse_forward(dnode1)

print("Traversing backward:")

traverse_backward(dnode3)

 

 

print("\n[Circular Singly Linked List]")

cnode1 = Node(3)

cnode2 = Node(5)

cnode3 = Node(13)

 

cnode1.next = cnode2

cnode2.next = cnode3

cnode3.next = cnode1 #[cite: 1]

 

traverse_circular_singly(cnode1)

 

 

print("\n[Circular Doubly Linked List]")

cdnode1 = DoublyNode(3)

cdnode2 = DoublyNode(5)

cdnode3 = DoublyNode(13)

cdnode4 = DoublyNode(2) #[cite: 1]

 

# เชื่อมโหนดแบบ Doubly ปกติ

cdnode1.next = cdnode2

cdnode2.prev = cdnode1

cdnode2.next = cdnode3

cdnode3.prev = cdnode2

cdnode3.next = cdnode4

cdnode4.prev = cdnode3 #[cite: 1]

 

# เชื่อมโหนดสุดท้ายและโหนดแรกเข้าด้วยกันเพื่อสร้างวงกลม (Circular)

cdnode4.next = cdnode1 #[cite: 1]

cdnode1.prev = cdnode4 #[cite: 1]

 

print("Traversing forward:")

traverse_circular_doubly_forward(cdnode1)

print("Traversing backward:")

traverse_circular_doubly_backward(cdnode4)


