'''

Template for France-IOI programming tasks with debugger in gitpod

The Python version on gitpod is 3.11, whereas the python version on france-ioi
is sadly stuck at 3.4.2 ... This means no type hints, no dataclasses, ... The
code should therefore remain pretty basic to run flawlessly on france-ioi

'''

##################################################################
# read input from file tests/test1.in as if type on the keyboard
# This shouldn't run on France-IOI
# replace this with the name of your test file
test_file = 'test1.in'

import sys, os, platform
# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ('3', '11'):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################



from collections import namedtuple

Problem = namedtuple('Problem', [])

    


def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''
    n=int(input())
    FactorialLliste=(479001600, 39916800, 3628800, 362880, 40320, 5040, 720, 120, 24, 6, 2, 1)
    Liste=[0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(12):
        Liste[i]=n//FactorialLliste[i]
        n-=Liste[i]*FactorialLliste[i]
    i=0
    while Liste[i]==0:
        i+=1
    cutListe=Liste[i:]
    cutListe.reverse()
    p=12-i
    result=""
    for i in cutListe:
        result+=str(i)+" "
    print(p)
    print(result)    


def solve(problem):



    
    return result
        
    
    
def output(result):
    for r in result:
        print(r)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)