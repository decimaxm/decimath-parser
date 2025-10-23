from typing import List, Optional
from custom_queue import Queue
import os
import math

class Node:
    """ node of a tree """
    def __init__(self, value: str | int, children: Optional[List["Node"]] = []):
        self.value = value 
        self.children = children[:]

    def add_child(self, node: "Node", index: int = None):
        if index is None:
            index = len(self.children)
        self.children.insert(index, node)

    def remove_child(self, index: int =-1):
        if len(self.children) > 0 and len(self.children) < index:
            self.children.pop(index)

    def update_child(self, index: int, value: str | int):
        if len(self.children) > 0 and len(self.children) < index:
            self.children[index].value = value

    def print_node(self, endline=None):
        print(self.value, end=endline)

    def __str__(self):
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
        terminal_length = os.get_terminal_size().columns #* 0.75
        print(terminal_length*"_")
        level = 0
        if not isinstance(self.root, Node):
            raise Exception("This three hasn't a valid root")
        prev_mod = {}
        queue = Queue[Node]()
        queue.enqueue(self.root)
        queue.enqueue(Node("\n"))
        internal_counter = 0
        while len(queue) > 0:
            node = queue.dequeue()
            length = len(str(node))
            half = terminal_length//2
            mod = terminal_length % 2
            adjustments = {i:0 for i in prev_mod.keys()}
            if node.value != '\n':
                
                left_mod = math.floor(length/2)
                right_mod = math.ceil(length/2)
                left_padding = half-left_mod-1
                right_padding = half-right_mod+mod-1
                adjustments = {i: prev_mod[i] for i in prev_mod.keys() if (internal_counter+1)%(2**(level-i)) == 0}
                #if sum(adjustments.values()) == 1:
                if len(adjustments.values()) > 0 and adjustments[min(adjustments.keys())] == 1:
                    adjust = 1
                else:
                    adjust = 0
                #to_print = "|"+left_padding*" "+str(node)+right_padding*" "+"|"+adjust*"^^"
                to_print = " "+left_padding*" "+str(node)+right_padding*" "+" "+adjust*"  "
                internal_counter = internal_counter+1
            else:
                to_print = node
            print(to_print, end="")
            l = len(node.children) 
            if l > 0:
                for child in node.children:
                    queue.enqueue(child)
                if node.value != '\n' \
                    and node.value != "_" \
                    and l < self.n:
                        for _ in range(l, self.n):
                            queue.enqueue(Node("_"))
            if node.value == '\n' and len(queue) > 0:
                prev_mod[level] = mod
                level = level+1
                queue.enqueue(Node("\n"))
                terminal_length = half
                internal_counter = 0
                


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
n17 = Node(17, [n3, n4])
n18 = Node(18, [n5, n6])
#n19 = Node(19, [n7, n8])
n19 = Node(19, [n7])
n20 = Node(20, [n9, n10])
n21 = Node(21, [n11, n12])
n22 = Node(22, [n13, n14])
n23 = Node(23, [n15, n15b])   # un figlio solo per testare un caso asimmetrico

# Livello 2
n24 = Node(24, [n16, n17])
n25 = Node(25, [n18, n19])
n26 = Node(26, [n20, n21])
#n27 = Node(27, [n22, n23])
n27 = Node(27, [n22])

# Livello 1 (radice)
root = Node(99, [n24])#, n25])
right_root = Node(100, [n26, n27])

# Livello 0 (super-radice)
super_root = Node(200, [root, right_root])

# Costruisci l’albero
tree = UnorderedNaryTree(super_root)
tree.print_tree()
#|                       99                       |
#|                       100                      |