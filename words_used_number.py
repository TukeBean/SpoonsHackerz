import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request  # the lib that handles the url stuff
import csv

reviewLinesR = list()

fr = open(".\\dataset\\real_reviews.txt", encoding='utf8')
#print(f.readline())

for line in fr :
    reviewLinesR.append(line)
    
reviewLinesF = list()

ff = open(".\\dataset\\fake_reviews.txt", encoding='utf8')
#print(f.readline())

for line in ff :
    reviewLinesF.append(line)
    
       
    

#for item in reviewLines:
#    print(item)


##----------------------- ^ Don't fuck with ^ ---------------------------------
    
#charCount = (reviewLines)

 
 ##prints list of number of characters per review 
#for item in charCount:
#    print(len(item))
 
##prints list of number of words per review
#for item in reviewLines:
   # print (len(item.split()))
    
    
##----------------------- ^ Don't fuck with ^ ---------------------------------

wordCountR = list()

for item in reviewLinesR:
    wordCountR.append(len(item.split()))
    
print (wordCountR)

wordCountF = list()

for item in reviewLinesF:
    wordCountF.append(len(item.split()))
    
print (wordCountF)
#list created = wordCount