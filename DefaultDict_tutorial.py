#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict
d = defaultdict(list)
list_m=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    list_m=list_m+[input()]  

for i in list_m: 
    if i in d:
        print(" ".join(map(str,d[i])))
    else:
        print(-1)


# In[ ]:




