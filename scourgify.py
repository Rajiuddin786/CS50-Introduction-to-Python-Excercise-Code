import sys
from csv import reader
from csv import DictWriter

first_name = []
last_name = []
house_of_them = []
with open("before.csv",errors='ignore') as file:
    read = reader(file)
    head= next(read)
    first_name.append("first")
    last_name.append("last")
    house_of_them.append("house")
    for first,last,house in read:
        first_name.append(first)
        last_name.append(last)
        house_of_them.append(house)

with open("after.csv","a") as file:
    write = DictWriter(file,fieldnames=["first","last","house"])
    for first2,last2,house2 in zip(first_name,last_name,house_of_them):
        write.writerow({"first":first2,"last":last2,"house":house2})