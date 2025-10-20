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
        terminal_length = os.get_terminal_size().columns

        level = 1
        if not isinstance(self.root, Node):
            raise Exception("This three hasn't a valid root")
        
        queue = Queue[Node]()
        queue.enqueue(self.root)
        queue.enqueue(Node("\n"))
        while len(queue) > 0:
            spaces = math.floor(terminal_length / (math.pow(2,level)))
            node = queue.dequeue()
            if node.value != '\n':
                to_print = spaces*" "+str(node)+spaces*" "
            else:
                to_print = node
            print(to_print, end="")
            if len(node.children) > 0:
                for child in node.children:
                    queue.enqueue(child)
            elif node.value == '\n' and len(queue) > 0:
                level = level+1
                queue.enqueue(Node("\n"))



leftmost_nephew =   Node(8)
second_nephew   =   Node(9)
left_child      =   Node(6, [leftmost_nephew, second_nephew])
third_nephew    =   Node(10)
fourth_nephew   =   Node(11)
right_child     =   Node(7, [third_nephew, fourth_nephew])
root_node       =   Node(5, [left_child, right_child])

tree = UnorderedNaryTree(root_node)
tree.print_tree()
