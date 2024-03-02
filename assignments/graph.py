def dfs(graph, starting_node, vis, intermediate_steps):
    print(starting_node)
    vis[starting_node] = True
    for neigh in graph[starting_node]:
        intermediate_steps.append([starting_node, graph[starting_node]])
        if vis[neigh] == False:
            dfs(graph, neigh, vis, intermediate_steps)

def bfs(graph, start, intermediate_steps):
    vis = [False] * len(graph)
    q = [start]
    vis[start] = True

    while q:
        node = q.pop(0)
        print(node)
        intermediate_steps.append([node, graph[node]])
        for neigh in graph[node]:
            if vis[neigh] == False:
                q.append(neigh)
                vis[neigh] = True

n = int(input("enter the number of edges: "))

graph = {}

for i in range(n):
    graph[i] = []

for i in range(n-1):
    a, b = map(int, input("Enter the edge u{i}, v{i}: ").split())
    graph[a].append(b)
    graph[b].append(a)

print("\nDFS traversal: ")

vis = [False] * (n)

print(graph)
intermediate_steps = []
dfs(graph, 0, vis, intermediate_steps)

print("Intermediate steps: ")
for i in intermediate_steps:
    print(i)

print("\nBFS traversal: ")
intermediate_steps = []
bfs(graph, 0, intermediate_steps)

print("Intermediate steps: ")
for i in intermediate_steps:
    print(i)