class HashTable: 
    def __init__(self): 
        self.hash_table = list([0 for i in range(8)]) 
    def hash_function(self, key): 
        return key % 8 
    def insert(self, key, value): 
        hash_value = self.hash_function(hash(key)) 
        self.hash_table[hash_value] = value 
    def read(self, key): 
        hash_value = self.hash_function(hash(key)) 
        return self.hash_table[hash_value] 
    def print(self): print(self.hash_table)


# 출처: https://davinci-ai.tistory.com/19 [DAVINCI - AI]
