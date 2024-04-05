#!/usr/bin/env python
# coding: utf-8

# In[4]:


def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

factorial_iterative(3)


# In[3]:


def factorial_recursive(n):
    if n<= 1:
        return 1
    #n! - n * (n - 1)!
    return n * factorial_recursive(n-1)

factorial_recursive(3)

