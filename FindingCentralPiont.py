n = int(input())
arr = []
for i in range(n):
    ele = int(input())
    arr.append(ele)
sum = 0
for i in arr:
  sum+=i
sum_from_begin=0
for i in range(n):
  sum_from_begin+=arr[i]
  if sum_from_begin==(sum-sum_from_begin):
    print(i)
    break
else:
  print(-1)
