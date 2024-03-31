#!/usr/bin/env python
# coding: utf-8

# - 첫째 줄에 정수 N이 입력된다. (0<=N<=23)
# - 00시 00분 00초부터 N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수를 츨력한다. 

# In[1]:


# 모든 경우를 흩어야 하므로 3중 for문이 필요 = 완전 탐색(brute forcing)
# 데이터가 100만개 이하일 때 완전 탐색을 사용하는 것이 좋음

# 입력받기
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 3 포함 count 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
                
print(count)

