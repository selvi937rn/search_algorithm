from graph import graph

def dp_min_cost_path(start, goal):
    memo = {}

    def dp(node):
        if node == goal:
            return (0, [goal])
        if node in memo:
            return memo[node]
        min_cost = float('inf')
        best_path = []
        for neighbor, weight in graph.get(node, []):
            cost, path = dp(neighbor)
            if cost + weight < min_cost:
                min_cost = cost + weight
                best_path = [node] + path
        memo[node] = (min_cost, best_path)
        return memo[node]

    cost, path = dp(start)
    return path if path[-1] == goal else None
