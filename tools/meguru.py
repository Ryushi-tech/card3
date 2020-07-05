def is_ok(i):
   return i <= 5


ok = -1
ng = 10
while ng-ok > 1:
    mid = (ok+ng) // 2 # 平均(小数切り捨て)
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok, ng)
