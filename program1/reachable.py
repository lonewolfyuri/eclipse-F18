# Submitter: ggabrich(Gabricht, George)

import prompt
from collections import defaultdict
from goody import safe_open


def read_graph(file : open) -> {str:{str}}:
    graph_dict = defaultdict(set)
    for line in file:
        node, edge = tuple(line.rstrip().split(';'))
        graph_dict[node].add(edge)
    return graph_dict

def graph_as_str(graph : {str:{str}}) -> str:
    graph_str = ''
    for line in [f'  {node[0]} -> {node[1]}\n' for node in sorted([(node, sorted(graph[node])) for node in graph])]: 
        graph_str += line
    return graph_str
        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    if not graph.get(start, None): return None 
    explore, reached = [start], set()
    while len(explore) > 0:
        if trace: print(f'reached set    = {reached}', f'exploring list = {explore}', sep = '\n', end='\n')
        node = explore.pop()
        reached.add(node)
        if node in graph: explore.extend([edge for edge in graph[node] if edge not in reached])
        if trace: print(f'removing node from exploring list and adding it to reached list: node = {node}', f'after adding all nodes reachable directly from {node} but not already in reached, exploring = {explore}\n', sep='\n',end='\n')
    return reached

if __name__ == '__main__':
    # Write script here
    graph = read_graph(safe_open("Choose the file name representing the graph ", 'r', 'Invalid File Name', default='graph1.txt'))
    print('',"Graph: any node -> [all that node's destination nodes]", graph_as_str(graph), sep='\n')   
    while True:
        start = prompt.for_string("Choose the start node (or choose quit) ", default = 'quit', error_message = 'Entry Error')
        if start =='quit': 
            break
        elif start not in graph:
            print(f'Entry Error: {start}; Illegal: not a source node\nPlease enter a legal String\n')
            continue
        reached_nodes = set()
        for node in reachable(graph, start, prompt.for_bool("Choose whether to trace this algorithm ", default = True, error_message="Invalid Entry: Please enter a True or False")):
            if len(graph[node]) > 0 : reached_nodes.add(node)
        print(f'From {start} the reachable nodes are {reached_nodes}\n')
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
