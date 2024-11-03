#A* Algorithm

from heapq import heappop, heappush
from math import sqrt

class Graph:
    def __init__(self, graph, coordinates):
        self.graph = graph #Adjacency list
        self.coordinates = coordinates #Dictionary of nodes coordinates

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def heuristic(self, node, goal):
        #Euclidian distance
        x1, y1 = self.coordinates[node]
        x2, y2 = self.coordinates[goal]
        return sqrt((x1 - x2)**2 + (y1 - y2)**2)

    def a_star(self, start, goal):
        #priority queueu to hold nodes to explore
        pq = [(0 + self.heuristic(start, goal), 0, start, [start])]
        visited = set()

        while pq:
            estimated_total, current_cost, current_node, path = heappop(pq)
            if current_node == goal:
                return path, current_cost

            if current_node in visited:
                continue

            for neighbor, weight in self.graph.get(current_node, {}).items():
                if neighbor not in visited: 
                    new_cost = current_cost + weight
                    estimated_total_cost = new_cost + self.heuristic(neighbor, goal)
                    heappush(pq, (estimated_total_cost, new_cost, neighbor, path + [neighbor]))

        return None, float("inf") #if goal unreachable

if __name__ == "__main__":
    # Graph adjacency list
    graph_data = {
        "A": {"B": 3, "C": 3},
        "B": {"A": 3, "D": 3.5, "E": 2.8},
        "C": {"A": 3, "E": 2.8, "F": 3.5},
        "D": {"B": 3.5, "E": 3.1, "G": 10},
        "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
        "F": {"G": 2.5, "C": 3.5},
        "G": {"F": 2.5, "E": 7, "D": 10},
    }
    
    # Coordinates for each node
    coordinates = {
        "A": (0, 0),
        "B": (1, 2),
        "C": (2, 0),
        "D": (3, 4),
        "E": (2, 3),
        "F": (4, 1),
        "G": (5, 5)
    }

    G = Graph(graph=graph_data, coordinates=coordinates)
    start_node = "A"
    goal_node = "G"
    path, cost = G.a_star(start_node, goal_node)
    if path:
        print(f"Shortest path from {start_node} to {goal_node}: {path} with total cost {cost}")
    else:
        print(f"No path found from {start_node} to {goal_node}")


