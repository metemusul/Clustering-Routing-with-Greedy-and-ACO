# ACO veya rota hesaplamaları 

# basit greedy yaklasımı 

import numpy as np 

def distance(a,b):
    return np.linalg.norm(a-b)

def greedy_tsp(points):
    n = len(points)
    visited = [False]*n
    route = [0]
    visited[0] = True
    for _ in range(1,n):
        last = route[-1]
        next_index = np.argmin([
            distance(points[last],points[i]) if not visited[i] else float('inf')
            for i in range(n)
        ])
        route.append(next_index)
        visited[next_index] = True

    route.append(0)
    return route   





