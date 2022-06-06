n=int(input())
a=[[*map(int,input().split())] for _ in range(n)]
adj=[[] for _ in range(2*n+1)]
for i in range(n-1):
  xi,yi,zi=a[i]
  for j in range(i+1,n):
    xj,yj,zj=a[j]
    if xi>=xj and yi>=yj and zi>=zj:
      adj[2*i+1].append(j+1)
      adj[2*i+2].append(j+1)
    elif xi<=xj and yi<=yj and zi<=zj:
      adj[2*j+1].append(i+1)
      adj[2*j+2].append(i+1)
def bfs():
  Q=[]
  dist[0]=-1
  for i in range(1,2*n+1):
    if pair_u[i]==0:
      dist[i]=0
      Q.append(i)
    else:
      dist[i]=-1
  while Q and dist[0]==-1:
    q=[]
    for i in Q:
      for j in adj[i]:
        if dist[pair_v[j]]==-1:
          dist[pair_v[j]]=dist[i]+1
          q.append(pair_v[j])
    Q=q
  return dist[0]>-1
def dfs(i):
  if i==0: return 1
  for j in adj[i]:
    if dist[pair_v[j]]==dist[i]+1:
      if dfs(pair_v[j]):
        pair_u[i]=j
        pair_v[j]=i
        return 1
  return 0
pair_u,pair_v=[0]*(2*n+1),[0]*(n+1)
dist=[0]*(2*n+1)
c=0
while bfs():
  for i in range(1,2*n+1):
    if pair_u[i]==0:
      if dfs(i):
        c+=1
print(n-c)