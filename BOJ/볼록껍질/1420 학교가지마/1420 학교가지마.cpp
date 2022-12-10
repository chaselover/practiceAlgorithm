#include <bits/stdc++.h>
using namespace std;

typedef pair<int, int> p;
const int inf = 1e9;

char arr[111][111];
vector<int> g[23232];
int par[23232];
map<p, int> c, f;
int s = -1, t = -1;
int si, sj, ti, tj;

int n, m;

void addEdge(int s, int e, int x){
	g[s].push_back(e); c[{s, e}] = x;
	g[e].push_back(s); c[{e, s}] = 0;
}

int run(){
	int ret = 0;
	while(1){
		memset(par, -1, sizeof par);
		queue<int> q; q.push(s);
		while(q.size()){
			int now = q.front(); q.pop();
			for(auto nxt : g[now]){
				if(par[nxt] == -1 && c[{now, nxt}] - f[{now, nxt}] > 0){
					q.push(nxt); par[nxt] = now;
				}
			}
		}
		if(par[t] == -1) break;
		for(int i=t; i!=s; i=par[i]){
			int a = par[i], b = i;
			f[{a, b}]++;
			f[{b, a}]--;
		}
		ret++;
	}
	return ret;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	cin >> n >> m;

	int pv = 0;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			cin >> arr[i][j];
			if(arr[i][j] == 'K'){
				s = pv + 1;
				si = i, sj = j;
			}
			if(arr[i][j] == 'H'){
				t = pv;
				ti = i, tj = j;
			}
			pv += 2;
		}
	}

	if(n == 1 && m == 1){
		cout << -1; return 0;
	}
	if(abs(si - ti) + abs(sj - tj) == 1 || s == -1 || t == -1){
		cout << -1; return 0;
	}

	for(int i=0; i<n*m; i++){
		addEdge(2*i, 2*i+1, 1);
	}

	pv = 0;
	for(int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			if(i+1 < n && arr[i][j] != '#' && arr[i+1][j] != '#'){
				int nxt = pv + 2 * m;
				addEdge(pv+1, nxt, inf);
				addEdge(nxt+1, pv, inf);
			}
			if(j+1 < m && arr[i][j] != '#' && arr[i][j+1] != '#'){
				int nxt = pv + 2;
				addEdge(pv+1, nxt, inf);
				addEdge(nxt+1, pv, inf);
			}
			pv += 2;
		}
	}

	cout << run();
}