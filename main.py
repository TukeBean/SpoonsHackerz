import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request  # the lib that handles the url stuff
import csv

reviewLines = list()

f = open("C:\\Users\Marc\\Desktop\\realReview", encoding='utf8')
#print(f.readline())

for line in f :
    reviewLines.append(line)

for item in reviewLines:
    print(item)

#import and view dataset
#git clone https://github.com/TukeBean/SpoonsHackerz.git
#kickstarter = pd.read_csv("SpoonsHackerz/blob/master/dataset/fake_reviews.txt")
#print(kickstarter.shape)
#kickstarter.head(10)
#
#https://github.com/TukeBean/SpoonsHackerz/blob/master/dataset/fake_reviews.txt
#
##import and view dataset
#!git clone https://github.com/Jake-Young/AI-NI-Academy.git
#kickstarter = pd.read_csv("/content/AI-NI-Academy/AI NI Data Workshop/kickstarter2018.csv")
#print(kickstarter.shape)
#kickstarter.head(10)