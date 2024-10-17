# Minimax Algorithm with Alpha-Beta Pruning

This project demonstrates the **Minimax algorithm** with **Alpha-Beta Pruning** in Python. The algorithm efficiently explores the game tree by pruning branches that will not affect the final decision, optimizing the search process.

---

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [How Alpha-Beta Pruning Works](#how-alpha-beta-pruning-works)
- [Code Structure](#code-structure)
- [Example Output](#example-output)


---

## Introduction

The **Minimax algorithm** is used in decision-making and game theory to minimize the possible loss for a worst-case scenario. This version of the Minimax algorithm includes **Alpha-Beta Pruning**, which reduces the number of nodes that are evaluated in the search tree, improving performance.

---

## Features
- Implementation of Minimax with Alpha-Beta Pruning in Python.
- Debugging print statements to understand the decision-making process.
- Handles both maximizer and minimizer players.
- Supports variable-depth trees and customizable leaf-node values.

---

## How Alpha-Beta Pruning Works

- **Alpha**: The best value the maximizer can guarantee so far.
- **Beta**: The best value the minimizer can guarantee so far.
- **Pruning**: If `alpha >= beta`, further exploration of the current branch is stopped.

This avoids unnecessary computations and speeds up decision-making.

---

## Code Structure

- **`minimax()`**: The main function implementing the Minimax algorithm with Alpha-Beta Pruning.
- **Parameters:**
  - `depth`: Current depth of the tree.
  - `nodeIndex`: Index of the current node.
  - `isMaximizingPlayer`: Boolean indicating the player's turn (True for Maximizer, False for Minimizer).
  - `values`: List of leaf node values.
  - `alpha` & `beta`: Alpha and Beta values for pruning.
  - `maxDepth`: Maximum depth of the game tree.

---

## Example Output
- Maximizer at depth 0, alpha: -inf, beta: inf
- Maximizer at depth 1, alpha: -inf, beta: inf
- Leaf node reached at depth 3, returning value: -1
- Maximizer at depth 2, comparing value: -1 with best: -inf
- ...
- The optimal value is: 4
