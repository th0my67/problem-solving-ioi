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


##################################################################
##################################################################
#
#To do list:
#   Create a way to link the reduced maps to the original map
#   Create a way to find the smallest density in the reduced maps
#      
#   Think about the tiling cause it may cut the biggest camp
#
##################################################################
##################################################################

















from collections import namedtuple

Problem = namedtuple('Problem', [])

class plan:
    
    def __init__(self, map_size,mosquitos_map):
        self.size = map_size #Tuple of (row,col)
        self.mosquitos_map = mosquitos_map #Tuple of tuples of 1 and 0 for the mosquitos or not
        self.reduced_map_list = [] #List of reduced maps, each level represent a reduction of 3x3 squares of data points
        self.auto_resize()

    
    def reduce_map(self,Big_Map):
        '''
        Reduce the map by taking 3x3 squares of data points and associating the dominant value for a new data point 

        '''
        reduced_map = []
        
        for row in range(0,self.size[0]-2,3):
            reduced_row = []
            for col in range(0,self.size[1]-2,3):
                reduced_row.append(self.get_dominant_value(Big_Map,row,col))
            reduced_map.append(tuple(reduced_row))
        self.reduced_map_list.append(tuple(reduced_map))
    
    def get_dominant_value(self,Big_Map,row,col):
        '''
        Get the dominant value of a 3x3 square of data points

        '''
        values = []
        for r in range(row,row+3):
            for c in range(col,col+3):
                values.append(Big_Map[r][c])
        return max(set(values), key = values.count)

    def auto_resize(self):
        '''
        Automatically create reduced maps until the size of the smalest reduced 
        map do not exceed 20x20

        '''
        if self.size[0]>20 and self.size[1]>20:
            self.reduce_map(self.mosquitos_map)
            while len(self.reduced_map_list[-1])>20 and len(self.reduced_map_list[-1][0])>20:
                self.reduce_map(self.reduced_map_list[-1])

    

    

def data_harvester():
    '''
    
    Harvests the data from the input and returns it in a well structured
    way.
    
    '''

    #Read the dimension input and then the plan, and store it in a tuple
    dimensions = tuple([int(x) for x in input().split()])
    mosquito_map = []
    for r in range(dimensions[0]):
        mosquito_map.append(tuple(map(int, input().split())))
    mosquito_map = tuple(mosquito_map)

    #Store all the data in an object and return the object
    return plan(dimensions, mosquito_map)


def make_density_map(plan,row,col):

    '''

    Returns a density map from a plan.

    '''

    density_map=[]

    #First row
    density_row=[(plan[0][0]+plan[0][1]+plan[1][0]+plan[1][1])/4]
    for c in range(1,col-1):
        density_row.append((plan[0][c-1]+plan[0][c]+plan[0][c+1]+plan[1][c-1]+plan[1][c]+plan[1][c+1])/6)
    density_row.append((plan[0][col-2]+plan[0][col-1]+plan[1][col-2]+plan[1][col-1])/4)
    density_map.append(tuple(density_row))

    #Middle rows
    for r in range(1,row-1):
        density_row=[(plan[r-1][0]+plan[r-1][1]+plan[r][0]+plan[r][1])/4]
        for c in range(1,col-1):
            density_row.append((plan[r-1][c-1]+plan[r-1][c]+plan[r-1][c+1]+plan[r][c-1]+plan[r][c]+plan[r][c+1]+plan[r+1][c-1]+plan[r+1][c]+plan[r+1][c+1])/9)
        density_row.append((plan[r-1][col-2]+plan[r-1][col-1]+plan[r][col-2]+plan[r][col-1])/4)
        density_map.append(tuple(density_row))

    #Last row
    density_row=[(plan[row-2][0]+plan[row-2][1]+plan[row-1][0]+plan[row-1][1])/4]
    for c in range(1,col-1):
        density_row.append((plan[row-2][c-1]+plan[row-2][c]+plan[row-2][c+1]+plan[row-1][c-1]+plan[row-1][c]+plan[row-1][c+1])/6)
    density_row.append((plan[row-2][col-2]+plan[row-2][col-1]+plan[row-1][col-2]+plan[row-1][col-1])/4)
    density_map.append(tuple(density_row))


    return tuple(density_map)

def get_smallest_density(density_map,row,col):

    '''
    Returns the position list of the smallest density in the density map.
    
    '''

    #Initializing the smallest density and the position list
    smallest_density=density_map[0][0]
    position=[(0,0)]

    #Density checking loop
    for r in range(row):
        for c in range(col):
            if density_map[r][c]<smallest_density:
                smallest_density=density_map[r][c]
                position=[(r,c)]
            elif density_map[r][c]==smallest_density:
                position.append((r,c))

    return position



def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''

    #Harvest, store and organize the data
    mos_map = data_harvester()
    





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