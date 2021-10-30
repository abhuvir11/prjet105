import csv
import math 

with open("data.csv",newline="") as b:
    reader=csv.reader(b)
    file_data=list(reader)
file_data.pop(0)

def mean(data):
    n = len(data)
    total =0
    for x in data:
        total= total + int(x)

    mean =total/n
    return mean

squared_list = []

for number in file_data:
    a= int(number)- mean(file_data)
    a = a**2
    squared_list.append(a)


sum = 0
for i in squared_list :
    sum = sum +i

 
result = sum/(len(file_data)-1)

std_dev = math.sqrt(result)
print(std_dev)