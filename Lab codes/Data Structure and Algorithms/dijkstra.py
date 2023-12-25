import sys

def dijkstra(graph, start):
    n = len(graph)
    visited = [False] * n
    distance = [sys.maxsize] * n
    distance[start] = 0

    for _ in range(n):
        # Find the vertex with the minimum distance value
        min_dist = sys.maxsize
        min_index = -1
        for v in range(n):
            if not visited[v] and distance[v] < min_dist:
                min_dist = distance[v]
                min_index = v

        # Mark the selected vertex as visited
        visited[min_index] = True

        # Update the distance values of the adjacent vertices
        for v in range(n):
            if not visited[v] and graph[min_index][v] != 0 and distance[min_index] + graph[min_index][v] < distance[v]:
                distance[v] = distance[min_index] + graph[min_index][v]

    return distance

# Example usage
if __name__ == "__main__":
    # Read the number of vertices
    n = int(input())

    # Read the weight matrix
    graph = [list(map(int, input().split())) for _ in range(n)]

    # Start vertex (considering vertex 5 as the start vertex)
    start_vertex = 4  # (0-based indexing)

    # Find the single-source shortest path using Dijkstra's algorithm
    distances = dijkstra(graph, start_vertex)

    # Print the result
    print("Vertex: Distance from Start vertex {}".format(start_vertex + 1))
    for i in range(n):
        print("{}:{}".format(i + 1, distances[i] if distances[i] != sys.maxsize else "INF"))