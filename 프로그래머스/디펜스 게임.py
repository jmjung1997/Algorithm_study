import heapq
def solution(n, k, enemy): ## 솔루션 함수 정의
    heap=[]
    if len(enemy)==k:
        return len(enemy)
    for i in range(len(enemy)):
        if n>=enemy[i]:
            heapq.heappush(heap, -enemy[i])
            n-=enemy[i]
        else:
            if k>0:
                if heap:
                    a=-heapq.heappop(heap)
                    k-=1
                    if a>enemy[i]:
                        n+=a-enemy[i]
                        heapq.heappush(heap,-enemy[i])
                    elif a==enemy[i]:
                        heapq.heappush(heap,-enemy[i])
                    else:
                        heapq.heappush(heap, -a)
                else:
                    k-=1
            else:
                return i

    return len(enemy)

enemy=list(map(int,input().split()))

n,k=map(int, input().split())
answer=solution(n,k,enemy)
print(answer)