# csv 文件读写
import sys
import csv

f = open("./test.csv", "w+", newline="")

f.write("name,age\n")
f.writelines(["haoyu1", ",", "25", "\n"])
f.writelines(["haoyu2", ",", "33", "\n"])

writer = csv.writer(f)
writer.writerow(["haoyu3", "11"])
f.close()

f = open("./test.csv", "r")
# for index, line in enumerate(f.readlines()):
#     if index == 0:
#         continue
#     print(line)
reader = csv.reader(f)
for line in reader:
    print(line[0], line[1])

f.close()
