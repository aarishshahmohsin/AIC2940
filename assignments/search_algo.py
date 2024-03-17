from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, x, y, cost):
        if x not in self.graph:
            self.graph[x] = []
        if y not in self.graph:
            self.graph[y] = []
        self.graph[x].append((y, cost))
        self.graph[y].append((x, cost))


def uniform_cost_search(graph, start, goal):
    priority_queue = PriorityQueue()
    priority_queue.put((0, start, []))

    while not priority_queue.empty():
        cost, node, path = priority_queue.get()
        if node == goal:
            return path + [node]
        if len(graph[node]) > 0:
            for neighbor, neighbor_cost in graph[node]:
                new_cost = cost + neighbor_cost
                print((new_cost, neighbor, path + [(node, new_cost)]))
                priority_queue.put((
                    new_cost, neighbor, path + [(node, new_cost)]))



def best_first_search(graph, start, goal, heuristic):
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic[start], start, []))

    while not priority_queue.empty():
        _, node, path = priority_queue.get()

        if node == goal:
            return path + [node]

        for neighbor, _ in graph[node]:
            if neighbor not in [n for n, _ in path]:
                new_cost = heuristic[neighbor]
                print((new_cost, neighbor, path + [(node, new_cost)]))
                priority_queue.put((new_cost, neighbor, path + [(node, new_cost)]))


def a_start_search(graph, start, goal, heuristic):
    priority_queue = PriorityQueue()
    priority_queue.put((heuristic[start], 0, start, []))

    while not priority_queue.empty():
        _, cost, node, path = priority_queue.get()

        if node == goal:
            return path + [node]
        for neighbor, neighbor_cost in graph[node]:
            new_cost = cost + neighbor_cost
            print((
                heuristic[neighbor]+new_cost,
                new_cost, neighbor, path + [(node, new_cost+heuristic[node])]))
            priority_queue.put((
                heuristic[neighbor]+new_cost,
                new_cost, neighbor, path + [(node, new_cost+heuristic[node])]))


graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 5)
graph.add_edge('C', 'D', 5)


heuristic = {'A': 5, 'B': 4, 'C': 3, 'D': 2, 'E': 1}

source_node = input("Enter source node: ")
goal_node = input("Enter goal node: ")


print("uniform cost search\n")
ucs_path = uniform_cost_search(graph.graph, source_node, goal_node)
print(ucs_path)

print("best first search\n")
bfs_path = best_first_search(graph.graph, source_node, goal_node, heuristic)
print(bfs_path)

print("a star search\n")
astar_path = a_start_search(graph.graph, source_node, goal_node, heuristic)
print(astar_path)
