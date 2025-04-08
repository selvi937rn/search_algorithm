from graph import graph

def dp_min_cost_path(start, goal, visited=None):
    if visited is None:
        visited = set()

    if start == goal:
        return (0, [start])
    
    visited.add(start)
    min_cost = float('inf')
    best_path = []

    for neighbor, weight in graph[start]:
        if neighbor not in visited:
            cost, path = dp_min_cost_path(neighbor, goal, visited.copy())
            total_cost = weight + cost
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = [start] + path

    return (min_cost, best_path)
