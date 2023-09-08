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
test_file = 'test2.in'

import sys, os, platform
# only if executed on Python 3.11 (gitpod), will be false on france-ioi
if platform.python_version_tuple()[:2] == ('3', '11'):
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################



from collections import namedtuple

Problem = namedtuple('Problem', [])

    
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

    #Returning the smallest density and the position list
    return position


def position_testing(position,size, plan):
    '''
    Tests if a position is valid for a given size and a given plan with little DeltaX and DeltaY that watch around the position.

    Returns True if the position is valid, False otherwise.

    '''

    Delta_P=size//2
    if size%2:
        parity_compensation=0
    else:
        parity_compensation=-1

    is_valid=True

    #Chosing little DeltaX
    for DeltaX in range(-1-parity_compensation,2,1):

        #Testing if the x-position is out of bounds
        if position[1]+DeltaX-Delta_P>=0 and position[1]+DeltaX+Delta_P+parity_compensation<len(plan[0]):

            #Chosing little DeltaY
            for DeltaY in range(-1-parity_compensation,2,1):

                #Testing if the y-position is out of bounds
                if  position[0]+DeltaY-Delta_P>=0 and position[0]+DeltaY+Delta_P+parity_compensation<len(plan):

                    #Testing the position
                    temp_plan=plan[position[0]+DeltaY-Delta_P:position[0]+DeltaY+Delta_P+1+parity_compensation]

                    for row in temp_plan:

                        #Testing if the row is valid, if not, it breaks the loop, if yes, it continues
                        temp_row=row[position[1]+DeltaX-Delta_P:position[1]+DeltaX+Delta_P+1+parity_compensation]

                        if sum(temp_row)!=0:
                            is_valid=False
                            break
                    
                    #Returning True if the position is valid
                    if is_valid:
                        return True
                    is_valid=True
            
    #After all the testing, if none of the position is valid, it returns False            
    return False

def quick_ranking(position_list,plan):
    ''' 
    Retrun a list of positions sorted by the max space around them.
    
    '''

    #Initializing score of position list
    position_score=[]
    #Initializing the size of the plan
    row=len(plan)
    col=len(plan[0])

    #Ranking loop
    for position in position_list:


        #Initializing the radius
        radius=1
        while True:
            
            #Rigth side check
            if position[1]+radius>=col:
                break
            if plan[position[0]][position[1]+radius]:
                break
            #Up side check
            if position[0]-radius<0:
                break
            if plan[position[0]-radius][position[1]]:
                break
            #Left side check
            if position[1]-radius<0:
                break
            if plan[position[0]][position[1]-radius]:
                break
            #Down side check
            if position[0]+radius>=row:
                break
            if plan[position[0]+radius][position[1]]:
                break
            radius+=1
        position_score.append(radius*2)
    
    #Sorting the position list by the score
    position_list = sorted(zip(position_score, position_list), reverse=True)

    #Returning the sorted position list
    return position_list






def parse_input():
    '''
    
    Parses the input data and returns a dictionary with everything
    well structured.
    
    '''
    #Harvesting data
    row, col= [int(x) for x in input().split(' ')]
    plan = []
    max_size_square = min(row,col)

    #Making the plan from the console input by adding each row to the plan
    for r in range(row):
        plan.append([int(x) for x in input().split(' ')])

    #Making density map from the plan
    density_map = make_density_map(plan,row,col)

    #Getting the smallest density and the position list
    position = get_smallest_density(density_map,row,col)
    
    #Ranking the position list by the max space around them
    position = quick_ranking(position,plan)

    #Position testing loop
    max_size_found=0
    courrent_size=0
    for pos in position:
        if pos[0]<=max_size_found:
            break
        courrent_size=pos[0]
        while courrent_size>=max_size_found and not position_testing(pos[1],courrent_size,plan):
            courrent_size-=1
        max_size_found=courrent_size
    return max_size_found


    """for size in range(max_size_square,0,-1):
        for pos in position:
            if position_testing(pos,size,plan):
                return size
                exit()"""



#Way of imporvement : selection the best position in the position list by testing in order by the max_sized_square possible by lokking on each direction of the positon.


def solve(problem):
    return problem
        
    
    
def output(result):
        print(result)
    
            


if __name__ == '__main__':
    problem = parse_input()
    result = solve(problem)
    output(result)