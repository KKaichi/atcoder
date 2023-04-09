from collections import deque


def dfs(s):
    dist = [-1] * N
    dist[s] = 0
    que = deque([s])
    while que:
        v = que.popleft()
        for w in G[v]:
            if dist[w] == -1:
                que.append(w)
                dist[w] = dist[v] + 1

    return dist


N = int(input())
G = [[] for _ in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
print(max(distmv) + 1)

"""
閉路の長さとは
頂点 u,vに辺を結ぶことでできる閉路の長さは、
パス u-vの長さ + 1

木の直径は次の方法で求められます (証明は略)。

適当な頂点 uを 1 つ選ぶ
頂点 uから最も遠い頂点 vを求める (O(N))
頂点 vから最も遠い頂点 wを求める (O(N))
このとき、パス v-wの長さが求める直径になります。それに 1 を足して出力すればよいです。

なお、木において 1 頂点 sから各頂点 vへの距離を求めるのは DFS でも BFS でも求められます。下に挙げるコードでは DFS で実装しています。
計算量は O(N)になります。
"""
