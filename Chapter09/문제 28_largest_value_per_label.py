import collections
import heapq
from typing import List


cost = [6, 3, 6, 7, 8]
label = [5, 2, 2, 4, 5]
total_limit = 2
label_limit = 1


def take_largest_values_per_label(values: List[int], labels: List[int], total_limit, label_limit) -> int:
    costs = collections.defaultdict(list)
    
    for label, value in zip(labels, values):
        heapq.heappush(costs[label], -1*value)
    
    high_costs = []
    for label in set(labels):
        for i in range(label_limit):
            if not costs[label]:
                break
            high_costs += -1*heapq.heappop(costs[label]),
        
    return sum(sorted(high_costs, reverse=True)[:total_limit])


print(15 == take_largest_values_per_label(cost, label, total_limit, label_limit))