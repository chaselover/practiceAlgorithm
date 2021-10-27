
from heapq import heappush, heappop

def cardinalitySort(nums):
    # Write your code here
    answer = []
    heap = []
    for num in nums:
        binary_cardinality = bin(int(num))[2:].count('1')
        heappush(heap, (binary_cardinality, num))
    while heap:
        answer.append(heappop(heap)[1])
    return answer

    
if __name__ == '__main__':
    

    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    result = cardinalitySort(nums)

    print(result)