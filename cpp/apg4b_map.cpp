#include<bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int) (n); i++)
#define all(x) x.begin(), x.end()
template<class T>
void print(const T &t) { cout << t << "\n"; }

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int n; cin >> n;
    vector <int> p(n);
    rep(i, n) cin >> p[i];

    map<int, int> d;
    for (int pp : p) {
        if (d[pp]) d[pp]++;
        else d[pp] = 1;
    }

    int ans = 0;
    int tmp = 0;
    for (int pp: p) {
        if (d[pp] > ans) {
            ans = d[pp]; tmp = pp;
        }
    }
    cout << tmp << " " << ans << "\n";
}
