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
    P=int(input())
    N_P=list(map(int, input().split()))
    N_P.sort()
    N_P=tuple(N_P)
    S=int(input())
    N_S=list(map(int, input().split()))
    N_S.sort()
    N_S=tuple(N_S)


    N_AND=0
    
    if P<S:
        pos_S=0
        for p in N_P:
            while pos_S<S and N_S[pos_S]<=p:
                if N_S[pos_S]==p:
                    N_AND+=1
                pos_S+=1
    else:
        pos_P=0
        for s in N_S:
            while pos_P<P and N_P[pos_P]<=s:
                if N_P[pos_P]==s:
                    N_AND+=1
                pos_P+=1






    return N_AND

def solve(problem):
    return problem
        
    
    
def output(result):
    print(result)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)