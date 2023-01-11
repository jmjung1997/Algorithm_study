from collections import deque

# N, M을 공백으로 구분하여 입력받기

n,m=map(int,input().split())

# 2차원 리스트의 맵 정보 입력받기
graph=[]

for i in range(n):
    graph.append(list(map(int,input())))

    # 이동할 네 방향 정의(상, 하, 좌, 우)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

# BFS 소스코드 구현

def bfs(x,y):
    #큐(QUEUE) 구현을 위해 deque 라이브러리 사용
    queue=deque()
    queue.append((x,y))
    # 큐가 빌 때 까지 반복
    while queue:
        x, y=queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인

