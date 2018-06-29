import csv

f = open("in.csv", "r")
reader = csv.reader(f)
mylist = list(reader)
f.close()
print(mylist)

mylist[0][1] = "x"  # here 2 is third row starting from 0 and [0] is the cell postion
my_new_list = open('in.csv', 'w', newline='')
csv_writer = csv.writer(my_new_list)
csv_writer.writerows(mylist)  # you can use writerow also to get the data into 1 single column
my_new_list.close()