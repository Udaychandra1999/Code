from queue import Queue, LifoQueue
from typing import List

def bfs(graph: List[List[int]], start: int, visited: List[bool]) -> None:
    q = Queue()
    q.put(start)
    visited[start] = True

    while not q.empty():
        vertex = q.get()
        print(vertex + 1, end="")

        # Collect unvisited adjacent vertices in ascending order
        unvisited_neighbors = sorted(i for i in range(len(graph)) if graph[vertex][i] == 1 and not visited[i])

        # Mark as visited while collecting
        for neighbor in unvisited_neighbors:
            visited[neighbor] = True
            q.put(neighbor)

        if not q.empty():
            print("->", end="")

    print(end="" if not q.empty() else "\n")

def dfs(graph: List[List[int]], start: int, visited: List[bool]) -> None:
    stack = LifoQueue()
    stack.put(start)
    visited[start] = True

    while not stack.empty():
        vertex = stack.get()
        print(vertex + 1, end="")

        # Collect unvisited adjacent vertices in ascending order
        unvisited_neighbors = sorted(i for i in range(len(graph)) if graph[vertex][i] == 1 and not visited[i])

        # Mark as visited while collecting
        for neighbor in unvisited_neighbors:
            visited[neighbor] = True
            stack.put(neighbor)

        if not stack.empty():
            print("->", end="")

    print(end="" if not stack.empty() else "\n")

if __name__ == "__main__":
    n = int(input())
    graph = [list(map(int, input().split())) for _ in range(n)]
    visited = [False] * n

    # Perform BFS traversal
    for i in range(n):
        if not visited[i]:
            bfs(graph, i, visited)

    # Reset visited array for DFS
    visited = [False] * n

    # Perform DFS traversal
    for i in range(n):
        if not visited[i]:
            dfs(graph, i, visited)