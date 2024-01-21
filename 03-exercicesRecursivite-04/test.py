import random


def remove_all(Liste,element):
    last_exchange_pos=-1
    number_of_exchange=0
    i=0
    while i<len(Liste)-number_of_exchange:
        if Liste[i]==element:
            Liste[i]=Liste[last_exchange_pos]
            Liste[last_exchange_pos]=element
            last_exchange_pos-=1
            number_of_exchange+=1
        i+=1
    return Liste[:len(Liste)-number_of_exchange]


def mastermind_ill_positioned(choice, solution):
    
    for i in range(len(choice)):
        if choice[i]==solution[i]:
            choice[i]=None
            solution[i]=None


    while None in choice:
        choice.remove(None)
    choice.sort()
    while None in solution:
        solution.remove(None)
    solution.sort()

    i,j=0,0
    common=0
    while i<len(choice) and j<len(solution):
        if choice[i]==solution[j]:
            common+=1
            i+=1
            j+=1
        elif choice[i]<solution[j]:
            i+=1
        else:
            j+=1


    return common

print(mastermind_ill_positioned([1,2,3,4], [1,2,3,4]))
print(mastermind_ill_positioned([1,2,3,4], [1,2,5,3]))
print(mastermind_ill_positioned([1,2,3,4], [5,1,2,3]))
print(mastermind_ill_positioned([1,2,3,4], [5,6,7,8]))

