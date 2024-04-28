graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G', 'H'],
    'F': [],
    'G': [],
    'H': []
}


def dfs(start, depth_limit, path=[]):
    path = path + [start]

    if len(path) > depth_limit + 1:
        return None

    if start == goal:
        return path

    for neighbor in graph[start]:
        result = dfs(neighbor, depth_limit, path)
        if result is not None:
            return result

    return None


def iterative_deepening_search(start, goal):
    for depth in range(len(graph)):
        path = dfs(start, depth, [])
        if path is not None:
            return path

    return None


start = 'A'
goal = 'G'

path = iterative_deepening_search(start, goal)
if path:
    print(path)
else:
    print("no path exists")
