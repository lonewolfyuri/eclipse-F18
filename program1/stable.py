# Submitter: ggabrich(Gabricht, George)

import prompt
from collections import defaultdict
from goody import safe_open

# Use these global variables to index the list associated with each name in the dictionary.
# e.g., if men is a dictionary, men['m1'][match] is the woman who matches man 'm1', and 
# men['m1'][prefs] is the list of preference for man 'm1'.
# It would seems that this list might be better represented as a named tuple, but the
# preference list it contains is mutated, which is not allowed in a named tuple. 

match = 0   # Index 0 of list associate with name is match (str)
prefs = 1   # Index 1 of list associate with name is preferences (list of str)


def read_match_preferences(open_file : open) -> {str:[str,[str]]}:
    match_dict = defaultdict(list)
    for line in open_file:
        line_split = line.rstrip().split(';')
        match_dict[line_split[0]].append(None)
        match_dict[line_split[0]].append(line_split[1:])
    return dict(match_dict)
    


def dict_as_str(d : {str:[str,[str]]}, key : callable=None, reverse : bool=False) -> str:
    dict_str, sorted_list = '', [(person, d[person]) for person in sorted(d, key=key, reverse=reverse)]
    for person, vals in sorted_list: dict_str += f'  {person} -> {vals}\n'
    return dict_str
        


def who_prefer(order : [str], p1 : str, p2 : str) -> str:
    return (p1 if order.index(p1) < order.index(p2) else p2)


def extract_matches(men : {str:[str,[str]]}) -> {(str,str)}:
    return {(man, men[man][match]) for man in men}


def make_match(men : {str:[str,[str]]}, women : {str:[str,[str]]}, trace : bool = False) -> {(str,str)}:
    print()
    new_men, unmatched = men.copy(),  {man for man in men}
    if trace: print(f'Women Preferences (unchanging)\n{dict_as_str(women)}')
    while unmatched != set():
        if trace: print(f'Men Preferences (current)\n{dict_as_str(men)}',f'unmatched men = {unmatched}\n',sep='\n')
        man = unmatched.pop()
        propose = new_men[man][prefs].pop(0)
        if women[propose][match] == None: 
            if trace: print(f'{man} proposes to {propose}, who is currently unmatched, accepting the proposal\n')
            new_men[man][match] = propose
            women[propose][match] = man
        else: 
            new_match = who_prefer(women[propose][prefs], man, women[propose][match])
            if women[propose][match] != new_match:
                if trace: print(f'{man} proposes to {propose}, who is currently matched, accepting the proposal, rejecting match with {women[propose][match]}\n')
                new_men[women[propose][match]][match] = None
                unmatched.add(women[propose][match])
            else:
                if trace: print(f'{man} proposes to {propose}, who is currently matched, rejecting the proposal (likes current match better)\n') 
                unmatched.add(man)
            new_men[new_match][match] = propose
            women[propose][match] = new_match     
    return extract_matches(new_men)


  
    
if __name__ == '__main__':
    # Write script here
    men = read_match_preferences(safe_open("Choose the file name representing the men ", 'r', 'Invalid File Name', default='men0.txt'))
    women = read_match_preferences(safe_open("Choose the file name representing the women ", 'r', 'Invalid File Name', default='women0.txt'))   
    print('', 'Men Preferences', dict_as_str(men), 'Women Preferences', dict_as_str(women), sep='\n', end='\n')
    print(f'matches = {make_match(men, women, prompt.for_bool("Choose whether to trace this algorithm ", default = True, error_message="Invalid Entry: Please enter a True or False"))}')       
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
