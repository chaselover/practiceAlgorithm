#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
typedef pair<ll,ll> pii;
#define ff first
#define ss second
 
vector<pii> edg[20202];
ll dis[303030];
ll inf=1e18;
 
ll in[303030];
ll out[303030];
 
vector<ll> lnk;
ll ans=1e18;
 
void dijk1(ll bit){
    priority_queue<pii,vector<pii>,greater<pii>> pq;
    for(auto x : lnk)
         if(x&(1 << bit)){
             pq.push({in[x],x});
             dis[x]=in[x];
         }
    while(!pq.empty()){
        auto x = pq.top(); pq.pop();
        if(dis[x.ss]<x.ff) continue;
        for(auto n : edg[x.ss])
            if(dis[x.ss]+n.ff<dis[n.ss]){
                dis[n.ss]=dis[x.ss]+n.ff;
                pq.push({dis[n.ss],n.ss});
            }
    }
}
 
void dijk2(ll bit){
    priority_queue<pii,vector<pii>,greater<pii>> pq;
    for(auto x : lnk)
         if( ! (x&(1 << bit))){
             pq.push({in[x],x});
             dis[x]=in[x];
         }
    
    while(!pq.empty()){
        auto x = pq.top(); pq.pop();
        if(dis[x.ss]<x.ff) continue;
        for(auto n : edg[x.ss])
            if(dis[x.ss]+n.ff<dis[n.ss]){
                dis[n.ss]=dis[x.ss]+n.ff;
                pq.push({dis[n.ss],n.ss});
            }
    }
}
 
int main(){
    ll i,j,k,l,m,n,u,v,c,d;
    scanf("%lld %lld",&n,&m);
    for(i=1;i<=m;i++){
        scanf("%lld %lld %lld %lld",&u,&v,&c,&d);
        if(u!=1&&v!=1) {
            edg[u].emplace_back(c,v);
            edg[v].emplace_back(d,u);
        }
        if(u*v==u){
            lnk.push_back(u);
            out[u]=c;
            in[u]=d;
        }
        if(v*u==v){
            lnk.push_back(v);
            out[v]=d;
            in[v]=c;
        }
    }
 
    for(i=0;i<=12;i++){
        for(j=1;j<=n;j++)
            dis[j]=inf;        
        dijk1(i);
        for(auto x:lnk)
            if( !(x&(1 << i)) ) 
                 ans=min(ans,out[x]+dis[x]);    
        for(j=1;j<=n;j++)
            dis[j]=inf;
        dijk2(i);
        for(auto x:lnk)
            if( (x&(1 << i)) ) 
                 ans=min(ans,out[x]+dis[x]);
    }
    printf("%lld",ans);
}