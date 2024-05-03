# Brandon Gurley
# Wednesday March 2nd, 2022
# Senior Project
# DBScan Clustering Algorithm

import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from datetime import datetime
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import v_measure_score
from sklearn.metrics import homogeneity_score
from sklearn.metrics import completeness_score
from collections import Counter
import re
from time import time
import pandas as pd
import matplotlib
from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
from scipy.spatial.distance import euclidean, cdist
from DBCV import DBCV


#Reads in CSV File Input Data
netData = pd.read_csv("HomeHost.csv")

#Variable Delclaration from CSV File Columns
timeSrcP = pd.DataFrame(netData, columns= ['Time', 'Source Port'])
timeSrcP = timeSrcP.fillna(timeSrcP.mean())

timeSrcIP = pd.DataFrame(netData, columns= ['Time', 'Source'])
timeSrcIP = np.nan_to_num(timeSrcIP)

timeDP=  pd.DataFrame(netData, columns= ['Time', 'Destination Port'])
timeDP = timeDP.fillna(timeDP.mean())

#List Conversions for Count
source = netData['Source'].tolist()
dest = netData['Destination'].tolist()
portSCount = netData['Source Port'].tolist()
portDCount = netData['Destination Port'].tolist()

print('\n')
#prints stripped string
sourceL=(Counter(source))
sourceL=(repr(sourceL).strip('Counter()'))
sourceL = re.sub("[{}]", "", sourceL)
sourceL = re.sub("['']", "", sourceL)
print("Source IP Count: ", sourceL)
print("\n")


#print("\nD ", destNoNthn)
destL=(Counter(dest))
destL = (repr(destL).strip('Counter()'))
destL = re.sub("[{}]", "", destL)
destL = re.sub("['']", "", destL)
print("Destination IP Count: ", destL)

print("\n")


#print("\nSPo ", portNoNthn)
portSCountL = (Counter(portSCount))
portSCountL =(repr(portSCountL).strip('Counter()'))
portSCountL = re.sub("[{}]", "", portSCountL)
portSCountL = re.sub("['']", "", portSCountL)
print("Source Port Count: ", portSCountL)
print("\n")


#print("\nDPo ", port2NoNthn)
portDCountL = (Counter(portDCount))
portDCountL= (repr(portDCountL).strip('Counter()'))
portDCountL = re.sub("[{}]", "", portDCountL)
portDCountL = re.sub("['']", "", portDCountL)
print("Destination Port Count: ", portDCountL)
print("\n")

output = open("DBSCANOUTPUT.txt", "w")


#determines the shape of the dataset
#print("time source overall dataset shape: ", timeSrcP.shape)
#print("time dest overall dataset shape: ", timeDP.shape)
#print("time source overall dataset shape: ", timeSrcIP.shape)
#print(timeDP)
#checks if any missing values in dataset
netData.isnull().any().any()


#Finds optimal EPS value for Time vs Source Port
neighb = NearestNeighbors(n_neighbors=2)
nbrs=neighb.fit(timeSrcP)
distances, indices = nbrs.kneighbors(timeSrcP)
distances = np.sort(distances, axis = 0)
distances = distances[:, 1]
plt.plot(distances)
plt.title("Neartest Neighbors to find Optimal EPS value (Time & Source Port)")
plt.show()

#Finds optimal EPS value for Time vs Destination Port
neighb = NearestNeighbors(n_neighbors=2)
nbrs=neighb.fit(timeDP)
distances, indices = nbrs.kneighbors(timeDP)
distances = np.sort(distances, axis = 0)
distances = distances[:, 1]
plt.plot(distances)
plt.title("Neartest Neighbors to find Optimal EPS value (Time & Destination Port)")
plt.show()

