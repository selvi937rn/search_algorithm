from graph import graph, heuristic

def hill_climbing(start, goal):
    current = start
    path = [current]

    while current != goal:
        neighbors = graph.get(current, [])
        if not neighbors:
            break
        # Pilih tetangga dengan heuristic terkecil
        next_node = min(neighbors, key=lambda x: heuristic[x[0]])
        if heuristic[next_node[0]] >= heuristic[current]:
            break
        current = next_node[0]
        path.append(current)
    return path if current == goal else None
