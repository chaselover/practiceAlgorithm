def solution(arr):
    anagrams = set()
    for num in arr:
        counter = [0] * 10
        for char in str(num):
            counter[int(char)] += 1
        anagrams.add(tuple(counter))
    
    return len(anagrams)