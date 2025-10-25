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
        """ Pretty-print the content of the tree"""
        # define two utility functions for a clearer code
        def print_vertical_branches(slot_length : int, max_slots_level: int, branch_height: int = 2):
            half_slot = slot_length/2
            for _ in range(branch_height):
                for _ in range(max_slots_level):
                    # vertical branches must have distance equal to slot length - 1
                    # the first vertical branch should begin half a slot after the terminal left edge
                    print(math.ceil(half_slot)*" "+"|"+math.floor(half_slot-1)*" ", end="")
                print()

        def print_horizontal_branch(slot_length : int, level: int, n: int):
            half_slot = slot_length / 2
            for _ in range(n**(level-1)):
                # every horizontal branch must have (n-1) whole slots of '-' and be sorrounded by 2 half slots -> total: SL/2*" " + SL*(N-1)*"-" + SL/2*" " = SL*N
                # math proof of concept: be SL the slot length
                #                   SL/2      + 1(/) +   SL      *(N-1)- 1     +1(\)            + SL/2 - 1              = SL + (SL)*(N-1) = SL*N
                print(math.ceil(half_slot)*" "+"/"+((slot_length)*(n-1)-1)*"-"+"\\"+math.floor(half_slot-1)*" ", end="")
                        
            print()

        n = self.n
        level = 0
        queue = Queue[Node]()
        blank_queue = Queue[Node]()
        queue.enqueue(self.root)
        queue.enqueue(Node("\n"))

        terminal_length = os.get_terminal_size().columns
        imposed_terminal_length = n**math.floor(math.log(terminal_length, n))

        print(imposed_terminal_length*"_")

        max_slots_level = n**level
        slot_length = imposed_terminal_length // max_slots_level

        while len(queue) > 0:
            node = queue.dequeue()
            node_value = str(node)
            length = len(node_value)
            
            if node_value != '\n':
                # print content of the node
                padding = (slot_length - length)/2
                print(math.ceil(padding)*" "+node_value+math.floor(padding)*" ", end="")

            else:
                level = level+1
                print()
                if len(queue) > 0:

                    # print second half of the tree branches UNDER the nodes
                    print_vertical_branches(slot_length=slot_length, max_slots_level=max_slots_level)

                    # compute values for the next level
                    max_slots_level = n**level 
                    slot_length = imposed_terminal_length // max_slots_level

                    # print horizontal branches 
                    print_horizontal_branch(slot_length=slot_length, level=level, n=n)

                    # print first half of the NEXT tree branches, OVER the future nodes
                    print_vertical_branches(slot_length=slot_length, max_slots_level=max_slots_level)

                    # before inserting a \n node, if the tree is not finished yet spill the blanks inside the main queue
                    if len(blank_queue) > 0:
                        while len(blank_queue) > 0:
                            queue.enqueue(blank_queue.dequeue())
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
                        # if the node has less than n nodes, put the other ones as blanks, so that the print is easier
                        # in order to avoid an infinite loop, a buffer queue is used to temporarily the list of _
                        # the content of this queue will be read only if it is necessary
                        blank_queue.enqueue(Node("_"))
                


