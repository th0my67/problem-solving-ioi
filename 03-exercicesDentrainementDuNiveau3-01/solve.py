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

    Na= int(input())
    ValueNa =  tuple(map(int,input().split()))
    Nb= int(input())
    ValueNb =  tuple(map(int,input().split()))


    Pa=0
    Pb=0
    sortedValue = []

    while Pa < Na and Pb < Nb:
        if ValueNa[Pa] < ValueNb[Pb]:
            sortedValue.append(ValueNa[Pa])
            Pa+=1
        else:
            sortedValue.append(ValueNb[Pb])
            Pb+=1
    if Pa < Na:
        sortedValue.extend(ValueNa[Pa:])
    if Pb < Nb:
        sortedValue.extend(ValueNb[Pb:])
    return sortedValue

def solve(problem):
    return problem
        
    
    
def output(result):
    print(*result)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)