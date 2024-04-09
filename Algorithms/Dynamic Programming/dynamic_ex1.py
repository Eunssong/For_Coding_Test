# -*- coding: utf-8 -*-
"""dynamic_ex1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UjL0pWbUKisD8A2FYnJRWuhVYJwkQilf
"""

n, m = map(int, input().split())

array = []
for i in range(n):
  array.append(int(input()))

d = [10001] * (m+1)

d[0]=0
for i in range(n):
  for j in range(arrya[i], m+1):
    if d[j - array[i]] != 1001:
      d[j] = min(d[j], d[j-array[i]]+1)

if d[m] == 10001:
  print(-1)
else:
  print(d[m])