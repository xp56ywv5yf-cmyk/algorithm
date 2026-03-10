"""
n = int(input())
plans = input().split()

x, y = 1, 1

move = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

for plan in plans:
    dx, dy = move[plan]
    nx = x + dx
    ny = y + dy

    if 1 <= nx <= n and 1 <= ny <= n:
        x, y = nx, ny

print(x, y)
"""
"""
import sys
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x - 1, y)  
        dfs(x + 1, y)  
        dfs(x, y - 1)  
        dfs(x, y + 1)  
        
        return True
    
    return False

result = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)
"""
"""
from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n - 1][m - 1]

print(bfs(0, 0))
"""
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()                  
b.sort(reverse=True)      

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))
"""
"""
n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

start = 0
end = max(rice_cakes)
result = 0

while start <= end:
    mid = (start + end) // 2
    
    total = 0
    for x in rice_cakes:
        if x > mid:
            total += x - mid

    if total >= m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
"""
"""
INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for mid in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][mid] + graph[mid][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print(-1)
else:
    print(distance)
"""