#Time vs Source Port Graphing
colors = ['red', 'blue']
timeSrcP= timeSrcP.to_numpy()
clustering = DBSCAN(eps=8.420 , min_samples=3).fit(timeSrcP)
labels = clustering.labels_
plt.figure(figsize=(13.34,7.5))
plt.scatter(timeSrcP[:, 0], timeSrcP[:, 1], c=labels,cmap = matplotlib.colors.ListedColormap(colors), s=45)
plt.title("Time vs Source Port")
plt.xlabel("Time (seconds)")
plt.ylabel("Source Port")
plt.show()

#Time vs Destination Port Graphing
colors = ['red', 'blue']
timeDP= timeDP.to_numpy()
clustering2 = DBSCAN(eps=159.9 , min_samples=4).fit(timeDP)
labels2 = clustering.labels_
plt.figure(figsize=(13.34,7.5))
plt.scatter(timeDP[:, 0], timeDP[:, 1], c=labels,cmap = matplotlib.colors.ListedColormap(colors), s=45)
plt.title("Time vs Destination Port")
plt.xlabel("Time (seconds)")
plt.ylabel("Destination Port ")
plt.show()

output.write("Source Port vs Time Clustering Analytics")
output.write("\n")

homoS = metrics.homogeneity_score(timeSrcP[:, 0], labels)
homoS = repr(homoS)
output.write("\nHomogeneity Score: "+ homoS)

compScore = metrics.completeness_score(timeSrcP[:, 0], labels)
compScore = repr(compScore)
output.write("\nCompleteness Score: "+ compScore)

vscore = v_measure_score(timeSrcP[:, 0], labels)
vscore = repr(vscore)
output.write("\nV Score: "+ vscore)

scorey= metrics.silhouette_score(timeSrcP,labels)
scorey = repr(scorey)
output.write("\nSilhouette Score: "+ scorey)

dbdb = (davies_bouldin_score(timeSrcP, labels))
dbdb = repr(dbdb)
output.write("\nDavies Bouldin Score: "+ dbdb)

CHS = metrics.calinski_harabasz_score(timeSrcP, labels)
CHS = repr(CHS)
output.write("\nCalinski Harabasz Score: "+ CHS)

dbcvscore = DBCV(timeSrcP,labels, dist_function=euclidean)
dbcvscore = repr(dbcvscore)
output.write("\nDBCV Score: "+ dbcvscore)

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

n_clusters_ = repr(n_clusters_)
n_noise_ = repr(n_noise_)
output.write("\nEstimated number of clusters: "+ n_clusters_)
output.write("\nEstimated number of noise points: "+ n_noise_)

output.write("\n")
output.write("\nDestination Port vs Time Clustering Analytics")
output.write("\n")

homoS2 = metrics.homogeneity_score(timeDP[:, 0], labels)
homoS2 = repr(homoS2)
output.write("\nHomogeneity Score: "+ homoS2)

compScore2 = metrics.completeness_score(timeDP[:, 0], labels)
compScore2 = repr(compScore2)
output.write("\nCompleteness Score: "+ compScore2)

vscore2 = v_measure_score(timeDP[:, 0], labels)
vscore2 = repr(vscore)
output.write("\nV Score: "+ vscore2)

scorey2= metrics.silhouette_score(timeDP,labels)
scorey2 = repr(scorey)
scorey2 = re.sub("['']", "", scorey2)
output.write("\nSilhouette Score: " + scorey2)

dbdb2 = (davies_bouldin_score(timeDP, labels))
dbdb2 = repr(dbdb2)
output.write("\nDavies Bouldin Score: "+ dbdb2)

CHS2 = metrics.calinski_harabasz_score(timeDP, labels)
CHS2 = repr(CHS2)
output.write("\nCalinski Harabasz Score: "+ CHS2)

dbcvscore2 = DBCV(timeDP,labels, dist_function=euclidean)
dbcvscore2 = repr(dbcvscore2)
output.write("\nDBCV Score: "+ dbcvscore2)

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)
n_noise_ = list(labels).count(-1)

n_clusters_ = repr(n_clusters_)
n_noise_ = repr(n_noise_)
output.write("\nEstimated number of clusters: "+ n_clusters_)
output.write("\nEstimated number of noise points: "+ n_noise_)
output.close()
