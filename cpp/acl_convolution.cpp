#include<bits/stdc++.h>
#include<atcoder/all>

using namespace std;
using namespace atcoder;
using mint = modint998244353;

typedef long long ll;
#define rep(i, n) for (int i = 0; i < (int) (n); i++)
template<class T> void print(const T& t){ cout << t << " "; }

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int n, m;
    cin >> n >> m;

    vector<ll> a(n), b(m);
    rep(i, n) cin >> a[i];
    rep(i, m) cin >> b[i];

    vector<ll> c = convolution(a,b);
    for(ll x:c) print(x);

    return 0;
}