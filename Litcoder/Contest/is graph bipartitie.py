from collections import deque
def is_bipartite(graph):
    n = len(graph)
    colors = [-1] * n

    def bfs(start):
        queue = deque([start])
        colors[start] = 0

        while queue:
            current = queue.popleft()

            for neighbor in graph[current]:
                if colors[neighbor] == -1:
                    colors[neighbor] = 1 - colors[current]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[current]:
                    return "false"

        return "true"

    for i in range(n):
        if colors[i] == -1 and not bfs(i):
            return "false"

    return "true"

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    neighbors = list(map(int, input().split()))
    graph[i].extend(neighbors)

# Call the function with user input
result = is_bipartite(graph)
print(result)
                                                                                                                            