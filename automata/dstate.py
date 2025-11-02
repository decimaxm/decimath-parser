class DState:

    def __init__(self, name):
        self.name = name


    def __repr__(self):
        return self.name
    
    def print_state(self):
        print("-"*(len(self.name)+4))
        print(f"| {self.name} |")
        print("-"*(len(self.name)+4))
