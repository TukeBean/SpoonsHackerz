import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request  # the lib that handles the url stuff
import csv

reviewLines = list()

f = open(".\\dataset\\real_reviews.txt", encoding='utf8')
#print(f.readline())

for line in f :
    reviewLines.append(line)

for item in reviewLines:
    print(item)

