n=int(input())
board=[1]*n

def is_valid_play(play):
    """
    Rule 1: We can set the first position to 0 or 1 whenever we want
    Rule 2: If first position is set to 1, we can set the second position to 0 or 1
    Rule 3: For position 3<=i<=18, we can set it to 0 or 1 if the position 0 to i-1 are set to 0 and i-i is set to 1
    """
    if play>=2:
        if board[play-1] and sum(board[:play-1])==0:
            return (True,None)
        else:
            if not board[play-1]:
                return (False,play-1)
            for i in range(play-2,-1,-1):
                if board[i]:
                    return (False,i)
    elif play==1:
        if board[0]:
            return (True,None)
        else:
            return (False,0)
    elif play==0:
        return (True,None)

def board_play(play):
    if board[play]:
        board[play]=0
    else:
        board[play]=1
if n==1:
    print(1)
    exit()
while True:
    if board[-1]:

        plays =is_valid_play(len(board)-1)
        last_play=len(board)-1
        while not plays[0]:
            last_play=plays[1]
            plays =is_valid_play(plays[1])
        print(last_play+1)
        board_play(last_play)
    else:
        board=board[:-1]
        if len(board)==1:
            print(1)
            break


