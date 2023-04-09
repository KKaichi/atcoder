from collections import deque


def bfs(s):
    dist = [-1] * (N)
    que = deque([s])
    dist[s] = 0
    while que:
        v = que.popleft()
        d = dist[v]
        for w in G[v]:
            if dist[w] > -1:
                continue
            dist[w] = d + 1
            que.append(w)
