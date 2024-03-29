#define _USE_MATH_DEFINES
#include <iostream>
#include <complex>
#include <algorithm>
#include <vector>
using namespace std;

typedef complex<double> cpx;
typedef vector<cpx> vec;

const double pi = acos(-1);

void fft(vec &a, bool inv){
    int n = a.size();
    for(int i=1, j=0; i<n; i++){
        int bit = n >> 1;
        for(; bit<=j; bit>>=1) j -= bit;
        j += bit;
        if(i < j) swap(a[i],a[j]);
    }
    for(int len=2; len<=n; len<<=1){
        double ang = 2 * M_PI / len;
        if(inv) ang = -ang;
        cpx w(cos(ang), sin(ang));
        for(int i=0; i<n; i+=len){
            cpx wp(1, 0);
            for(int j=0; j<len/2; j++){
                cpx u = a[i + j], v = a[i + j + len/2] * wp;
                a[i + j] = u + v;
                a[i + j + len/2] = u - v;
                wp *= w;
            }
        }
    }
    if(inv){
        for(int i=0;i<n;i++){
			a[i] /= n;
			a[i] = cpx(round(a[i].real()), round(a[i].imag())); //result is integer
		}
    }
}

vector<int> mul(const vector<int> &a, const vector<int> &b){
	vec aa(a.begin(), a.end()), bb(b.begin(), b.end());
	int n = 1; while(n <= max(a.size(), b.size())) n <<= 1;
	aa.resize(n), bb.resize(n);
	fft(aa, 0), fft(bb, 0);
	for(int i=0; i<n; i++) aa[i] *= bb[i];
	fft(aa, 1);
	vector<int> ret(n);
	for (int i = 0; i < n; i++){
		ret[i] = round(aa[i].real());
		if(ret[i]) ret[i] = 1;
	}
	//while(ret.size() > 10 && ret.back() == 0) ret.pop_back();
	return ret;
}

vector<int> ori(1024);

vector<int> pw(vector<int> a, int b){
	/*vector<int> ret = ori;
	for(int i=1; i<b; i++){
		ret = mul(ret, a);
	}*/

	vector<int> ret = ori; b--;
	while(b){
		if(b & 1) ret = mul(ret, a);
		b >>= 1; a = mul(a, a);
	}
	return ret;
}

int main(){
	ios_base::sync_with_stdio(0); cin.tie(0);
	int n, k; cin >> n >> k;
	for (int i = 1; i <= n; i++){
		int t; cin >> t;
		ori[t] = 1;
	}
	vector<int> res = pw(ori, k);
	for (int i = 0; i < res.size(); i++){
		if (res[i]) cout << i << " ";
	}
}