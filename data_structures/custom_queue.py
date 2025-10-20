# TODO: to be reimplemented with Linked List
from typing import TypeVar, Generic, Optional

T = TypeVar("T")
class Queue(Generic[T]):
    """ FIFO structure """
    
    def __init__(self, elements: Optional[list[T]] = None):
        """ creates a shallow copy of elements in reversed order"""
        self.__elements: list[T] = []
        if elements:
            for element in elements:
                self.enqueue(element)
    
    def enqueue(self, element: T) -> None:
        """ insert element in front of the others """
        self.__elements.insert(0, element)
    
    def dequeue(self) -> T:
        """ extract the element in the back of the queue"""
        return self.__elements.pop()
    
    def print_queue(self) -> None:
        """ print the content of the queue from left (most recent added) to right """
        print(self.__elements)

    def __len__(self):
        return len(self.__elements)