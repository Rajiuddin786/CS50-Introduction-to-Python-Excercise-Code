import csv
import sys

if len(sys.argv) != 3:
    sys.exit("Invalid Input")
s = ''
s1 = ''
try:
    student = []
    with open(sys.argv[1]) as file:
        read = csv.reader(file)
        header = next(read)
        for row in read:
            comma = row[0]
            for i in comma:
                if i != '"':
                    s = s+i
            print(s)
            student.append({"frist":row[0],"last":row[1],"house":row[2]})
except FileNotFoundError:
    sys.exit(f"Could not find {sys.argv[1]}")
except IOError:
    sys.exit("Error: An I/O error occurred while reading or writing the files.")

with open(sys.argv[2],"a",newline='') as file:
    write = csv.DictWriter(file,fieldnames=["frist","last","house"])
    write.writeheader()
    write.writerows(student)
sys.exit(0)