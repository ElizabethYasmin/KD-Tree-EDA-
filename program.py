from scipy import spatial
from time import time
import csv
import pandas as pd
import math

data = []

times = []

start_time = time()

data1 = []
with open('datos_para_test/test100.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data1.append(r)	
		else: 
			a+=1


elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data1)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data1)

start_time = time()

data2 = []
with open('datos_para_test/test500.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data2.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data2)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data2)

start_time = time()

data3 = []
with open('datos_para_test/test1000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data3.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data3)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data3)

start_time = time()

data4 = []
with open('datos_para_test/test5000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data4.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data4)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data4)

start_time = time()

data5 = []
with open('datos_para_test/test10000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data5.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data5)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data5)

start_time = time()

data6 = []
with open('datos_para_test/test20000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data6.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data6)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data6)

start_time = time()

data7 = []
with open('datos_para_test/test100000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data7.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data7)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data7)

start_time = time()

data8 = []
with open('datos_para_test/test200000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data8.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data8)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data8)

start_time = time()

data9 = []
with open('datos_para_test/test350000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data9.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data9)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data9)

start_time = time()

data10 = []
with open('datos_para_test/test500000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data10.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data10)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data10)

start_time = time()

data11 = []
with open('datos_para_test/test1000000.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile)
	a = 0
	for row in spamreader:
		r = []
		if a > 0:
			for i in range(1, len(row)):
				r.append(float(row[i]))
			data11.append(r)	
		else: 
			a+=1

elapse = time()-start_time

start_time = time()
tree = spatial.KDTree(data11)
elapsee = time()-start_time

times.append((elapse,elapsee))

data.append(data11)

def distancia(point1, point2):
	val = 0
	for i in range(len(point1)):
		val += (point1[i]-point2[i])*(point1[i]-point2[i])
	return math.sqrt(val)

def knn_fuerza_bruta(pointList, point, k):

	time_start = time()

	vecinos = []
	for j in range(k):
		nearest = pointList[0]
		a = 0
		while(True):
			if nearest in vecinos or nearest == point:
				a+=1
				nearest = pointList[a]
			else:
				break
		for i in range(len(pointList)):
			if (distancia(nearest,point) > distancia(pointList[i], point)):
				if not pointList[i] in vecinos and point != pointList[i]:
					nearest = pointList[i]
		#print(nearest)
		vecinos.append(nearest)

	elapse = time() - time_start

	return elapse

def kClosest(points, K, point):

	time_start = time()

	tree = spatial.KDTree(points)
	# x is the origin, k is the number of closest neighbors, p=2 refers to choosing l2 norm (euclidean distance)

	

	distance, idx = tree.query(x=point, k=K, p=2)

	elapse = time() - time_start 
	return elapse

for i in range(len(times)):
	print(times[i])

points = [[2,3],[5,4],[9,1],[4,7],[8,1]]

print(kClosest(points, 3, [2,3]))

for i in range(len(data)):
	print(knn_fuerza_bruta(data[i], data[i][int(len(data[i])/2)], 3), kClosest(data[i], 3, data[i][int(len(data[i])/2)]))