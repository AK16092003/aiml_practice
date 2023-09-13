

def neighbour(cur_state ,player):
    char = 'X'
    if(player == 1):
        char = 'O'

    nghb = []
    
    for i in range(3):
        for j in range(3):
            if cur_state[i][j] == ' ':
                next_state = [[x for x in y] for y in cur_state]
                next_state[i][j] = char
                nghb.append(next_state)
    return nghb 


def win(cur_state , char):

    for i in range(3):
        cnt = 0
        for j in range(3):
            if cur_state[i][j] == char:
                cnt+=1
        if cnt == 3:
            return True

        
    for j in range(3):
        cnt = 0
        for i in range(3):
            if cur_state[i][j] == char:
                cnt+=1
        if cnt == 3:
            return True


    if cur_state[0][0] == cur_state[1][1] == cur_state[2][2] == char :
        return True

    if cur_state[0][2] == cur_state[1][1] == cur_state[2][0] == char :
        return True


    return False



def full(cur_state):
    for i in range(3):
        for j in range(3):
            if cur_state[i][j] == ' ':
                return False
    return True


def terminal_test(cur_state):

    if win(cur_state , 'X'):
        return True
    if win(cur_state , 'O'):
        return True
    if full(cur_state):
        return True
    return False


def utility_fn(cur_state):
    
    if win(cur_state , 'X'):
        return 1
    if win(cur_state , 'O'):
        return -1
    return 0

def tostr(cur_state):
    s = ''
    for i in range(3):
        for j in range(3):
            s += cur_state[i][j]
        s += '\n'
    return s



memo = {}

def play(cur_state , player):

    ans = 0

    if tostr(cur_state) in memo:
        return memo[tostr(cur_state)]
    
    if terminal_test(cur_state):
        ans =  utility_fn(cur_state)
    else:
        if player == 0:
            ans = -10**10
            for next_state in neighbour(cur_state , player):
                ans = max(ans , play(next_state , player^1))                  
        if player == 1:
            ans = 10**10
            for next_state in neighbour(cur_state , player):
                ans = min(ans , play(next_state , player^1))
    memo[tostr(cur_state)] = ans
    return ans


initial_state = [[' ' , ' ' , ' '],[' ' , ' ' , ' '],[' ' , ' ' , ' ']]
play(initial_state , 0)

print("Calculated MINIMAX .... ")
for k in memo:
    print(k + "f(n) = " , memo[k] , '\n')
    





