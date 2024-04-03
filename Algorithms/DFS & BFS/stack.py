#!/usr/bin/env python
# coding: utf-8

# In[1]:


stack = []

# 삽입 5-2-3-7-삭제-1-4삭제
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력 

