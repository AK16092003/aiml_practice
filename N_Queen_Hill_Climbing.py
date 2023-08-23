
import random

"""

Hill Climbing

choose nearest state which is most optimal
nearest state differ by only 1 queen position

"""

N = 8
state = [1 for i in range(N)]

def random_initial_state():
    for i in range(N):
        state[i] = random.randint(0,N-1)


random_initial_state()
cur_state = state

print("initial state: ", cur_state)

def score(state):

    attack = 0

    for i in range(N):
        for j in range(i+1,N):
            if(state[i] == state[j] or i+state[i] == j+state[j] or i-state[i] == j-state[j]):
                attack += 1
    return attack

def neighbour_states(state):
    
    neighbour_list = []
    for i in range(N):
        for j in range(N):
            if(state[i] != j):
                new_state = list(state)
                new_state[i] = j
                neighbour_list.append(new_state)
                
    return neighbour_list

def printboard(cur_state):
    l = [[0 for i in range(N)] for j in range(N)]
    print()
    for i in range(N):
        l[i][cur_state[i]] = 1
        print(*l[i])
    print()
    
while True:
    
    cur_score = score(cur_state)
    next_state = -1
    
    for neighbour in neighbour_states(cur_state):
        if(cur_score >= score(neighbour)):
            cur_score = score(neighbour)
            next_state = list(neighbour)

    if next_state == -1:
        if(cur_score == 0):
            print("Solution found")
            print(cur_state)
            printboard(cur_state)
        else:
            print("Local minima attained with score = ", cur_score)
        break
    
    cur_state = list(next_state)
    print(cur_state)
    
