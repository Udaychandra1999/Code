import heapq
def min_steps(target,candies):
    heapq.heapify(candies)
    steps=0
    while candies[0]<target:
        new_candy=heapq.heappop(candies)+2*heapq.heappop(candies)
        heapq.heappush(candies,new_candy)
        steps+=1
    return steps
target_sweetness=int(input())
candies=list(map(int,input().split()))

result=min_steps(target_sweetness,candies)
print(result)