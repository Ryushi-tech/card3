#include<bits/stdc++.h>
#include<atcoder/all>

using namespace std;
using namespace atcoder;
#define rep(i, n) for (int i = 0; i < (int) (n); i++)

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int n, q;
    cin >> n >> q;

    dsu uf(n);
    rep(i, q) {
        int t, u, v;
        cin >> t >> u >> v;
        if (t) cout << uf.same(u, v) << '\n';
        else uf.merge(u, v);
    }
    return 0;
}
