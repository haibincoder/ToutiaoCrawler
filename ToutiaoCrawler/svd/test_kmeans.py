from numpy import *
import time
import matplotlib.pyplot as plt

## step 1: load data
from ToutiaoCrawler.svd.k_means import kmeans, showCluster

print("step 1: load data...")
dataSet = []
fileIn = open('d:/test.txt')
for line in fileIn.readlines():
    lineArr = line.strip().split('\t')
    dataSet.append([float(lineArr[0]), float(lineArr[1])])

## step 2: clustering...
print("step 2: clustering...")
dataSet = mat(dataSet)
k = 4
centroids, clusterAssment = kmeans(dataSet, k)

## step 3: show the result
print("step 3: show the result...")
showCluster(dataSet, k, centroids, clusterAssment)