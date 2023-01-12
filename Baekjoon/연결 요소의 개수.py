import sys
sys.setrecursionlimit(10000) # 파이썬은 재귀제한이 걸려 있기 때문에 재귀 허용치를
#넘어가면 런타임 에러를 일으킨다. 이에 런타임 제한을 걸어주어야 한다.
def link_number(graph,v,visited): # DFS 함수이다.
    visited[v]=True # 노드를 방문 하면 TRUE로 바꿔 준다.
    for i in graph[v]: # 해당 그래프에 노드에서 연결되어 있는 노드들을 순차적으로 진행
        if not visited[i]: # 꺼내온 노드가 방문한 적이 없다면
            link_number(graph,i,visited) # 다시한번 재귀적으로 호출한다.

node, link=map(int, input().split()) # 노드수와 연결할 링크 수를 결정한다.
graph=[[] for _ in range(node+1)] #첫 노드는 0이므로 +1을 하여 초기 설정을 한다.
for i in range(link): #연결할 링크 수 만큼 반복한다.
    a, b=map(int, input().split())# map을 통해서 입력 받는다.
    graph[a] += [b]  # a에 b 연결 # 이차원 배열 같은 이와 같은 방식으로 concatenate를 할 수 있다.
    graph[b] += [a]  # b에 a 연결 -> 양방향
visited=[False]*(node+1) # visited 배열을 False로 초기 설정을 해준다.

count=0 # 그래프 개수 저장

for i in range(1, node+1): # 1번 노드 부터 시작해서 순차적으로 반복해본다.
    if not visited[i]: # 만약 해당노드가 방문한 적이 없다면
        link_number(graph,i,visited) # 재귀함수를 호출한다
        count+=1 #재귀함수를 호출을 한뒤 dfs를 탐색한 후 갯수를 말한다
print(count)