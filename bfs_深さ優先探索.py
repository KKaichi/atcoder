from collections import deque


def dfs(s):
    dist=[-1]*N
    dist[s]=0
    que = deque([s])
    while que:
        v = que.popleft()
        for w in G[v]:
            if dist[w] == -1:
                que.append(w)
                dist[w] = dist[v] + 1

    return dist
 