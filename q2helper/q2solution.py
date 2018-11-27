# Submitter: ggabrich(Gabricht, George)

import re
from goody import irange
from collections import defaultdict

# Before running the driver on the bsc.txt file, ensure you have put a regular
#   expression pattern in the files repattern1a.txt, repattern1b.txt, and
#   repattern2a.txt. The patterns must be all on the first line

def pages (page_spec : str, unique :  bool) -> [int]: #result in ascending order
    page_struct = (set() if unique else [])
    page_comp = re.compile(open('repattern2a.txt', 'r').read())
    for spec in page_spec.split(','):
        g1, g2, g3, g4 = page_comp.match(spec).groups()
        assert page_comp.match(spec), f'pages: in page specification {spec}, No Match Found!'
        if not g2:
            if unique: page_struct.add(int(g1))
            else: page_struct.append(int(g1))
        if g2 == '-': 
            assert (int(g1) <= int(g3)), f'pages: in page specification {spec}, {g1} > {g3}.'
            if unique: 
                if not g4: page_struct.update({pg for pg in irange(int(g1), int(g3))})
                else: page_struct.update({pg for pg in irange(int(g1), int(g3), int(g4))})
            else:
                if not g4: page_struct.extend([pg for pg in irange(int(g1), int(g3))])
                else: page_struct.extend([pg for pg in irange(int(g1), int(g3), int(g4))])
        elif g2 == ':':
            if unique: 
                if not g4: page_struct.update({pg for pg in range(int(g1), int(g1)+int(g3))})
                else: page_struct.update({pg for pg in range(int(g1), int(g1)+int(g3), int(g4))})
            else:
                if not g4: page_struct.extend([pg for pg in range(int(g1), int(g1)+int(g3))])
                else: page_struct.extend([pg for pg in range(int(g1), int(g1)+int(g3), int(g4))])
    return sorted(page_struct)

def expand_re(pat_dict:{str:str}):
        for rule in sorted(pat_dict, key=(lambda x: len(pat_dict[x]))):
            rule_comp = re.compile(f'#{rule}#')
            for rule2 in sorted(pat_dict, key=(lambda y: len(pat_dict[y]))): pat_dict[rule2] = rule_comp.sub(f'(?:{pat_dict[rule]})', pat_dict[rule2])

if __name__ == '__main__':
    
    p1a = open('repattern1a.txt').read().rstrip() # Read pattern on first line
    print('Testing the pattern p1a: ',p1a)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1a,text)
        print(' ','Matched' if m != None else "Not matched")
        
    p1b = open('repattern1b.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p1b: ',p1b)
    for text in open('bm1.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p1b,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
        
    p2 = open('repattern2a.txt').read().rstrip() # Read pattern on first line
    print('\nTesting the pattern p2: ',p2)
    for text in open('bm2a.txt'):
        text = text.rstrip()
        print('Matching against:',text)
        m = re.match(p2,text)
        print('  ','Matched with groups ='+ str(m.groups()) if m != None else 'Not matched' )
        
    print('\nTesting pages function')
    for text in open('bm2b.txt'):
        text = text.rstrip().split(';')
        text,unique = text[0], text[1]=='True'
        try:
            p = pages(text,unique)
            print('  ','pages('+text+','+str(unique)+') = ',p)
        except:
            print('  ','pages('+text+','+str(unique)+') = raised exception')
        
    
    print('\nTesting expand_re')
    pd = dict(digit = r'[0-9]', integer = r'[+-]?#digit##digit#*')
    print('  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary
    # {'digit': '[0-9]', 'integer': '[+-]?(?:[0-9])(?:[0-9])*'}
    
    pd = dict(integer       = r'[+-]?[0-9]+',
              integer_range = r'#integer#(..#integer#)?',
              integer_list  = r'#integer_range#(?,#integer_range#)*',
              integer_set   = r'{#integer_list#?}')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'integer': '[+-]?[0-9]+',
    #  'integer_range': '(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?',
    #  'integer_list': '(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*',
    #  'integer_set': '{(?:(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?)(?,(?:(?:[+-]?[0-9]+)(..(?:[+-]?[0-9]+))?))*)?}'
    # }
    
    pd = dict(a='correct',b='#a#',c='#b#',d='#c#',e='#d#',f='#e#',g='#f#')
    print('\n  Expanding ',pd)
    expand_re(pd)
    print('  result =',pd)
    # produces/prints the dictionary 
    # {'a': 'correct',
    #  'b': '(?:correct)',
    #  'c': '(?:(?:correct))',
    #  'd': '(?:(?:(?:correct)))',
    #  'e': '(?:(?:(?:(?:correct))))',
    #  'f': '(?:(?:(?:(?:(?:correct)))))',
    #  'g': '(?:(?:(?:(?:(?:(?:correct))))))'
    # }
    
    print()
    print()
    import driver
    driver.default_file_name = "bscq2F18.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()