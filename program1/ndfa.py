# Submitter: ggabrich(Gabricht, George)

from collections import defaultdict
from goody import safe_open


def read_ndfa(file : open) -> {str:{str:{str}}}:
    new_ndfa = dict()
    for line in file:
        data = line.rstrip().split(';')
        zip_data = zip(data[1::2], data[2::2])
        new_ndfa[data[0]] = defaultdict(set)
        for entry in zip_data: new_ndfa[data[0]][entry[0]].add(entry[1])
    return new_ndfa

def read_inputs(file : open) -> [(str, [str])]:
    new_inputs = []
    for line in file:
        data = line.rstrip().split(';')
        new_inputs.append((data[0], data[1:]))
    return new_inputs

def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    ndfa_str, sorted_ndfa = '', [(state[0], sorted(state[1].items())) for state in sorted(ndfa.items())]
    for state, trans in sorted_ndfa:
        trans = [(val[0], sorted(val[1])) for val in trans]
        ndfa_str += f'  {state} transitions: {trans}\n'
    return ndfa_str

       
def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    current, new_poss, poss, result = {state}, set(), set(), [state] if state in ndfa else [None]
    if not result[0]: return result
    for trans in inputs:
        for a_state in current:
            for val in ndfa[a_state]: poss.update(ndfa[a_state][val])
            for a_state in current:
                if trans in ndfa[a_state]: new_poss.update({new_current for new_current in ndfa[a_state][trans] if new_current in poss})
        current, new_poss = new_poss, set()
        result.append((trans, current))
        if current == set(): return result
    return result

def interpret(result : [None]) -> str:
    stop, interpret_str = '', ''
    for step in result:
        # if not step: return interpret_str + f'Start state = {step}\nIllegal Start state: simulation terminated\n'
        if type(step) is not type(tuple()): interpret_str += f'Start state = {step}\n'
        # elif not step[1]: return interpret_str + f'  Input = {step[0]}; illegal input: simulation terminated\nStop state = None\n'
        else: stop, interpret_str = step[1], interpret_str + f'  Input = {step[0]}; new possible states = {sorted(step[1])}\n'
    return interpret_str + f'Stop state(s) = {sorted(stop)}\n'





if __name__ == '__main__':
    # Write script here
    ndfa_dict = read_ndfa(safe_open('Choose the file name representing the non-deterministic finite automaton ', 'r','Invalid File Name', default='ndfaendin01.txt'))
    print('', 'The Description of the chosen Non-Deterministic Finite Automaton', ndfa_as_str(ndfa_dict), sep='\n', end='\n')
    ndfa_inputs = read_inputs(safe_open('Choose the file name representing the start-states and their inputs ', 'r', 'Invalid File Name', default='ndfainputendin01.txt'))   
    for ndfa_start, ndfa_input in ndfa_inputs: print(f'\nBegin tracing the next NDFA simulation\n{interpret(process(ndfa_dict, ndfa_start, ndfa_input))}', end='')          
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc4.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
