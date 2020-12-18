import csv
import math
with open("height-weight.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)


m = len(data)
print(m)
data.sort()



n = len(data) % 2
if(n == 0):
    new_data = math.floor(len(data)/2)   
    print(new_data)
    mode1 = float(data[new_data][2])
    mode2 = float(data[new_data-1][2])
    print(mode1)
    print(mode2)
    f_mode = mode1+mode2
    print("The median = ",f_mode/2.0)
else:
    new_data = math.floor(len(data)/2)
    print("The median = ",data[new_data][2])
