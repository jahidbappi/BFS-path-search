## BFS Path Search

This repository demonstrates a breadth-first style search that uses uniform-cost logic to locate the lowest-cost route from node `A` to node `P` in a weighted graph.

### Project Structure

- `task 5.py` – contains the graph configuration, the uniform-cost search loop (implemented without function definitions), and the complexity notes.

### How to Run

```bash
python "task 5.py"
```

The script prints the optimal path and the associated cost, or reports that no path exists.

### Algorithm Notes

- **Search strategy:** uniform-cost search implemented with a priority queue (`heapq`)
- **Time complexity:** `O(E log V)`
- **Space complexity:** `O(V)`

### Repository

Created for the GitHub project [jahidbappi/BFS-path-search](https://github.com/jahidbappi/BFS-path-search).

