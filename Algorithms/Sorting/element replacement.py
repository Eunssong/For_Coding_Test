#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, k = map(int, input().split()) 
a = list(map(int, input().split())) # element
b = list(map(int, input().split())) # element 

a.sort() # 오름차순
b.sort(reverse = True) # 내림차순

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break

print(sum(a))

