#!/usr/bin/env python
# coding: utf-8

# # Searching 

# ## (1) Linear Search

# In[1]:


# In linear search we have to traverse each and every element one by one..
# We have to compare each element with the given key
# Given an array of n elements you have to search x in that array and return it's position


# In[2]:


def linear_Search(arr,n,x):
    for i in range(n):
        if arr[i]==x:
            return i
    return -1


# In[3]:


array = [10,20,30,12,23,45]
x = 12
print(f"Element {x} found at  index {linear_Search(array,len(array),x)} or position {linear_Search(array,len(array),x)+1}")


# In[4]:


#time complexity of linear search is O(n)
# another approach


# In[5]:


def search(arr,x):
    left = 0
    length = len(arr)
    position = -1
    right = length-1
    for left in range(0,right,1):
        if (arr[left]==x):
            position = left
            print(f"Element found in Array at {position +1} Position with  {left + 1}  Attempt")
            break
        if (arr[right]==x):
            position = right
            print("Element found in Array at ", position + 1,
                  " Position with ", length - right, " Attempt")
            break
        left+=1
        right-=1
        if position==-1:
            pass
                  
        
    


# In[6]:


arr = [1,2,3,4,5]
x = 5
search(arr,x)


# ## (2) Binary Search

# In[7]:


# Binary search is  another way of searching which takes O(logn) comparatively less than that of linear search
# Binary search is only applicable when you have sorted array
# It is based on divide and conquer approach..We generally divide the array into two equal halves and then search accordingly. 


# ### Search a sorted array by repeatedly dividing the search interval in half. Begin with an interval covering the whole array. If the value of the search key is less than the item in the middle of the interval, narrow the interval to the lower half. Otherwise narrow it to the upper half. Repeatedly check until the value is found or the interval is empty.

# In[8]:


def B_search(array,left,right,value):
    if right>=left:# right is starting index and left is ending index
        middle = (right+left)//2
        if(array[middle]==value):
            return middle
        elif array[middle]>value:
            return B_search(array,left,middle-1,value)
        else:
            return B_search(array,middle+1,right,value)
    else:
        return -1
    
            
            
        


# In[9]:


import random
arr =  [10,22,32,34,43,62,71,81,92,110]
x = random.choice(arr)
print("Element = ",x)
result = B_search(arr,0,len(arr)-1,x)
if(result>=0):
    print(f"Element {x} found at index {result} ")
else:
    print("-1")


# ## (3)Exponential Search

# In[10]:


# Exponential search uses binary search for searching the element 
# It also takes O(logn) time to search.


# ## In Exponential Search we generally find a range in which the search_element lies and further we perform binary search in that range.

# In[12]:


list1=list(map(int, input().split(" "))) # take input in the form of list...
val=int(input()) # value after getting complete list
if list1[0] == val: # if element is at index 0 simply print("0")
    print("0")
i = 1 # or just use loop counter for further approach
#Finding range for binarySearch
while(i<len(list1) and list1[i]<=val): # condition for finding the range 
        i = i * 2
min1=min(i,len(list1))
def binarySearch(data_list,low,high,value): # same above approach of binary search
    if(high>= low):
        mid=int(low + ( high-low )//2)
        if data_list[mid] == value:
            return mid
        if data_list[mid] > value:
            return binarySearch(data_list,low,mid - 1,value)
        else:
            return binarySearch(data_list,mid + 1,high,value)
    if(high<low):
        return -1
    # Applying binary search for specified range
index=binarySearch(list1,i/2,min(i,len(list1)),val)
if(index==-1):
    print("Element not found")
else:
    print("Element found at ",index)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




