#include <bits/stdc++.h>
using namespace std;
using ll = long long;
#define rep(i,n) for(int i = 0; i < (int) (n); i++)

const int lim = 202020;
const ll mod = 998244353;

ll powmod(ll n, ll k){
    k %= mod - 1;
    if (k < 0) k += mod - 1;
    ll ret = 1;
    while (k) {
        if (k & 1) ret = ret * n % mod;
        n = n * n % mod;
        k >>= 1;
    }
    return ret;
}

ll fac[lim], finv[lim], inv[lim];

void fac_build() {
  fac[0] = fac[1] = 1;
  finv[0] = finv[1] = 1;
  inv[1] = 1;
  for (int i = 2; i < lim; i++){
    fac[i] = fac[i - 1] * i % mod;
    inv[i] = mod - inv[mod % i] * (mod / i) % mod;
    finv[i] = finv[i - 1] * inv[i] % mod;
  }
}

ll nCr(int n, int k){
  if (n < k || n < 0 || k < 0) return 0;
  return fac[n] * (finv[k] * finv[n - k] % mod) % mod;
}

ll nPr(int n, int k){
  if (n < k || n < 0 || k < 0) return 0;
  return fac[n] * finv[n - k] % mod;
}

int main(){
  cin.tie(0);
  ios::sync_with_stdio(0);
  int n; cin >> n;
  fac_build();
  ll ans = 0;
  for (int i = 0; i <= n; i+=2) {
    ans += 2 * powmod(2, abs(n - 2 * i)) * nCr(n, i) % mod;
    if (ans > mod) ans -= mod;
  }
  cout << ans << "\n";
}