from collections import deque
import sys
read=sys.stdin.readline
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue=deque([start])
    # 현재 노드를 방문 처리
    visited[start]=True
    # 큐가 빌 때 까지 반복
    while queue: #
        # 큐에서 하나의 원소를 뽑아 출력
        v=queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


node, link=map(int, input().split()) # 노드수와 연결할 링크 수를 결정한다.
graph=[[] for _ in range(node+1)] #첫 노드는 0이므로 +1을 하여 초기 설정을 한다.
for j in range(1,node+1):
        add=list(map(int,input().split()))
        graph[j]+=add
visited=[False]*(node+1) # visited 배열을 False로 초기 설정을 해준다.

count=0 # 그래프 개수 저장

for i in range(1, node+1): # 1번 노드 부터 시작해서 순차적으로 반복해본다.
    if not visited[i]: # 만약 해당노드가 방문한 적이 없다면
        bfs(graph, i, visited) # 재귀함수를 호출한다
        count+=1 #재귀함수를 호출을 한뒤 dfs를 탐색한 후 갯수를 말한다


print(count)