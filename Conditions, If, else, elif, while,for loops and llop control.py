#!/usr/bin/env python
# coding: utf-8

# In[6]:


# F String
age=32
print(f"My age is:{age}" )


# In[9]:


## Format()
Name="Vivek"
Age= 28
print("My Name is {} and my age is {}".format(Name, Age))


# In[10]:


name=input("Enter the name")


# In[11]:


name


# In[13]:


age=int(input("Enter the age"))


# In[14]:


type(age)


# In[27]:


age=int(input("Enter the age"))

if age>=18 and age<=45:
     print("You are a Young blood")


# In[28]:


age=int(input("Enter the age"))

if age<45>=18:
     print("You are a Young blood")


# In[35]:


age=int(input("Enter the age"))

if age>=18 and age<=45:
     print("You are a Young blood")
else:     
     print("Thanku we will let you know")


# In[ ]:


# Mall - Input the product price
# Product >1000 rs 20% off
# Print the product price
## Product <=1000 rs 30% Off
## Print the product price after removing the discount


# In[46]:


Product_price = int(input( "Enter the Product_price" ))
if Product_price > 1000:
    print(f"Discounted_price={Product_price*0.8}")
if Product_price < 1000:
    
    print(f"Discounted_Price={Product_price*0.7}")


# In[47]:


Product_price = int(input("Enter the Product_price"))
if Product_price > 1000:
    print("The price of the product is {}".format(Product_price*0.8))
else:
    print("The price of the product is {}".format(Product_price*0.7))


# In[55]:


## Conditions

#Special Condition: if price=2999 you will get an additional gift
# Price==4000, you get a trip to goa


# In[57]:


Product_price=int(input("Enter the Price"))
if Product_price>3000:
    if  Product_price==4000:
        print("You got a trip to Goa")
    print("The product price is {}".format(Product_price*0.8))
elif Product_price>=2000 and Product_price<=3000:
    if Product_price==2999:
        print("Congratulations you are elgible for an additional gift")
    print("The product price is {}".format(Product_price*0.7))
elif Product_price>=1000 and Product_price<2000:
    print("The product_price is {}".format(Product_price*0.6))
else:
    print("Lets drink Tea")


# In[53]:


Product_price=int(input("Enter the Price"))
if Product_price>3000:
    print("The product price is {}".format(Product_price*0.8))
elif Product_price>=2000 and Product_price<=3000:
    print("The product price is {}".format(Product_price*0.7))
else: 
    print("The product_price is {}".format(Product_price*0.6))


# # Loop Statements
# 
# 1. While Loop
# 2. For Loop
# 3. Nested Loop
# 4. Loop Control(break, Continue,pass)

# In[68]:


#  While Loop: while-else
joining_age=25
while joining_age<=60:
    print(joining_age)
    joining_age=joining_age+1
else:
    print("It's time to retire")


# In[79]:


## ATM Machine with 1000 rs
Total_Amount = 1000
while Total_Amount!=0:
    Total_Amount=Total_Amount-100
    print(Total_Amount)
else:
          print('There is no money')


# In[80]:


## ATM Machine with 1000 rs
Total_Amount = 1000
while Total_Amount!=0:
    print(Total_Amount)
    Total_Amount=Total_Amount-100
    
else:
          print('There is no money')


# # For Loop

# In[81]:


list=["krish",1,2,3,4,"Apple", "Banana"]


# In[83]:


type(list)


# In[85]:


for i in list:
    print(i)


# In[86]:


fruit_list=["mango","Cherry","Apple","Banana"]


# In[89]:


for i in fruit_list:
    print(i)
    if i=="Cherry":
        print("The fruit is Cherry")


# In[90]:


fruit='Mango'
for x in fruit:
    print(x)


# In[93]:


fruit='Mango'
for x in fruit:
    print(x,end=' ')


# ## Nested Loop

# In[97]:


for i in range(1,6,2):
    print(i)


# In[98]:


#nested Loops

n=7

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")


# In[122]:


n=7

for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")


# In[128]:


def triangle(n):
  k = n - 1
  for i in range(0,n):
    for j in range(0,k):
      print(end = " ")
    k -= 1
    for j in range (0, i+1):
      print("* ", end='')
    print("\n") 

n = int(input())
triangle(n)


# In[ ]:




