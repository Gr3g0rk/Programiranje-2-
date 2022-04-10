import os
from os import listdir
from os.path import isfile, join

file1 = open('flaskReq.txt', 'r')
Lines = file1.readlines()
 
for line in Lines:
    zazeni = line.strip()
    os.system(zazeni)