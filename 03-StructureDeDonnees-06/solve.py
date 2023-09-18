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
    return Problem()


def density_map(Force_map:tuple):
    """
    Make density map by adding each force on his density point like this:
    [2,5,1,2,4]
    ->
    [2+5+1, 5+1+2, 1+2+4]

    2 is added to position 0 (done manually because it's the first one)
    5 is added to position 1 and 2 (also done manually because it's the second one)
    1 is added to position 1 , 2 and 3 (done with a loop)
    symetrically, the last two are added to their position manually for the same reason
    
    """
    density_map = [0]*(len(Force_map)-2)
    density_map[0] = Force_map[0]
    density_map[0] += Force_map[1]
    density_map[1] += Force_map[1]
    for i in range(2,len(Force_map)-2):
        density_map[i-2] += Force_map[i]
        density_map[i-1] += Force_map[i]
        density_map[i] += Force_map[i]
    density_map[-1] += Force_map[-1]
    density_map[-1] += Force_map[-2]
    density_map[-2] += Force_map[-2]
    return tuple(density_map)
    
def get_best_density(density_map:tuple,deltaRange:int):
    """
    Get the best density in a density map
    """
    best_density = max(density_map)-deltaRange
    positions = []
    for density in density_map:
        if density >= best_density:
            positions.append(density)
    return tuple(positions)


def test_positions(force_map:tuple,positions:int,k:int):
    
    """
    Test positions to get the best one
    """
    is_even = k%2


    for i in range(positions-1,positions+2):
        for pos in range(k):
            pass





def solve(problem):
    K,N=map(int,input().split())
    Force_map=map(int,input().split())
    Force_map=tuple(Force_map)
    densityMap=density_map(Force_map)
    result_positions=get_best_density(densityMap,K/5)


    



    return result
        
    
    
def output(result):
    for r in result:
        print(r)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)