def dfs(order, graph, v, visited):
    if visited[v]:
        return True
    visited[v] = True
    order.append(v)

    for i in graph[v]:
        return(dfs(order, graph, i, visited))
    return False 

def isDAG(graph, vertice):
    for v in range(1, vertice+1):
        visited = [False for i in range(int(vertice)+1)]
        order = []
        if dfs(order, graph, v, visited):
            return (-1)
    return (1)

def main():
    graphs = []
    vertices = []
    
    with open("data.txt") as f:
        count = int(f.readline().strip())

        for line in f:
            if line.strip():
                n1, n2 = map(int, line.strip().split())
                graph[n1].append(n2)
            else:
                vertice = list(map(int, f.readline().strip().split()))[0]
                graph = {i+1:[] for i in range(vertice)}
                graphs.append(graph)
                vertices.append(vertice)

    for n in range(len(graphs)):
        graph = graphs[n]
        vertice = vertices[n]
        print(isDAG(graph, vertice), end=" ")


if __name__ == "__main__":
    main()