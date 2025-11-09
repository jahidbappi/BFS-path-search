## BFS Path Search

This project illustrates a breadth-first (uniform-cost) traversal that finds the minimum-cost route from node `A` to node `P` in a weighted directed graph. The implementation avoids function definitions to keep the logic inline and easy to follow.

### Contents

- `bfs.py` – builds the example graph, performs the uniform-cost search with `heapq`, prints the optimal path, and documents complexity analysis.
- `.gitignore` – excludes editor, system, and Python bytecode artifacts.

### Running the Script

```bash
python bfs.py
```

The script reports either the optimal path (with total cost) or indicates that no route exists.

### Algorithm Overview

- **Search strategy:** Uniform-cost search using a binary heap to explore paths in order of cumulative cost.
- **Output:** Path nodes joined with arrows plus the accumulated cost.
- **Complexity:** Time `O(E log V)`, Space `O(V)`, where `V` is the number of vertices and `E` the number of edges.

### Project Goal

Designed for the repository [jahidbappi/BFS-path-search](https://github.com/jahidbappi/BFS-path-search) as a reference implementation of cost-aware BFS traversal.

