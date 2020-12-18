import csv
from collections import Counter
with open("height-weight.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)

New_data = []
for i in range(len(data)):
    new_data = data[i][2]
    New_data.append(new_data)
   # new_data = float(new_data)


count = Counter(New_data)

mode_data = {
    "70-80":0,
    "80-90":0,
    "90-100":0,
    "100-110":0,
    "110-120":0,
    "120-130":0,
    "130-140":0,
    "140-150":0,
    "150-160":0,
    "160-170":0,
}


for weight,occurence in count.items():
    if 110 < float(weight) < 120:
        mode_data["110-120"] += occurence
    elif 120 < float(weight) < 130:
        mode_data["120-130"] += occurence
    elif 130 < float(weight) < 140:
        mode_data["130-140"] += occurence
    elif 140 < float(weight) < 150:
        mode_data["140-150"] += occurence
    elif 150 < float(weight) < 160:
        mode_data["150-160"] += occurence
    elif 160 < float(weight) < 170:
        mode_data["160-170"] += occurence
    elif 70 < float(weight) < 80:
        mode_data["70-80"] += occurence
    elif 80 < float(weight) < 90:
        mode_data["80-90"] += occurence
    elif 90 < float(weight) < 100:
        mode_data["90-100"] += occurence
    elif 100 < float(weight) < 110:
        mode_data["100-110"] += occurence



print(mode_data)


mode_range,mode_occurence = 0,0

for range,occurence in  mode_data.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence = [int(range.split('-')[0]), int(range.split('-')[1])],occurence

print(mode_range)
print(mode_occurence)
print(occurence)
mode = float((mode_range[0] + mode_range[1]) / 2)
print(mode)
print("Mode is -> ",mode)
