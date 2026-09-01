# Lab ระหว่างเรียน ส่วนที่ 1: โครงสร้างพื้นฐานและการสำรวจ (Singly Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse_singly(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end= " ->")
        currentNode = currentNode.next
    print("null")
    pass

print("--- ผลลัพธ์ส่วนที่ 1: Singly Linked List ---")
# HINT 3: การเชื่อมโหนด (Linking) ควรสร้าง object ของ Node ให้ครบทุกตัวก่อน 
# แล้วค่อยจับคู่โดยระบุว่า node.next ชี้ไปที่ใคร[cite: 1]

# TODO: สร้างโหนดข้อมูล Integer 4 ตัว ได้แก่ 9, 1, 7, 8 และเชื่อมโยง (link) เข้าด้วยกัน
node1 = Node(9)
node2 = Node(1)
node3 = Node(7)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

traverse_singly(node1)