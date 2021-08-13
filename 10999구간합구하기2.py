import sys
import math
from collections import deque
import copy
input=sys.stdin.readline
INF=sys.maxsize

def init(arr,tree,start,end,node):
   if start==end:
      tree[node]=arr[start]
   else:
      mid = (start+end)//2
      init(arr,tree,start,mid,node*2)
      init(arr,tree,mid+1,end,node*2+1)
      tree[node]=tree[node*2]+tree[node*2+1]

def update_lazy(tree,lazy,node,start,end):
   if lazy[node] !=0:
      tree[node] += (end-start+1)*lazy[node]
      if start!=end:
         lazy[node*2]+=lazy[node]
         lazy[node*2+1]+=lazy[node]
      lazy[node]=0

def update_range(tree,lazy,start,end,node,idx_start,idx_end,dif):
   update_lazy(tree,lazy,node,start,end)
   if idx_start>end or start>idx_end: return

   if start>=idx_start and idx_end>=end:
      tree[node]+=(end-start+1)*dif
      if start!=end:
         lazy[node*2]+=dif
         lazy[node*2+1]+=dif
      return

   mid = (start+end)//2
   update_range(tree,lazy,start,mid,node*2,idx_start,idx_end,dif)
   update_range(tree,lazy,mid+1,end,node*2+1,idx_start,idx_end,dif)
   tree[node]=tree[node*2]+tree[node*2+1]

def sum(tree,lazy,start,end,node,left,right):
   update_lazy(tree,lazy,node,start,end)
   if left>end or start>right:return 0
   if start>=left and right>=end: return tree[node]

   mid=(start+end)//2
   return sum(tree,lazy,start,mid,node*2,left,right)+sum(tree,lazy,mid+1,end,node*2+1,left,right)

if __name__ == "__main__":
   n,m,k=map(int,input().split())
   arr=[int(input()) for _ in range(n)]
   val=[list(map(int,input().split())) for _ in range(m+k)]
   #tree_list=[0]*(pow(2,math.ceil(math.log(n,2))+1)-1)
   tree_list=[0]*(n*4)
   lazy=[0]*(n*4)
   init(arr,tree_list,0,n-1,1)
   
   for v in val:
      b,c=v[1],v[2]
      if v[0]==1: #b~c까지 d를 더함
         d=v[3]
         update_range(tree_list,lazy,0,n-1,1,b-1,c-1,d)
      else:
         print(sum(tree_list,lazy,0,n-1,1,b-1,c-1))