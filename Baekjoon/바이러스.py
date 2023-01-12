from collections import deque
import sys
read=sys.stdin.readline

def dfs(v):
    visit_list[v]=1
    for i in range(1, node+1):
        if visit_list[i]==0 and graph[v][i]==1:
            dfs(i)

node=int(input())
link=int(input())


graph=[[0]*(node+1) for _ in range(node+1)]
visit_list=[0]*(node+1)


for _ in range(link):
    a, b,=map(int, read().split())
    graph[a][b]=graph[b][a]=1
dfs(1)
print(sum(visit_list)-1)