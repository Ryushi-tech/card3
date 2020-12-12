#include<bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int) (n); i++)
template<class T>
void print(const T &t) { cout << t << " "; }

int main() {
    cin.tie(0);
    ios::sync_with_stdio(0);

    int n; cin >> n;
    vector <pair<int, int>> p(n);
    rep(i, n) cin >> p[i].second >> p[i].first;
    sort(p.begin(), p.end());
    rep(i, n) cout << p[i].second << " " << p[i].first << "\n";
}
