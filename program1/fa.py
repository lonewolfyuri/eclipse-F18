# Submitter: ggabrich(Gabricht, George)

from goody import safe_open


def read_fa(file : open) -> {str:{str:str}}:
    new_fa = dict()
    for line in file:
        data = line.rstrip().split(';')
        zip_data = zip(data[1::2], data[2::2])
        new_fa[data[0]] = {entry[0]: entry[1] for entry in zip_data}
    return new_fa
            
def read_inputs(file : open) -> [(str, [str])]:
    new_inputs = []
    for line in file:
        data = line.rstrip().split(';')
        new_inputs.append((data[0], data[1:]))
    return new_inputs

def fa_as_str(fa : {str:{str:str}}) -> str:
    fa_str, sorted_fa = '', [(state[0], sorted(state[1].items())) for state in sorted(fa.items())]
    for state, trans in sorted_fa: fa_str += f'  {state} transitions: {trans}\n'
    return fa_str


    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    current, result = state, [state] if state in fa else [None]
    if not result[0]: return result
    for trans in inputs:
        if trans not in fa[current]: 
            result.append((trans, None))
            break
        current = fa[current][trans]
        result.append((trans, current))
    return result

def interpret(fa_result : [None]) -> str:
    stop, interpret_str = '', ''
    for step in fa_result:
        if not step: return interpret_str + f'Start state = {step}\nIllegal Start state: simulation terminated\n'
        elif type(step) is not type(tuple()): interpret_str += f'Start state = {step}\n'
        elif not step[1]: return interpret_str + f'  Input = {step[0]}; illegal input: simulation terminated\nStop state = None\n'
        else: stop, interpret_str = step[1], interpret_str + f'  Input = {step[0]}; new state = {step[1]}\n'
    return interpret_str + f'Stop state = {stop}\n'


if __name__ == '__main__':
    # Write script here
    fa_dict = read_fa(safe_open('Choose the file name representing the finite automaton ', 'r','Invalid File Name', default='faparity.txt'))
    print('', 'The Description of the chosen Finite Automaton', fa_as_str(fa_dict), sep='\n', end='\n')
    fa_inputs = read_inputs(safe_open('Choose the file name representing the start-states and their inputs ', 'r', 'Invalid File Name', default='fainputparity.txt'))   
    for fa_start, fa_input in fa_inputs: print(f'\nBegin tracing the next FA simulation\n{interpret(process(fa_dict, fa_start, fa_input))}', end='')
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc3.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
