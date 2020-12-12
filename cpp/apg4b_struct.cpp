#include<bits/stdc++.h>
using namespace std;

#define rep(i, n) for (int i = 0; i < (int) (n); i++)
#define all(x) x.begin(), x.end()
template<class T>
void print(const T &t) { cout << t << "\n"; }

struct Clock {
    int hour;    //時間を表す (0~23の値をとる)
    int minute;  //分を表す   (0~59の値をとる)
    int second;  //秒を表す   (0~59の値をとる)

    void set(int h, int m, int s) {
        hour = h;
        minute = m;
        second = s;
    }

    string to_str() {
        string ret;
        if (hour < 10) ret += "0";
        ret += to_string(hour);
        ret += ":";
        if (minute < 10) ret += "0";
        ret += to_string(minute);
        ret += ":";
        if (second < 10) ret += "0";
        ret += to_string(second);
        return ret;
    }

    void shift(int diff_second) {
        int diff_hour = diff_second / 3600;
        diff_second %= 3600;
        int diff_minute = diff_second / 60;
        diff_second %= 60;

        second += diff_second;
        if (second > 59) { minute += 1; second -= 60; }
        else if (second < 0) { minute -= 1; second += 60; }

        minute += diff_minute;
        if (minute > 59) { hour += 1; minute -= 60; }
        else if (minute < 0) { hour -= 1; minute += 60; }

        hour += diff_hour;
        if (hour > 23) { hour -= 24; }
        else if (hour < 0) { hour += 24; }
    }
};

int main() {
  int hour, minute, second;
  cin >> hour >> minute >> second;
  int diff_second;
  cin >> diff_second;
  Clock clock;
  clock.set(hour, minute, second);
  print(clock.to_str());
  clock.shift(diff_second);
  print(clock.to_str());
}