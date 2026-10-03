# Python + DSA Upskilling Demo

A compact Codementor tutoring sample for **Python fundamentals → DSA patterns → deliberate practice**.

## Tutoring path

1. **Fundamentals** — lists, dicts, sets, recursion vs iteration, Big-O intuition  
2. **Patterns** — hash maps, two pointers, sliding window, BFS/DFS, basic heaps  
3. **Practice** — timed drills, explain-out-loud, then optimize  

### Typical session arc

- Warm-up: complexity of a snippet you wrote (5 min)
- One pattern + one problem live (35–40 min)
- Homework: 2 similar problems + write the pattern in one sentence

## What’s in this repo

| Path | Content |
|------|---------|
| [`solutions/two_sum.py`](solutions/two_sum.py) | Classic hash-map Two Sum |
| [`solutions/bfs_sketch.py`](solutions/bfs_sketch.py) | BFS level-order sketch on an adjacency list |
| [`notes/complexity.md`](notes/complexity.md) | Short Big-O reminders tied to these solutions |

## How I teach

- Start from a **brute-force** you can defend, then tighten
- Name the pattern before coding (“this is a hash-map lookup”)
- Always state **time / space** after a working solution
- Prefer clarity over golf — internship and interview code should read cleanly

## Run

```bash
python solutions/two_sum.py
python solutions/bfs_sketch.py
```

---

*Demo for Codementor mentoring offers — topic/skill focused, not client-specific.*
