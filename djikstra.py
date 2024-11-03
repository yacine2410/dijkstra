#This assignment was completed using this tutorial: https://www.datacamp.com/tutorial/dijkstra-algorithm-in-python
#Dijkstra algorithm 
#Sample graph in the form of a dictionary
#Each point has a corresponding dictionary representing edges and weights

from heapq import heapify, heappop, heappush
class Graph:
    def __init__(self, graph: dict = {}):
        self.graph = graph # Dictionary for the adjacency list

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight #Add connection to node2

    def dijkstra(self, source: str):
        #initialize all node values with infinity:
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0 #distance to the source node is 0

        #initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        #create a set to hold visited nodes
        visited = set()

        while pq:
            current_distance, current_node = heappop(pq)
            if current_node in visited:
                continue #skip already visited nodes
            visited.add(current_node)

            for neighbor, weight in self.graph[current_node].items():
                #calculate the distance from the current_node to the neighbor
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))
            
        return distances


if __name__ == "__main__":

    graph = {
   "A": {"B": 3, "C": 3},
   "B": {"A": 3, "D": 3.5, "E": 2.8},
   "C": {"A": 3, "E": 2.8, "F": 3.5},
   "D": {"B": 3.5, "E": 3.1, "G": 10},
   "E": {"B": 2.8, "C": 2.8, "D": 3.1, "G": 7},
   "F": {"G": 2.5, "C": 3.5},
   "G": {"F": 2.5, "E": 7, "D": 10},
    }  
    
    G = Graph(graph = graph)
    distances = G.dijkstra("B")
    to_F = distances["F"]
    print(f"The shortest distance from B to F is {to_F}")
