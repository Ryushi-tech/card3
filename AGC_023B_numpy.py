import numpy as np
from card3.void.stop_watch import stop_watch

@stop_watch
def main():
    n = int(input())
    A = np.array([list(input()) for _ in range(n)], dtype='str')
    ans = 0
    for i in range(n):
        B = np.block([A[:, i:], A[:, :i]])
        if (B == B.T).all():
            ans += n
    print(ans)
if __name__ == '__main__':
    main()