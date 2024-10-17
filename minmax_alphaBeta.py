import math

def minimax(depth, nodeIndex, isMaximizingPlayer, values, alpha, beta, maxDepth):
    # Terminal node (leaf nodes)
    if depth == maxDepth:
        print(f"Leaf node reached at depth {depth}, returning value: {values[nodeIndex]}")
        return values[nodeIndex]

    if isMaximizingPlayer:
        best = -math.inf
        print(f"Maximizer at depth {depth}, alpha: {alpha}, beta: {beta}")

        # Maximizer's choice (MAX player)
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta, maxDepth)
            print(f"Maximizer at depth {depth}, comparing value: {value} with best: {best}")
            best = max(best, value)
            alpha = max(alpha, best)
            print(f"Maximizer updated alpha: {alpha}")

            # Prune the branch if beta <= alpha
            if beta <= alpha:
                print(f"Pruning at depth {depth} with alpha: {alpha} >= beta: {beta}")
                break
        print(f"Maximizer at depth {depth}, selected best: {best}")
        return best

    else:
        best = math.inf
        print(f"Minimizer at depth {depth}, alpha: {alpha}, beta: {beta}")

        # Minimizer's choice (MIN player)
        for i in range(2):
            value = minimax(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta, maxDepth)
            print(f"Minimizer at depth {depth}, comparing value: {value} with best: {best}")
            best = min(best, value)
            beta = min(beta, best)
            print(f"Minimizer updated beta: {beta}")

            # Prune the branch if beta <= alpha
            if beta <= alpha:
                print(f"Pruning at depth {depth} with beta: {beta} <= alpha: {alpha}")
                break
        print(f"Minimizer at depth {depth}, selected best: {best}")
        return best

# Define the depth of the game
maxDepth = 3
# Define the leaf-node values
values = [-1, 4, 2, 6, -3, -5, 0, 7]

# Initialize alpha and beta values
alpha = -math.inf
beta = math.inf

# Call the minimax function
optimalValue = minimax(0, 0, True, values, alpha, beta, maxDepth)

print("\nThe optimal value is:", optimalValue)
