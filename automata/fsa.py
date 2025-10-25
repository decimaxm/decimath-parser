import State 
from pathlib import Path


INITIAL_STATE = 'q0'

class FSA:
    '''Class implementing Finite State Automata'''
    
    def __init__(self, name : str):
        self.name = name
        self.__head = INITIAL_STATE
        self.__states = {INITIAL_STATE: State(INITIAL_STATE)} # I'm thinking about implementing it with a SET...  
        self.__transactions = {}
        self.__acceptance_states = set()

    def add_state(self, name : str):
        if name not in self.states.keys():
            raise KeyError(f"State {name} already exists")
        self.states[name] = State(name)


    # TODO: maybe implement input with a TOKEN class instead of STRING
    def add_transaction(self, start_state : str, input : str, final_state: str):
        if not isinstance(start_state, str) or not isinstance(input, str) or not isinstance(final_state, str):
            raise TypeError("Check input type")
        
        if start_state not in self.__states.keys():
            raise KeyError(f"Selected state {start_state} does not exist")

        if final_state not in self.__states.keys():
            raise KeyError(f"Selected state {final_state} does not exist")

        if (start_state, input) not in self.__transactions.keys():
            self.__transactions[(start_state, input)] = final_state
        else:
            raise KeyError(f"Transaction {(start_state, input)} already defined")
        
    def set_final(self, final_state : str | list):
        if not isinstance(final_state, str) and not isinstance(final_state, list):
            raise TypeError("You must pass a state name or a list of state names")
    
        if isinstance(final_state, str):
            if final_state not in self.__states.keys():
                raise KeyError(f"State {final_state} doesn't exist")
            # TODO: this isn't really needed because atm the acceptance set is implemented as a SET. Anyway, it won't harm
            elif final_state in self.__acceptance_states:
                raise KeyError(f"State {final_state} is already final")
            else:
                self.__acceptance_states.add(final_state)

    def move(self, input : str):
        if (self.__head, input) in self.__transactions.keys():
            self.__head = self.__transactions[(self.__head, input)]

    def check_acceptance(self):
        return self.__head in self.__acceptance_states

    
    #TODO
    def __check_reachable_states(self):
        pass
    #TODO
    def parse_yaml(self, path : Path):
        '''create a FSA from YAML configuration file'''
        pass

    #TODO
    def dump_yaml(self, path : Path):
        '''dump the FSA configuration in a YAML file'''
    