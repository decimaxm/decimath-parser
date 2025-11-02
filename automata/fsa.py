from .dstate import DState
from utils.dynamic_programming import memoize_method
from pathlib import Path

INITIAL_STATE = 'q0'

class FSA:
    '''Class implementing Finite State Automata'''
    
    def __init__(self, name : str):
        self.name = name
        self.__head = INITIAL_STATE
        self.__states = {INITIAL_STATE: DState(INITIAL_STATE)} # I'm thinking about implementing it with a SET...  
        self.__transitions = {}
        self.__acceptance_states = set()

    #TODO: should also create a wrapper for adding more states through a list
    def add_state(self, name : str):
        '''Add a new state to the FSA, without transitions'''
        if name in self.__states.keys():
            raise KeyError(f"State {name} already exists")
        self.__states[name] = DState(name)

    # TODO: maybe implement input with a TOKEN class instead of STRING
    def add_transition(self, start_state : str, input_str : str, final_state: str):
        '''Add a transition between state start_state and final_state when input_str is read'''
        if not isinstance(start_state, str) or not isinstance(input_str, str) or not isinstance(final_state, str):
            raise TypeError("Check input type")
        
        if start_state not in self.__states.keys():
            raise KeyError(f"Selected state {start_state} does not exist")

        if final_state not in self.__states.keys():
            raise KeyError(f"Selected state {final_state} does not exist")

        if (start_state, input_str) not in self.__transitions.keys():
            self.__transitions[(start_state, input_str)] = final_state
            # clear mappability cache at least for final_state
        else:
            raise KeyError(f"transition {(start_state, input_str)} already defined")
    
    def _set_final(self, final_state : str):
        '''Set a state as final'''
        #TODO: should I put also an unset_final? When would it be used?
        if isinstance(final_state, str):
            if final_state not in self.__states.keys():
                raise KeyError(f"State {final_state} doesn't exist")
            # TODO: this isn't really needed because atm the acceptance set is implemented as a SET. Anyway, it won't harm
            elif final_state in self.__acceptance_states:
                raise KeyError(f"State {final_state} is already final")
            else:
                self.__acceptance_states.add(final_state)
        else:
            raise TypeError("Final state should be a string")
        
    def set_final(self, final_state : str | list):
        '''Wrapper for _set_final()'''
        if not isinstance(final_state, str) and not isinstance(final_state, list):
            raise TypeError("You must pass a state name or a list of state names")
    
        if isinstance(final_state, str):
            self._set_final(final_state)
        elif isinstance(final_state, list):
            for state in final_state:
                self._set_final(state)

    def move_head(self, input_str : str):
        '''Set the head to the new state based on `input_str`, current state and transitions of the FSA'''
        if (self.__head, input_str) in self.__transitions.keys():
            self.__head = self.__transitions[(self.__head, input_str)]

    def check_acceptance(self):
        '''Check that the head is in a final state'''
        return self.__head in self.__acceptance_states

    @memoize_method
    def __check_reachable_state(self, name : str) -> bool:
        '''Checks whether a single state is reachable or not'''
        # main idea: check reachability recursively
        # if exists a transition from state A to state B and A is reachable, B is reachable too
        
        if name == INITIAL_STATE:
            return True
        # check that B is reachable from ANY state
        else: 
            #TODO: definitely to be optimized! Here I'm doing a FULL SCAN of the dict (hash is on keys, not on values) -> O(n) -> not good for performance
            #scan the transition dict to get transitions immediately leading to the state and put them in a set 
            predecessors = {k[0] for k,v in self.__transitions.items() if v == name} 
            if len(predecessors) > 0:
                for pred in predecessors:
                    if self.__check_reachable_state(pred):
                        return True
            
            return False
    #TODO
    def __check_reachable_states(self):
        '''Check that each state is reachable'''
        pass
    
    #TODO
    def parse_yaml(self, path : Path):
        '''create a FSA from YAML configuration file'''
        pass

    #TODO
    def dump_yaml(self, path : Path):
        '''dump the FSA configuration in a YAML file'''
    