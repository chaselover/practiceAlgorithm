#include <stdio.h>
#include <string.h>
#define NMAX 105
#define MOD 1000000
 
int N;
int dp[NMAX][NMAX][NMAX][2];
 
long long int ret;
 
// l: 왼쪽에 남아있는 수 / r: 오른쪽에 남아있는 수 / s: 현재 골라야하는 방향
int sv(int idx, int l, int r, int s) {
    // 메모이제이션
    if(dp[idx][l][r][s] >= 0) return dp[idx][l][r][s];
 
    // 종료조건
    if(idx == N) {
        if(!l and !r) return dp[idx][l][r][s] = 1;
        else return dp[idx][l][r][s] = 0;
    }
    else {
        long long int ret=0;
 
        // 작은 수 고르는 단계
        if(s == 0) {
            for(int i=l-1;i>=0;i--) {
                ret = ( ret+sv(idx+1, i, r+(l-i-1), 1) )%MOD;
            }
        }
 
        // 큰 수 고르는 단계
        else {
            for(int i=r-1;i>=0;i--) {
                ret = ( ret+sv(idx+1, l+(r-i-1), i, 0) )%MOD;
            }
        }
 
        return dp[idx][l][r][s] = ret;
    }
}
 
int main() {
    // input
    scanf("%d", &N);
    
    if(N == 1) printf("1");
    else {
        // dp
        memset(dp, -1, sizeof(dp));
        for (int i=1;i<=N;i++) {
            for (int s=0;s<2;s++) {
                ret = ( ret+sv(1, i - 1, N - i, s) )%MOD;
            }
        }
        
        // print
        printf("%lld", ret);
    }
}