from graph import graph

def branch_and_bound(start, goal):
    queue = [(0, start, [start])]

    while queue:
        # Ambil node dengan cost terkecil
        queue.sort()
        cost, node, path = queue.pop(0)

        if node == goal:
            return path
        for neighbor, weight in graph.get(node, []):
            if neighbor not in path:
                queue.append((cost + weight, neighbor, path + [neighbor]))
    return None
