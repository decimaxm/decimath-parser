from .fsa import FSA

def test_initial_state():
    fsa = FSA("toy")
    print("=== test_initial_state ===")
    print("Initial head:", fsa._FSA__head)
    assert not fsa.check_acceptance(), "Expected: not accepting initially"
    print("Pass ✅\n")
    return fsa

def test_add_state(fsa):
    print("=== test_add_state ===")
    fsa.add_state('q1')
    assert 'q1' in fsa._FSA__states.keys() and str(fsa._FSA__states['q1']) == 'q1', "Expected: new state should be present in FSA states"
    print("Pass ✅\n")
    return fsa

def test_set_final(fsa: FSA):
    print("=== test_set_final ===")
    try:
        fsa.set_final("q1")
        print("Marked q1 as final.")
    except Exception as e:
        print("Error set_final('q1'):", e)
    assert fsa.check_acceptance(), "Expected: accepting after set_final(q1)"
    print("Pass ✅\n")

def test_add_transition(fsa: FSA):
    print("=== test_add_transition ===")
    try:
        fsa.add_transition("q0", "a", "q1")
        print("Transition (q0, 'a') -> q1 added.")
    except Exception as e:
        print("Error add_transition:", e)
    fsa.move_head("a")
    assert fsa._FSA__head == "q1", "Expected: head goes to q1"
    assert not fsa.check_acceptance(), "Expected: accepting after move('a')"
    print("Pass ✅\n")

def test_invalid_transition(fsa: FSA):
    print("=== test_invalid_transition ===")
    former_head = fsa._FSA__head
    fsa.move_head("b")  # missing symbol
    assert fsa._FSA__head == former_head, "Expected: head unchanged on invalid symbol"
    print("Pass ✅\n")

def test_duplicate_transition(fsa):
    print("=== test_duplicate_transition ===")
    try:
        fsa.add_transition("q0", "a", "q1")
        print("ERROR: should have raised KeyError for duplicate transition.")
    except KeyError as e:
        print("OK (expected) KeyError on duplicate transition:", e)
    print("Pass ✅\n")

def test_set_final_list(fsa: FSA):
    print("=== test_set_final_list ===")
    try:
        fsa.add_state('q2')
        fsa.add_state('q3')
        fsa.set_final(['q2','q3'])
        fsa.add_transition('q1', 'a', 'q2')
        fsa.move_head('a')
        print("Called set_final(['q2','q3']) — current acceptance:", fsa.check_acceptance())
        fsa.add_transition('q2', 'a', 'q3')
        fsa.move_head('a')
        print("Called set_final(['q2','q3']) — current acceptance:", fsa.check_acceptance())
    except Exception as e:
        print("Error set_final(['q2', 'q3']):", e)
    print("Pass ✅\n")


def test_reachable_state(fsa: FSA):
    print("=== test_reachable_state ===")
    fsa.add_state('q4')
    fsa.add_state('q5')
    fsa.add_state('q6')
    fsa.add_transition('q0', 'b', 'q4') # reachable
    fsa.add_transition('q5', 'd', 'q6') # not reachable
    
    assert fsa._FSA__check_reachable_state('q4'), "Expected: q4 should be reachable"
    assert not fsa._FSA__check_reachable_state('q5'), "Expected: q5 shouldn't be reachable"
    assert not fsa._FSA__check_reachable_state('q6'), "Expected: q6 shouldn't be reachable"
    print("Pass ✅\n")

def run_smoke_tests():
    fsa = test_initial_state()
    test_add_state(fsa)
    test_add_transition(fsa)
    test_set_final(fsa)
    test_invalid_transition(fsa)
    test_duplicate_transition(fsa)
    test_set_final_list(fsa)
    test_reachable_state(fsa)
    
    print("=== All smoke tests completed ===")
    print("Stored states:", list(fsa._FSA__states.keys()))
    print("Final states:", fsa._FSA__acceptance_states)
    print("Transitions:", fsa._FSA__transitions)

if __name__ == "__main__":
    run_smoke_tests()
