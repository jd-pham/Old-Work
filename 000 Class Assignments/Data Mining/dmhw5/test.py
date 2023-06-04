import heapq as hq

heap = []

hq.heappush(heap, 10)
hq.heappush(heap, 12)
hq.heappush(heap, 15)
hq.heappush(heap, 1)
hq.heappush(heap, 2)
hq.heappush(heap, 3)
hq.heappush(heap, 100)
hq.heappush(heap, 15)
hq.heappop(heap)
print(heap)


