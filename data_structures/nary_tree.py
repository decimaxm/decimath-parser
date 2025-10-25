from typing import List, Optional
from custom_queue import Queue
import os
import math

class Node:
    """ node of a tree """
    def __init__(self, value: str | int, children: Optional[List["Node"]] = []):
        self.value = value 
        self.children = children[:]

    def get_value(self):
        return self.value
    
    def set_value(self, value: str | int):
        self.value = value

    def add_child(self, node: "Node", index: int = None):
        if index is None:
            index = len(self.children)
        self.children.insert(index, node)

    def remove_child(self, index: int =-1):
        if len(self.children) > 0 and len(self.children) < index:
            self.children.pop(index)

    def update_child(self, index: int, value: str | int):
        l = len(self.children)
        if l > 0 and abs(index) < l:
            self.children[index].value = value
        else:
            raise KeyError("Index not found")

    def print_node(self, endline=None):
        print(self.value, end=endline)

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)
    
    def get_number_of_children(self):
        return len(self.children)
    
class UnorderedNaryTree:
    """ unbalanced unordered tree """
    def __init__(self, root: Node | None = None, n: int = 2):
        self.root = root 
        self.n = n

    #TODO: add check to n -> make all Node methods private and wrap within the Tree functions. 
    # if a node has already n children, raise an error
    # until then, if you want to create a tree, create raw Nodes and add children directly to them

    def print_tree(self):
        BRANCH_HEIGHT = 4
        terminal_length = os.get_terminal_size().columns

        imposed_terminal_length = 2**math.floor(math.log2(terminal_length))
        #imposed_terminal_length = terminal_length
        print(imposed_terminal_length*"_")
        level = 0
        if not isinstance(self.root, Node):
            raise Exception("This three hasn't a valid root")
        prev_mod = {}
        queue = Queue[Node]()
        blank_queue = Queue[Node]()
        queue.enqueue(self.root)
        queue.enqueue(Node("\n"))
        internal_counter = 0
        max_slots_level = 2**level
        slot_length = imposed_terminal_length // max_slots_level
        slot_middle_r = slot_length//2
        while len(queue) > 0:
            node = queue.dequeue()
            node_value = str(node)
            length = len(node_value)
            

            if node.value != '\n':
                start_slot = slot_length * internal_counter
                padding = (slot_length - length)/2
                to_print = math.floor(padding)*" "+node_value+math.ceil(padding)*" "
                internal_counter = internal_counter+1
                print(to_print, end="")
            else:
                level = level+1
                internal_counter = 0
                print()
                if len(queue) > 0:
                    for _ in range(BRANCH_HEIGHT):
                        for _ in range(max_slots_level):
                            print(math.floor(slot_middle_r-1)*" "+"|"+math.ceil(slot_middle_r)*" ", end="")
                        print()
                    max_slots_level = 2**level
                    slot_length = imposed_terminal_length // max_slots_level
                    slot_middle_r = slot_length//2
                    for _ in range(max_slots_level//2):
                        print(math.floor(slot_middle_r-1)*" "+
                              "/"+(slot_length-1)*"-"+"\\"
                              +math.ceil(slot_middle_r)*" ", end="")
                    print()
                    for _ in range(BRANCH_HEIGHT//2):
                        for _ in range(max_slots_level):
                            print(math.floor(slot_middle_r-1)*" "+"|"+math.ceil(slot_middle_r)*" ", end="")
                        print()
                    queue.enqueue(Node("\n"))
                
            l = len(node.children) 
            if l > 0:
                if len(blank_queue) > 0:
                    while len(blank_queue) > 0:
                        queue.enqueue(blank_queue.dequeue())
                for child in node.children:
                    queue.enqueue(child)
            if node_value != '\n' \
                and l < self.n:
                    for _ in range(l, self.n):
                        blank_queue.enqueue(Node("_"))
            #elif node_value == "_":
            #    for _ in range(self.n):
            #        queue.enqueue(Node("_"))
                


# Livello 4 (foglie)
n1  = Node(1)
n2  = Node(2)
n3  = Node(3)
n4  = Node(4)
n5  = Node(5)
n6  = Node(6)
n7  = Node(7)
n8  = Node(8)
n9  = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)
n14 = Node(14)
n15 = Node(15)
n15b = Node("15b")

# Livello 3
n16 = Node(16, [n1, n2])
n17 = Node(17)#, [n3, n4])
n18 = Node(18, [n5, n6])
n19 = Node(19, [n7, n8])
#n19 = Node(19, [n7])
n20 = Node(20, [n9, n10])
n21 = Node(21, [n11, n12])
n22 = Node(22, [n13, n14])
n23 = Node(23, [n15, n15b])   # un figlio solo per testare un caso asimmetrico

# Livello 2
n24 = Node(24, [n16, n17])
n25 = Node(25, [n18, n19])
n26 = Node(26)#, [n20, n21])
#n26 = Node(26, [n20, n21])
#n26 = Node(26, [n20])
n27 = Node(27, [n22, n23])
#n27 = Node(27, [n22])

# Livello 1 (radice)
root = Node(99, [n24, n25])
right_root = Node(100, [n26, n27])

# Livello 0 (super-radice)
super_root = Node(200, [root, right_root])
# Costruisci l’albero
tree = UnorderedNaryTree(super_root)
tree.print_tree()
