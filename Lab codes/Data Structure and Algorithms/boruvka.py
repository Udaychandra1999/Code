def boruvka(graph, vertices):
    result = []  # To store the final MST

    # Keep track of the cheapest edge for each component
    cheapest = [(-1, (-1, -1))] * vertices

    # Keep track of the component to which each vertex belongs
    parent = [-1] * vertices

    # Number of components initially is the number of vertices
    num_components = vertices

    def find_parent(vertex):
        if parent[vertex] == -1:
            return vertex
        return find_parent(parent[vertex])

    def union_set(x, y):
        parent[x] = y

    while num_components > 1:
        # Initialize cheapest array for each component
        cheapest = [(-1, (-1, -1))] * vertices

        # Iterate through each edge in the graph
        for i in range(len(graph)):
            src, (dest, weight) = graph[i]

            # Find the components to which the source and destination vertices belong
            comp_src = find_parent(src)
            comp_dest = find_parent(dest)

            # If the components are different and the edge is cheaper, update cheapest
            if comp_src != comp_dest:
                if cheapest[comp_src][0] == -1 or cheapest[comp_src][1][1] > weight:
                    cheapest[comp_src] = (src, (dest, weight))
                if cheapest[comp_dest][0] == -1 or cheapest[comp_dest][1][1] > weight:
                    cheapest[comp_dest] = (src, (dest, weight))

        # Add the cheapest edges to the result
        for node in range(vertices):
            if cheapest[node][0] != -1:
                src, (dest, weight) = cheapest[node]

                comp_src = find_parent(src)
                comp_dest = find_parent(dest)

                if comp_src != comp_dest:
                    result.append((src + 1, (dest + 1, weight)))
                    union_set(comp_src, comp_dest)
                    num_components -= 1

    return result

# Example usage
vertices = int(input())
graph = []

for i in range(vertices):
    weights = list(map(int, input().split()))
    for j in range(vertices):
        if weights[j] != 0:
            graph.append((i, (j, weights[j])))

# Run Boruvka's algorithm
mst = boruvka(graph, vertices)

# Print the result
print("Edge:Weight")
for i in range(len(mst)):
    src, (dest, weight) = mst[i]
    if i == 0:
        print(f"{src}-{dest}:{weight}")
    else:
        print(f"{dest}-{src}:{weight}")