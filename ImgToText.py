#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Importing library pytesseract,install the tesseract-ocr,adding the path of it.
import pytesseract as tss
tss.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


# In[28]:


#importing the library
from PIL import Image
import datefinder


# In[30]:


#Importing the user input image
imageFileName =input("enter the image name with absolute path ")


# In[31]:


#openin the image file path that we have given
img = Image.open(imageFileName)


# In[32]:


#coverting the image text into string
text = tss.image_to_string(img)


# In[33]:


#printing the converted text
print(text)


# In[35]:


# By using datefinder funtion we are extracting dates from text
matches = datefinder.find_dates(text)


# In[36]:


for match in matches:
    print(match)


# In[ ]:




