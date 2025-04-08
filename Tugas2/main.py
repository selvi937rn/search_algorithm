from bfs import bfs
from dfs import dfs
from hill_climbing import hill_climbing
from best_first_search import best_first_search
from branch_and_bound import branch_and_bound
from dynamic_programming import dp_min_cost_path
from graph import heuristic

if __name__ == "__main__":
    print("BFS:", bfs('A', 'Z'))
    print("DFS:", dfs('A', 'Z'))
    print("Hill Climbing:", hill_climbing('A', 'Z'))
    print("Best First Search:", best_first_search('A', 'Z', heuristic))
    print("Branch and Bound:", branch_and_bound('A', 'Z'))
    print("Dynamic Programming:", dp_min_cost_path('A', 'Z'))
