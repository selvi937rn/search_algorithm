from graph import graph

def bfs(start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        node, path = queue.pop(0)
        if node == goal:
            return path
        if node not in visited:
            visited.add(node)
            for neighbor, _ in graph.get(node, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
    return None
