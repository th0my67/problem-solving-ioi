
##############################################
##############################################

# This file contains the functions that you need to implement.

##############################################
##############################################




#Creating plan class and functions that act on it
#For harvesting the data, reducing the map, creating the density map
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
        Check if any one of the 9 data points is a mosquito and return 1 if so, 0 otherwise

        '''
        for r in range(row,row+3):
            for c in range(col,col+3):
                if Big_Map[r][c]:
                    return 1
        return 0

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
    Exemple :

    Input :

    8 5
    1 0 1 0 1 1 0 1
    1 0 1 0 1 1 0 1
    0 1 0 0 0 1 0 0
    1 0 0 1 0 0 1 1
    0 1 0 0 0 1 0 0

    Output :
    Plan:

    size = (8, 5)

    mosquitos_map = (
    (1, 0, 1, 0, 1, 1, 0, 1),
    (1, 0, 1, 0, 1, 1, 0, 1),
    (0, 1, 0, 0, 0, 1, 0, 0),
    (1, 0, 0, 1, 0, 0, 1, 1),
    (0, 1, 0, 0, 0, 1, 0, 0)
    )

    
    '''

    #Read the dimension input and then the plan, and store it in a tuple
    dimensions = tuple([int(x) for x in input().split()])
    mosquito_map = []
    for _ in range(dimensions[0]):
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


def get_zero_position(mos_map:tuple):
    
    '''
    test
    
    '''
    zero_pos=[]
    for r in range(len(mos_map)):
        zero_pos.append([])
        for c in range(len(mos_map[0])):
            if mos_map[r][c]==0:
                zero_pos[r].append(c)
    return tuple(zero_pos)



def find_square_and_get_angle_position(plan_map:tuple):
    '''
    test
    
    '''
    squarelist=[]
    max_size_square=0
    


def square_Finder_setVersion(zeros_positions:tuple,dimension:int):
    '''
    
    '''



    
    if dimension==2:
        for row in zeros_positions:
            setlist=[]
            setlist.append(square_Finder_setVersion(row,1))
        setlist=tuple(setlist)
        for row in setlist:
            for consecutivePos in row:
                size=len(consecutivePos)
                while i < size:
                    while max(row[i+1]) :


    elif dimension==1:
        i=0
        consecutive_positions_list=[]
        while i < len(zeros_positions):
            start_pos=zeros_positions[i]
            while i < len(zeros_positions) and zeros_positions[i]==zeros_positions[i+1]-1:
                i+=1
            end_pos=zeros_positions[i]
            consecutive_positions_list.append(set(range(start_pos,end_pos+1)))
        return tuple(consecutive_positions_list)

            

                









