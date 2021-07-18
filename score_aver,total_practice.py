#coding: utf-8

#성적 총점 평점.
list1 = [1,3, 6, 78, 35, 55]
list2 = [12,24,35,24,88,120,155]

#교집합 찾기.= 합집합- 반달1-반달2
#1:1대응
def intersect(x,y):
    return(set(x)&set(y))
    
print("두 배열의 공통된부분은?:{0}".format(intersect(list1,list2)))