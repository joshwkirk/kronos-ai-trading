# optimizer.py
def optimize_strategy(data, strategy_name, param_grid):
    print("Optimizer running with strategy:", strategy_name)
    best_params = param_grid[0]
    best_score = 10000
    best_result = data.copy()
    best_result["equity"] = [10000 + i*5 for i in range(len(data))]
    return best_params, best_score, best_result
