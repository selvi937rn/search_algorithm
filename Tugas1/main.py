from bfs import bfs
from dfs import dfs
from hill_climbing import hill_climbing
from best_first_search import best_first_search
from branch_and_bound import branch_and_bound
from dynamic_programming import dp_min_cost_path
from graph import heuristic

if __name__ == "__main__":
    print("BFS:", bfs('S', 'Z'))
    print("DFS:", dfs('S', 'Z'))
    print("Hill Climbing:", hill_climbing('S', 'Z'))
    print("Best First Search:", best_first_search('S', 'Z', heuristic))
    print("Branch and Bound:", branch_and_bound('S', 'Z'))
    # print("Dynamic Programming:", dp_min_cost_path('S', 'Z'))
    print("Dynamic Programming:", dp_min_cost_path('S', 'Z')[1])
