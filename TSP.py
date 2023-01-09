from itertools import permutations
from sys import maxsize

V = 4


def travelingSalesmanProblem(in_graph, start):
    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != start:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize
    next_permutation = permutations(vertex)
    for i in next_permutation:

        # store current Path weight(cost)
        current_path_weight = 0

        # compute current path weight
        k = start
        for j in i:
            current_path_weight += in_graph[k][j]
            k = j
        current_path_weight += in_graph[k][start]

        # update minimum
        min_path = min(min_path, current_path_weight)

    return min_path


# Driver Code
if __name__ == "__main__":
    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travelingSalesmanProblem(graph, s))
