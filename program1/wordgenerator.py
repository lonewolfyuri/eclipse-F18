# Submitter: ggabrich(Gabricht, George)

from goody import irange, safe_open
import prompt
from random import choice
from collections import defaultdict

# For use in read_corpus: leave unchanged in this file
def word_at_a_time(file : open):
    for line in file:
        for item in line.strip().split():
                yield item


def read_corpus(os : int, file : open) -> {(str):[str]}:
    corpus, corp_list, reader = defaultdict(list), [], word_at_a_time(file)
    for _ in range(os): corp_list.append(next(reader))
    try:    
        while True:
            word = next(reader)
            if word not in corpus[tuple(corp_list)]: corpus[tuple(corp_list)].append(word)
            corp_list.pop(0)
            corp_list.append(word)
    except StopIteration: return dict(corpus)

def corpus_as_str(corpus : {(str):[str]}) -> str:
    corpus_str, sorted_corpus, _max, _min = '', [(entry, corpus[entry]) for entry in sorted(corpus)], 0, 999999999
    for key, val in sorted_corpus:
        if len(val) > _max: _max = len(val)
        if len(val) < _min: _min = len(val)
        corpus_str += f'  {key} can be followed by any of {val}\n'
    return corpus_str + f'max/min list lengths = {_max}/{_min}\n'

def produce_text(corpus : {(str):[str]}, start : [str], count : int) -> [str]:
    text, new_word = start.copy(), ''
    for _ in range(count):    
        new_word = None if tuple(text[-len(start):]) not in corpus else choice(corpus[tuple(text[-len(start):])])
        text.append(new_word)
        if not new_word: return text
    return text
        
if __name__ == '__main__':
    # Write script here
    os, start = prompt.for_int('Choose the order statistic ', default=2, is_legal= (lambda x: x >= 0), error_message='Not a Valid Order Statistic!'), []
    corpus = read_corpus(os, safe_open('Choose the file name to process ', 'r', 'Not a Valid Filename! Try Again!', default='wginput1.txt'))
    print('Corpus', corpus_as_str(corpus), f'Choose {os} words to start with', sep='\n')
    for i in irange(1, os): start.append(prompt.for_string(f'Choose word {i}', error_message='Invalid Word: Please Enter a Valid word in the Text'))
    print(f"Random text = {produce_text(corpus, start, prompt.for_int('Choose # of words for generation ', default=10, is_legal= (lambda x: x >= 0), error_message= 'Not a Valid Number of Words!'))}")
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc5.txt"
    driver.default_show_traceback = True
    driver.default_show_exception = True
    driver.default_show_exception_message = True
    driver.driver()
