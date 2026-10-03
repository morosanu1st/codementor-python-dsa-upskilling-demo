# Complexity notes (tied to the demos)

## Two Sum (hash map)

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Nested loops | O(n²) | O(1) | Fine for tiny n; say why it’s slow |
| Hash map | O(n) | O(n) | One pass; trade space for speed |

Interview tip: state the O(n²) baseline first, then the map.

## BFS on adjacency list

- **Time:** O(V + E) — each vertex and edge processed once  
- **Space:** O(V) — queue + visited set  
- Use BFS for **unweighted** shortest path / level order; prefer Dijkstra when edges have weights

## Habit checklist

- [ ] Name inputs and constraints before coding  
- [ ] Give Big-O after the first working version  
- [ ] Mention one trade-off (e.g. memory vs speed)
