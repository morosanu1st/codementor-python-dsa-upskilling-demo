"""BFS sketch — shortest path in an unweighted graph (adjacency list)."""

from __future__ import annotations

from collections import deque


def bfs_levels(graph: dict[str, list[str]], start: str) -> list[list[str]]:
    """Return nodes grouped by distance from start."""
    visited = {start}
    queue: deque[str] = deque([start])
    levels: list[list[str]] = []

    while queue:
        size = len(queue)
        level: list[str] = []
        for _ in range(size):
            node = queue.popleft()
            level.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        levels.append(level)
    return levels


if __name__ == "__main__":
    g = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": [],
    }
    print(bfs_levels(g, "A"))  # [['A'], ['B', 'C'], ['D']]
