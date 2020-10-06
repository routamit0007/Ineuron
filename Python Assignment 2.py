#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(5):
    for j in range(i):
        print('*',end =" ")
    print(" ")
for i in range(6):
    for k in range(5-i):
        print('*' , end = " ")
    print("")


# In[4]:


value = input("Enter name you want to print in reverse order : ")
print(value[::-1])


# In[ ]:




