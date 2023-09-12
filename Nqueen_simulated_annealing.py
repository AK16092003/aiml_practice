import random
import math
import time

"""

Simulated Annealing

as temp more, more randomness
less temp less randomness

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
    
visited = {}

# initial parameters

temp = 100
k = 0.1
start_time = time.time()

def cooling_function(temp , time):
    delta_time = time - start_time
    new_temp = temp*(math.e**(-k*delta_time))
    return new_temp

while True:

    cur_score = score(cur_state)
    next_state = -1
    for neighbour in neighbour_states(cur_state):
        delta_e = -(score(neighbour) - score(cur_state))
        if(tuple(neighbour) not in visited):
            if(delta_e >= 0 and random.random() < (1/(1 + math.e**(-delta_e/temp)))):
                cur_score = score(neighbour)
                next_state = list(neighbour)
                visited[tuple(neighbour)] = True
                break
        
    if next_state == -1:
        if(cur_score == 0):
            print("Solution found")
            print(cur_state)
            printboard(cur_state)
        else:
            print("Local minima attained with score = ", cur_score)
        break
        
    cur_state = list(next_state)
    print(cur_state ," score : ",score(cur_state) , "time :" , round(time.time()-start_time,2) , "Temperature : " , round(temp , 2))
    temp = cooling_function(temp , time.time())
    
print("Total time taken : " , time.time() - start_time)
    
