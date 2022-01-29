import csv
f1  = open("students.csv","r")
data = csv.reader(f1)
#print(data)
next(data)
for s in data:
    if s[3]== "M" and s[5]<= "3":
        print(s[1],s[5])
f1.close()