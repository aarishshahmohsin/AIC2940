graph = {
    'A': [('B', 7, 2), ('C', 6, 3)],
    'B': [('A', 7, 2), ('C', 5, 1), ('D', 6, 4)],
    'C': [('A', 6, 3), ('B', 5, 1), ('D', 3, 2), ('E', 0, 5)],
    'D': [('B', 6, 4), ('C', 3, 2), ('E', 3, 1)],
    'E': [('C', 0, 5), ('D', 3, 1)]
}


def ida_star(start, goal):
    def search(path, g, bound):
        node = path[-1]
        heuristic_cost = next(
            (cost for neighbor, cost, _ in graph[node] if neighbor == goal), None)

        f = g + (heuristic_cost if heuristic_cost is not None else float('inf'))

        if f > bound:
            return f

        if node == goal:
            return path

        min_cost = float('inf')

        for neighbor, heuristic_cost, path_cost in graph[node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                new_g = g + path_cost

                t = search(new_path, new_g, bound)
                if isinstance(t, list):
                    return t
                if t < min_cost:
                    min_cost = t

        return min_cost

    heuristic_cost = next(
        (cost for neighbor, cost, _ in graph[start] if neighbor == goal), None)
    bound = heuristic_cost if heuristic_cost is not None else float('inf')
    path = [start]

    while True:
        t = search(path, 0, bound)
        if isinstance(t, list):
            return t
        if t == float('inf'):
            return None
        bound = t


start = 'A'
goal = 'E'

path = ida_star(start, goal)

if path:
    print(path)
else:
    print("Path not found")
