#include <stdio.h>
#include <vector>
#include <utility>
#define NMAX 300010
#define PAIR pair<int,int>
using namespace std;
 
int N, C, t, sz;
vector< int > mergeTree[NMAX*4];
int maxColor[NMAX*4];
 
PAIR tmp, vmax, ans;
 
int Q, a, b;
 
// 머지소트트리의 현재 인덱스(idx)에서 특정 색깔(val)의 개수 반환
int getColorCnt(int idx, int val) {
    int l, r, mid;
    int idxl, idxr;
 
    // 가장 왼쪽에 위치한 val의 위치 구하기
    l = 0; r = mergeTree[idx].size()-1;
    while(l<=r) {
        mid = (l+r)/2;
 
        if(mergeTree[idx][mid] < val) l = mid+1;
        else r = mid-1;
    }
    if(mergeTree[idx][l] != val) return 0;
    else idxl = l;
 
    // 가장 오른쪽에 위치한 val의 위치 구하기
    l = 0; r = mergeTree[idx].size()-1;
    while(l<=r) {
        mid = (l+r)/2;
 
        if(mergeTree[idx][mid] <= val) l = mid+1;
        else r = mid-1;
    }
    idxr = r;
 
    return (idxr-idxl)+1;
 
}
 
// 구간[l, r]에서 색깔(val)의 개수 가져오기
PAIR searchColor(int l, int r, int val) {
    PAIR ret;
 
    ret = make_pair(0, val);
    while(l<=r) {
        if(l%2 == 1) ret.first += getColorCnt(l++, val);
        if(r%2 == 0) ret.first += getColorCnt(r--, val);
 
        l/=2; r/=2;
    }
 
    return ret;
}
 
// 구간[l, r]에서 가장 많은 색깔과 개수 탐색
PAIR search(int l, int r) {
    int ll, rr;
    PAIR ret;
 
    ll = l; rr = r;
    ret = make_pair(0, 0);
    while(ll<=rr) {
        // maxColor[ll]/maxColor[rr]의 개수 중 최댓값 구하기
        if(ll%2 == 1) ret = max( ret, searchColor(l, r, maxColor[ll++]) );
        if(rr%2 == 0) ret = max( ret, searchColor(l, r, maxColor[rr--]) );
 
        ll/=2; rr/=2;
    }
 
    return ret;
}
 
 
// 머지소트트리의 현재 인덱스(idx)에서 가장 많은 색깔 찾기
void cntColor(int idx) {
    if(tmp.second == mergeTree[idx].back()) tmp.first++;
    else {
        vmax = max( vmax, tmp );
        tmp = make_pair(1, mergeTree[idx].back());
    }
}
 
int main() {
    // input
    scanf("%d %d", &N, &C);
    for(sz=1;sz<N;sz*=2);
    for(int i=0;i<N;i++) {
        scanf("%d", &t);
        // 바로 머지소트트리에 넣기
        mergeTree[sz+i].push_back(t);
 
        // 현재 구간에서 가장 많은 색깔 넣기
        maxColor[sz+i] = t;
    }
 
    // 머지소트트리 만들기
    for(int i=sz-1;i>0;i--) {
        int idxl, idxr, l, r;
 
        // 초깃값
        tmp = vmax = {0,0};
        l = i*2; r = i*2+1;
        idxl = idxr = 0;
 
        // 머지소트
        while(idxl<mergeTree[l].size() and idxr<mergeTree[r].size()) {
            if(mergeTree[l][idxl] < mergeTree[r][idxr]) mergeTree[i].push_back(mergeTree[l][idxl++]);
            else mergeTree[i].push_back(mergeTree[r][idxr++]);
 
            cntColor(i);
        }
 
        // 나머지 값 처리
        while(idxl<mergeTree[l].size()) {
            mergeTree[i].push_back(mergeTree[l][idxl++]);
            cntColor(i);
        }
        while(idxr<mergeTree[r].size()) {
            mergeTree[i].push_back(mergeTree[r][idxr++]);
            cntColor(i);
        }
 
        // 현재 구간에서 가장 많은 색
        vmax = max( vmax, tmp );
        maxColor[i] = vmax.second;
    }
 
 
    // 쿼리 처리
    scanf("%d", &Q);
    for(int i=1;i<=Q;i++) {
        scanf("%d %d", &a, &b);
        a--; b--;
 
        ans = search(a+sz, b+sz);
        if(ans.first > (b-a+1)/2) printf("yes %d\n", ans.second);
        else printf("no\n");
    }
}