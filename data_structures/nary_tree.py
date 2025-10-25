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
        n = self.n
        terminal_length = os.get_terminal_size().columns

        imposed_terminal_length = n**math.floor(math.log(terminal_length, n))
        #imposed_terminal_length = terminal_length

        print(imposed_terminal_length*"_")
        level = 0
        if not isinstance(self.root, Node):
            raise Exception("This three hasn't a valid root")
        
        queue = Queue[Node]()
        blank_queue = Queue[Node]()
        queue.enqueue(self.root)
        queue.enqueue(Node("\n"))

        internal_counter = 0
        max_slots_level = n**level
        slot_length = imposed_terminal_length // max_slots_level
        slot_middle_r = slot_length/2

        while len(queue) > 0:
            node = queue.dequeue()
            node_value = str(node)
            length = len(node_value)
            
            if node.value != '\n':
                padding = (slot_length - length)/2
                print(math.floor(padding)*" "+node_value+math.ceil(padding)*" ", end="")
                internal_counter = internal_counter+1
            else:
                level = level+1
                internal_counter = 0
                print()
                if len(queue) > 0:

                    # print second half of the tree branches UNDER the nodes
                    for _ in range(BRANCH_HEIGHT):
                        for _ in range(max_slots_level):
                            print(math.floor(slot_middle_r-1)*" "+"|"+math.ceil(slot_middle_r)*" ", end="")
                        print()

                    # compute values for the next level
                    max_slots_level = n**level
                    slot_length = imposed_terminal_length // max_slots_level
                    slot_middle_r = slot_length/2

                    # print horizontal branches 
                    for _ in range(max_slots_level//n):
                        print(math.floor(slot_middle_r-1)*" "+"/"+((slot_length-1)*(n-1)+n%2)*"-"+"\\"+math.ceil(slot_middle_r)*" ", end="")
                    print()

                    # print first half of the NEXT tree branches, OVER the future nodes
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
                


