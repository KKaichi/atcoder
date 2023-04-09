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

N=int(input())
G=[[] for _ in range(N)]
for i in range(N-1):
   a,b=map(int,input().split())
   a-=1
   b-=1
   G[a].append(b)
   G[b].append(a)

dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)
 