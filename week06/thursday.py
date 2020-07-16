# Thursday: Reading and Writing Files

#Working with Text Files

# opening/creating and writing to a text file
print("- Opening and creating a text file")

f = open("test.txt", "w+") # "w" writing mode
f.write("this is a test")
f.close()

f = open("test.txt", "r")
data = f.read()
f.close()
print(data)

# opening/creating and writing to a csv file
print("- Opening and creating a csv file")

import csv
with open("test.csv", mode="w", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["Name", "City"])
    writer.writerow(["Craig Loug", "Taiwan"])
    
# reading from csv files
print("- Reading a csv file")

with open("test.csv", mode="r") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        print(row)
        
