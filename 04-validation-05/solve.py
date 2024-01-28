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
if True:
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################


def harvester():
    n = int(input())
    manteaux = [input() for _ in range(n)]

    for i, manteau in enumerate(manteaux):
        manteaux[i] = [int(x) for x in manteau.split()]
        manteaux[i].append(i)
        manteaux[i] = tuple(manteaux[i])

    return manteaux

def get_best_manteaux(manteaux):
    
    any_sup = True
    while any_sup:
        any_sup = False
        i = 0
        while i < len(manteaux)-1:
            low = manteaux[i][0] - manteaux[i+1][0]
            high = manteaux[i][1] - manteaux[i+1][1]
            if low >= 0 and high >= 0:
                manteaux.pop(i+1)
                any_sup = True
                continue
            elif low <= 0 and high <= 0:
                manteaux.pop(i)
                any_sup = True
                continue
            i += 1
    return manteaux
                    
def get_level(meilleur_manteau, manteaux):
    manteaux.pop(meilleur_manteau[2])
    level = 0
    for manteau in manteaux:
        if meilleur_manteau[0] < manteau[0] and meilleur_manteau[1] > manteau[1]:
            level += 1
    return level



def main():
    manteaux = harvester()
    best_manteaux = get_best_manteaux(manteaux[:])

    manteaux_level = [0]*len(best_manteaux)
    for i , manteau in enumerate(best_manteaux):
        manteaux_level[i] = get_level(manteau, manteaux)
    return max(manteaux_level)
    







if __name__=='__main__':
    main()