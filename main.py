import heapq

# зчитування графу з файлу
with open("input.txt", "r") as f:
    n = int(f.readline().strip())
    graph = [list(map(int, f.readline().strip().split())) for _ in range(n)]

# використання алгоритму Прима для побудови мінімального остовного дерева
visited = [False] * n
heap = [(0, 0)]
total_weight = 0
while heap:
    (weight, node) = heapq.heappop(heap)
    if not visited[node]:
        visited[node] = True
        total_weight += weight
        for i in range(n):
            if graph[node][i] != 0 and not visited[i]:
                heapq.heappush(heap, (graph[node][i], i))
                # додатково можна вивести ребра остовного дерева
                print("Edge: ({}, {})".format(node, i))

# виведення ваги мінімального остовного дерева
print("Total weight of MST:", total_weight)
