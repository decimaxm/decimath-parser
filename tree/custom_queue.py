# TODO: to be reimplemented with Linked List
from typing import TypeVar, Generic

T = TypeVar("T")
""" FIFO structure """
class Queue(Generic[T]):
    """ creates a shallow copy of elements in reversed order"""
    def __init__(self, elements: list[T] = []):
        self.elements = []
        for element in elements:
            self.insert(element)

    """ insert element in front of the others """
    def insert(self, element: T) -> None:
        self.elements.insert(0, element)
    
    """ extract the element in the back of the queue"""
    def pop(self) -> T:
        return self.elements.pop()
    
    """ print the content of the queue from left (most recent added) to right """
    def print_queue(self) -> None:
        print(self.elements)

    def __len__(self):
        return len(self.elements)