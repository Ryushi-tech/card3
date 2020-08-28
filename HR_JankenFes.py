# from stop_watch import stop_watch
# @stop_watch
def solve():
    n, m = map(int, input().split())
    h = list(map(int, input().split()))
    acu = [[0] * 3 for _ in range(n + 1)]
    ADD = [[[], []] for _ in range(n + 1)]
    DEL = [[0] * 2 for _ in range(n + 1)]
    num = [0] * 3
    W = [0] * n
    L = [0] * n
    D = [0] * n
    for i in range(n):
        for j in range(3):
            acu[i + 1][j] = acu[i][j] + (h[i] == j)

    for _ in range(m):
        x, y = map(int, input().split())
        ADD[x - 1][0].append(y)  # x - 1 が始点の場合の終点の情報
        DEL[y][0] += 1  # 範囲の終点となった回数 imos?
        ADD[y][1].append(x - 1)  # y が終点の場合の始点の情報
        DEL[x - 1][1] += 1  # 範囲の始点となった回数 imos?

    valid = 0
    for i in range(n):  # i より後の手数に対する勝敗を探索
        valid -= DEL[i][0]  # 範囲の終点となった回数を引く
        for a in ADD[i][0]:
            valid += 1  # i 出現回数をカウント
            for j in range(3):
                num[j] += acu[a][j] - acu[i][j]  # a までの手数の総数
        num[h[i]] -= valid  # 総手数から i の分を引く
        W[i] += num[(h[i] + 1) % 3]
        L[i] += num[(h[i] + 2) % 3]
        D[i] += num[(h[i] + 3) % 3]

    num = [0] * 3
    valid = 0
    for i in range(n - 1, 0, -1):  # i より手前の手数に対する勝敗を探索
        for a in ADD[i + 1][1]:
            valid += 1
            for j in range(3):
                num[j] += acu[i + 1][j] - acu[a][j]
        num[h[i]] -= valid
        W[i] += num[(h[i] + 1) % 3]
        L[i] += num[(h[i] + 2) % 3]
        D[i] += num[(h[i] + 3) % 3]
        valid -= DEL[i][1]  # 範囲の始点となった回数を引く

    for i in range(n):
        print(W[i], L[i], D[i])


solve()

"""
#include <bits/stdc++.h>
using namespace std;
typedef signed long long ll;

#undef _P
#define _P(...) (void)printf(__VA_ARGS__)
#define FOR(x,to) for(x=0;x<(to);x++)
#define FORR(x,arr) for(auto& x:arr)
#define ITR(x,c) for(__typeof(c.begin()) x=c.begin();x!=c.end();x++)
#define ALL(a) (a.begin()),(a.end())
#define ZERO(a) memset(a,0,sizeof(a))
#define MINUS(a) memset(a,0xff,sizeof(a))

int N,M;
int H[101010];
int S[101010][3];
vector<int> add[101010][2];
int del[101010][2];
ll num[3];
ll W[101010],L[101010],D[103030];

void solve() {
	int i,j,x,y; string s;
	
	cin>>N>>M;
	FOR(i,N) {
		cin>>H[i];
		FOR(j,3) S[i+1][j]=S[i][j]+(H[i]==j);
	}
	FOR(i,M) {
		cin>>x>>y;
		add[x-1][0].push_back(y);
		del[y][0]++;
		add[y][1].push_back(x-1);
		del[x-1][1]++;
	}
  
	ll valid=0;
	FOR(i,N) {
		valid-=del[i][0];
		FORR(a,add[i][0]) {
			valid++;
			FOR(j,3) num[j]+=S[a][j]-S[i][j];
		}
		num[H[i]]-=valid;
		W[i]+=num[(H[i]+1)%3];
		L[i]+=num[(H[i]+2)%3];
		D[i]+=num[(H[i]+3)%3];
	}
	ZERO(num);
	valid=0;
	for(i=N-1;i>=0;i--) {
		FORR(a,add[i+1][1]) {
			valid++;
			FOR(j,3) num[j]+=S[i+1][j]-S[a][j];
		}
		num[H[i]]-=valid;
		W[i]+=num[(H[i]+1)%3];
		L[i]+=num[(H[i]+2)%3];
		D[i]+=num[(H[i]+3)%3];
		valid-=del[i][1];
	}
	
	FOR(i,N) cout<<W[i]<<" "<<L[i]<<" "<<D[i]<<endl;
}

int main(int argc,char** argv){
	string s;int i;
	if(argc==1) ios::sync_with_stdio(false), cin.tie(0);
	FOR(i,argc-1) s+=argv[i+1],s+='\n'; FOR(i,s.size()) ungetc(s[s.size()-1-i],stdin);
	cout.tie(0); solve(); return 0;
}
"""
