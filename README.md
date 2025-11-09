## BFS Path Search

This project illustrates a breadth-first (uniform-cost) traversal that finds the minimum-cost route from node `A` to node `P` in a weighted directed graph. The implementation keeps all logic inline (no function definitions) to match the original task constraints.

### Repository Summary

- Language: Python 3
- Primary script: `bfs.py`
- License: MIT (see [`LICENSE`](LICENSE))

### Problem Statement

> Given the graph below with edge costs, find the minimum-cost path from `A` to `P`.

```
A: B (3), C (2)
B: D (4), E (6)
C: F (5), G (1)
D: H (2)
E: —
F: —
G: P (3)
H: —
P: —
```

### Getting Started

#### Prerequisites

- Python 3.8 or later

#### Installation

```bash
git clone https://github.com/jahidbappi/BFS-path-search.git
cd BFS-path-search
```

### Contents

- `bfs.py` – builds the example graph, executes the uniform-cost search using `heapq`, prints the optimal path, and notes complexity results.
- `.gitignore` – excludes editor, system, and Python bytecode artifacts.
- `LICENSE` – project licensing terms.

### Running the Script

```bash
python bfs.py
```

Example output:

```
Optimal path: A -> C -> G -> P | Cost: 6
```

### Algorithm Overview

- **Search strategy:** Uniform-cost search (priority-queue-based BFS) that expands paths in ascending order of accumulated edge cost.
- **Time complexity:** `O(E log V)` – each edge can enter the heap once, and every heap operation costs `log V`.
- **Space complexity:** `O(V)` – the priority queue and `best_cost` dictionary hold at most one entry per vertex.

### Contributing

Bug reports and feature suggestions are welcome via GitHub issues. For larger changes, open an issue first to discuss scope and requirements.

### License

Distributed under the terms of the [MIT License](LICENSE). You are free to use, modify, and redistribute this project with appropriate attribution.

### Repository

Designed for the GitHub project [jahidbappi/BFS-path-search](https://github.com/jahidbappi/BFS-path-search) as a compact reference implementation of cost-aware BFS traversal.

