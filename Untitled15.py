
# coding: utf-8

# In[1]:


x=5
x


# In[2]:


y


# In[3]:


def word_count(str):
    count=dict()
    w=str.split()

    for a in w:
        if a in count:
            count[a]+=1
        else:
            count[a]=1
    return count

str1=input("Enter the string:")
c=word_count(str1)
d=sorted(c.items())
print(d)


# In[4]:


A=set([1,2,3,4])
B=set([2,4,6,7])

print('Set A')
print(A)

print('Set B')
print(B)
print(1 in A)
print('Union')
print(A|B)
print('Union using function')
print(A.union(B))
print('Intersection')
print(A&B)
print('Intersection using function')
print(A.intersection(B))
print('Difference')
print(A-B)
print('Difference using function')
print(A.difference(B))
print('Symmetric Difference')
print(A^B)
print('Symmetric Difference using function')
print(A.symmetric_difference(B))


# In[6]:


for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            #break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')


# In[7]:


for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
       # continue
    print("Found a number", num)

