
inf = 10**10
visited = []

def dfs_search(u , l , cost):
    next_node = -1
    next_weight = inf
    
    for v in range(n):
        if visited[v] == 0 and grid[u][v] > 0:
            if(next_weight > grid[u][v]):
                next_weight = grid[u][v]
                next_node = v

    if(next_node != -1):
        v = next_node
        visited[v] = 1
        dfs_search(v , l + [v,] , cost + grid[u][v])
        visited[v] = 0

    else:
        if visited.count(0) == 0 and grid[0][l[0]] > 0:
            l += [l[0],]
            cost += grid[u][l[0]]
            print(l ," cost : ", cost)
            exit(0)

n = int(input("Enter N : (number of nodes) "))
grid = [[-1 for i in range(n)] for j in range(n)]
visited = [0 for i  in range(n)]
print("Enter adjmatrix with weights : (-1 for no edge): ")
for i in range(n):
    grid[i] = list(map(int , input().split()))
for u in range(n):
    visited[u] = 1
    dfs_search(u , [u] , 0)
    visited[u] = 0

print("Failed , no TSP path can be found")
