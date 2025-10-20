# TODO: to be reimplemented with Linked List
from typing import TypeVar, Generic, Optional

T = TypeVar("T")
class Stack(Generic[T]):
    """ LIFO structure """

    # TODO: implement internal elements trought @properties
    def __init__(self, name: str = "Stack0", elements: Optional[list[T]] = None):
        """ creates a shallow copy of elements in reversed order"""
        if isinstance(name, str):
            self.__name = name
        self.__elements = []
        if isinstance(elements, list):
            if elements:
                for element in elements:
                    self.push(element)
        else:
            raise TypeError("elements should be a list")

    def push(self, element: T) -> None:
        """ insert element in front of the others """
        self.__elements.append(element)
    
    

    def pop(self) -> T:
        """ extract the element from the head of the stack"""
        if not self.__elements:
            raise IndexError("The stack is empty")
        else:
            return self.__elements.pop()
        
    
    def __repr__(self) -> None:
        """ print the content of the stack from top (most recent added) to bottom """
        return str(self.__elements)
    
    def print_stack(self) -> None:
        """ pretty print """
        elements = self.__elements

        print(f"\nContent of {self.__name} stack: \n")
        if not elements:
            print("| (empty) |")
            return

        idx_width = len(str(len(elements) - 1))
        val_width = max(len(str(e)) for e in elements)
        total_width = idx_width + val_width + 7 

        for off, item in enumerate(reversed(elements)):
            idx = len(elements) - 1 - off
            line = f"| {idx:>{idx_width}} | {str(item).ljust(val_width)} |"
            print(line)
            print("-" * total_width)

    def __len__(self):
        return len(self.__elements)








