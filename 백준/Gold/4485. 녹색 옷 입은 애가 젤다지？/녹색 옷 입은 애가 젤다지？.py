# 4485. 녹색 옷 입은 애가 젤다지?
from heapq import heappop, heappush

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra(start_x, start_y):
    distance[start_x][start_y] = cave[start_x][start_y]
    heap = [(cave[start_x][start_y], start_x, start_y)]

    while heap:
        min_dist, min_x, min_y = heappop(heap)
        if min_dist > distance[min_x][min_y]:
            continue

        for d in range(4):
            nx = min_x + dx[d]
            ny = min_y + dy[d]

            if 0 <= nx < n and 0 <= ny < n:
                new_dist = min_dist + cave[nx][ny]
                if new_dist < distance[nx][ny]:
                    distance[nx][ny] = new_dist
                    heappush(heap, (new_dist, nx, ny))


    return distance[-1][-1]

t = 0
while True:
    t += 1
    n = int(input())
    if n == 0:
        break
    cave = [list(map(int, input().split())) for _ in range(n)]
    INF = 99999999
    distance = [[INF] * n for _ in range(n)]
    dijkstra(0, 0)
    print(f'Problem {t}:', dijkstra(0, 0))
