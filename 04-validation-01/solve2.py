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
test_file = 'test3.in'

import sys, os, platform
# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ('3', '11'):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################


##################################################################
##################################################################
#
#To do list:
#   Create a way to link the reduced maps to the original map
#   Create a way to find the smallest density in the reduced maps
#      
#   Think about the tiling cause it may cut the biggest camp
#   
#   Find the biggest square in the reduced map and then check on the original map the edges but only the edges and not the center that has already been checked
#
#
##################################################################
##################################################################



from collections import namedtuple
from solve2Library import *


Problem = namedtuple('Problem', [])

    



def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''

    #Harvest, store and organize the data
    mos_map = data_harvester()
    zero_positions = get_zero_position(mos_map.reduced_map_list[-1])
    find_square_and_get_angle_position(zero_positions)





    return Problem()

def solve(problem):
    result = []
    
    return result
        
    
    
def output(result):
    for r in result:
        print(r)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)