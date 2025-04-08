from graph import graph

def best_first_search(start, goal, heuristic):
    queue = [(heuristic[start], start, [start])]
    visited = set()

    while queue:
        # Ambil node dengan heuristic terkecil
        queue.sort()
        _, node, path = queue.pop(0)

        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((heuristic[neighbor], neighbor, path + [neighbor]))
    return None
