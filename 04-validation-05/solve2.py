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
if True:
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join('tests', test_file), "r")
##################################################################


def harvester():
    n = int(input())
    manteaux = [input() for _ in range(n)]

    for i, manteau in enumerate(manteaux):
        manteaux[i] = [tuple([int(x) for x in manteau.split()]),i,set()]
        

    return manteaux


def compare_manteaux(manteaux:list):
    i = 0
    has_break = False
    while i < len(manteaux):
        j = i+1
        while j < len(manteaux):
            low = manteaux[i][0][0] - manteaux[j][0][0]
            high = manteaux[i][0][1] - manteaux[j][0][1]
            if low <= 0 and high >= 0:
                manteaux[i][2].add(manteaux[j][1])
                manteaux[i][2] = manteaux[i][2].union(manteaux[j][2])
                manteaux.pop(j)
                continue
            elif low >= 0 and high <= 0:
                manteaux[j][2].add(manteaux[i][1])
                manteaux[j][2] = manteaux[j][2].union(manteaux[i][2])
                manteaux.pop(i)
                has_break = True
                break
            j += 1
        if has_break:
            has_break = False
            continue
        i += 1

def get_best_level(manteaux):
    best_level = 0
    for manteau in manteaux: 
        level = len(manteau[2])
        if level > best_level:
            best_level = level
    return best_level

    

def main():
    manteaux = harvester()
    compare_manteaux(manteaux)
    print(get_best_level(manteaux))




if __name__=='__main__':
    main()