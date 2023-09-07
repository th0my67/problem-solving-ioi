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

    
def make_density_map(plan,row,col):
    density_map=[]

    #First row
    density_row=[(plan[0][0]+plan[0][1]+plan[1][0]+plan[1][1])/4]
    for c in range(1,col-1):
        density_row.append((plan[0][c-1]+plan[0][c]+plan[0][c+1]+plan[1][c-1]+plan[1][c]+plan[1][c+1])/6)
    density_row.append((plan[0][col-2]+plan[0][col-1]+plan[1][col-2]+plan[1][col-1])/4)
    density_map.append(density_row)

    #Middle rows
    for r in range(1,row-1):
        density_row=[(plan[r-1][0]+plan[r-1][1]+plan[r][0]+plan[r][1])/4]
        for c in range(1,col-1):
            density_row.append((plan[r-1][c-1]+plan[r-1][c]+plan[r-1][c+1]+plan[r][c-1]+plan[r][c]+plan[r][c+1]+plan[r+1][c-1]+plan[r+1][c]+plan[r+1][c+1])/9)
        density_row.append((plan[r-1][col-2]+plan[r-1][col-1]+plan[r][col-2]+plan[r][col-1])/4)
        density_map.append(density_row)

    #Last row
    density_row=[(plan[row-2][0]+plan[row-2][1]+plan[row-1][0]+plan[row-1][1])/4]
    for c in range(1,col-1):
        density_row.append((plan[row-2][c-1]+plan[row-2][c]+plan[row-2][c+1]+plan[row-1][c-1]+plan[row-1][c]+plan[row-1][c+1])/6)
    density_row.append((plan[row-2][col-2]+plan[row-2][col-1]+plan[row-1][col-2]+plan[row-1][col-1])/4)
    density_map.append(density_row)

    #Returning the density map
    return density_map


def get_smallest_density(density_map,row,col):
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

    #Returning the smallest density and the position list
    return position


def position_testing(position,size, plan):
    Delta_P=size//2
    is_valid=True

    out_of_boundsX=False
    out_of_boundsY=False
    #Chosing little DeltaX and DeltaY
    for DeltaX in range(-1,1,1+(size+1)%2):
        for DeltaY in range(-1,1,1+(size+1)%2):

            #Testing if the position is out of bounds
            if position[0]+DeltaX-Delta_P<0 or position[0]+DeltaX+Delta_P>=len(plan[0]):
                out_of_boundsX=True
            if position[1]+DeltaY-Delta_P<0 or position[1]+DeltaY+Delta_P>=len(plan):
                out_of_boundsY=True
            if out_of_boundsX or out_of_boundsY:
                break



            #Testing the position
            for row in plan[position[1]+DeltaY-Delta_P:position[1]+DeltaY+Delta_P+1]:
                if sum(row[position[0]+DeltaX-Delta_P:position[0]+DeltaX+Delta_P+1])!=0:
                    is_valid=False
                    break
            if is_valid:
                return True
            is_valid=True
    return False





def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''
    #Harvesting data
    row, col= map(int, input().split(' '))
    plan = []
    max_size_square = min(row,col)


    for r in range(row):
        plan.append(input().split(' '))

    #Making density map from the plan
    density_map = make_density_map(plan,row,col)

    #Getting the smallest density and the position list
    position = get_smallest_density(density_map,row,col)
    
    #Position testing loop

    for size in range(max_size_square,0,-1):
        for pos in position:
            continue

    



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