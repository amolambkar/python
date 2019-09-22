#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count_substring(string, sub_string):
    return len([i for i in range(len(string)) if string[i:i+len(sub_string)]==sub_string])

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


# In[ ]:



