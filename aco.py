# aco.py

import numpy as np
import random

class AntColony:
    def __init__(self, distances, n_ants=10, n_best=3, n_iterations=100, decay=0.1, alpha=1, beta=2):
        self.distances = distances
        self.pheromone = np.ones(self.distances.shape) / len(distances)
        self.all_inds = range(len(distances))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", float('inf'))

        for _ in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheromone(all_paths, self.n_best)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path
            self.pheromone *=(1 - self.decay)
        
        return all_time_shortest_path

    def gen_path_dist(self, path):
        total_dist = 0
        for i in range(len(path) - 1):
            total_dist += self.distances[path[i]][path[i + 1]]
        total_dist += self.distances[path[-1]][path[0]]  # Geri dön
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        path.append(start)

        prev = start
        for _ in range(len(self.distances) - 1):
            move = self.pick_move(self.pheromone[prev], self.distances[prev], visited)
            path.append(move)
            visited.add(move)
            prev = move
        return path

    def spread_pheromone(self, all_paths, n_best):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in range(len(path) - 1):
                i = path[move]
                j = path[move + 1]
                self.pheromone[i][j] += 1.0 / dist
                self.pheromone[j][i] += 1.0 / dist
            self.pheromone[path[-1]][path[0]] += 1.0 / dist
            self.pheromone[path[0]][path[-1]] += 1.0 / dist

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        dist = np.copy(dist)
        dist[dist == 0] = np.inf  # 🔧 NaN oluşmasın diye

        row = pheromone ** self.alpha * ((1.0 / dist) ** self.beta)

        # NaN'lere karşı güvenlik
        if np.sum(row) == 0 or np.isnan(np.sum(row)):
            row = np.ones_like(row)
        norm_row = row / row.sum()

        return np.random.choice(self.all_inds, 1, p=norm_row)[0]

