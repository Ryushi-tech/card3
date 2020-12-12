#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int) (n); i++)

bool ok(string s) {
  if (s[0] != 'A') return false;
  if (count(s.begin() + 2, s.end() - 1, 'C') != 1) return false;
  for (char c : s) {
    if (c != 'A' && c != 'C' && isupper(c)) return false;
  }
  return true;
}

int main() {
  string s;
  cin >> s;
  cout << (ok(s) ? "AC" : "WA") << endl;
}