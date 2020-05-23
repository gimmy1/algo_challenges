class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node("Dummy")
        self.tail = Node("Dummy")
        self.head.next = self.tail

        self.tail.prev = self.head


    def set_head(self, value):
        new_node = Node(value)
        if self.head.next == self.tail:
            self.head.next = new_node
            new_node.next = self.tail
            new_node.prev = self.head
            self.tail.prev = new_node
        else:
            previous_head = self.head.next
            self.head.next = new_node
            new_node.next = previous_head
            previous_head.prev = new_node
            new_node.prev = self.head
    
    def set_tail(self, value):
        # edge case
        if self.tail.prev == self.head:
            self.set_head(value)
        else:
            new_tail = Node(value) # create new node
            previous_tail = self.tail.prev # reference previous tail
            self.tail.prev = new_tail # set new previous tail to new_tail
            new_tail.prev = previous_tail # new_tail previous points to previous tail
            previous_tail.next = new_tail # previous tail next points to new tail
            new_tail.next = self.tail # new tail next points to tail
        
    def insert_before(self, v, n):
        new_node = Node(n)
        curr = self.head.next
        while curr.next:
            if curr.next.value == v:
                # set the next to be equal to the new_node
                next_value = curr.next
                curr.next = new_node
                new_node.prev = curr
                new_node.next = next_value
            curr = curr.next
        return None

    def insert_after(self, v, n):
        new_node = Node(n)
        curr = self.head.next
        while curr.next:
            if curr.value == v:
                next_value = curr.next
                curr.next = new_node
                new_node.prev = curr
                new_node.next = next_value
                next_value.prev = new_node
            curr = curr.next
        return None
    
    def insert_at_position(self, pos, n):
        new_node = Node(n)
        curr = self.head.next
        count = 1
        while curr.next:
            if (count + 1) == pos:
                next_value = curr.next
                curr.next = new_node
                new_node.prev = curr
                new_node.next = next_value
                next_value.prev = new_node
                return
            count += 1
            curr = curr.next
        return False


    def remove_node_with_value(self, v):
        curr = self.head.next
        while curr.next:
            if curr.next.value == v:
                next_next_value = curr.next.next 
                remove_value = curr.next
                curr.next = next_next_value
                next_next_value.prev = curr
                remove_value.prev = None
                remove_value.next = None
                return
            curr = curr.next
        return False
    
    def contains_node_with_value(self, v):
        curr = self.head.next
        while curr.next:
            if curr.value == v:
                return True
            curr = curr.next
        return False
    
    def print_it_out(self):
        curr = self.head.next
        dll = ""
        while curr.next:
            dll += f"{curr.value} <--> "
            curr = curr.next
        print(dll)

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.set_head(5)
    dll.set_head(10)
    dll.set_tail(17)
    dll.set_tail(13)
    dll.insert_before(13, 5)
    dll.insert_after(10, 5)
    dll.insert_at_position(3, 99)
    print(dll.contains_node_with_value(99))
    dll.print_it_out()




        
