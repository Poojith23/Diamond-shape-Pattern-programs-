#!/usr/bin/env python
# coding: utf-8

# In[11]:


#diamond pattern of star

rows = 5
i = 1
while i <= rows:
    j = rows
    while j > i:
        # display space
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k < 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i += 1

i = rows - 1
while i >= 1:
    j = rows
    while j > i:
        print(' ', end=' ')
        j -= 1
    print('*', end=' ')
    k = 1
    while k <= 2 * (i - 1):
        print(' ', end=' ')
        k += 1
    if i == 1:
        print()
    else:
        print('*')
    i -= 1


# In[10]:


#Alphabets and letters pattern

ascii_number = 65
rows = 7
for i in range(0, rows):
    for j in range(0, i + 1):
        character = chr(ascii_number)
        print(character, end=' ')
        ascii_number += 1
    print(" ")


# In[9]:


#Pattern to display letter of the word

word = "Python"
x = ""
for i in word:
    x += i
    print(x)


# In[8]:


#Equilateral triangle pattern of characters/alphabets

print("Print equilateral triangle Pyramid with characters ")
size = 7
asciiNumber = 65
m = (2 * size) - 2
for i in range(0, size):
    for j in range(0, m):
        print(end=" ")
    m = m - 1
    for j in range(0, i + 1):
        character = chr(asciiNumber)
        print(character, end=' ')
        asciiNumber += 1
    print(" ")


# In[7]:


#Pattern of same character

# Same character pattern
character = 'K'
# convert char to ASCII
char_ascii_no = ord(character)
for i in range(0, 5):
    for j in range(0, i + 1):
        # Convert the ASCII value to the character
        user_char = chr(char_ascii_no)
        print(user_char, end=' ')
    print()


# In[ ]:




