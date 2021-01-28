import csv

list1 = [
    ['WDay', 'SFo', 'Phoenix', 'LasVegas'],
    ['Monday', '33', '38', '31'],
    ['Tuesday', '38', '39', '30'],
    ['Wednesday', '34', '41', '36'],
    ['Thursday', '30', '40', '33'],
    ['Friday', '35', '37', '30'],
    ['Saturday', '37', '40', '31'],
    ['Sunday', '36', '39', '37']]

with open("temp_csv", "w+", newline="") as f:
    obj = csv.writer(f)
    obj.writerows(list1)
    f.seek(0)
    obj_read = csv.reader(f)
    for i in obj_read:
        print(i)

with open("temp_csv", "a+", newline="") as f1:
    obj1 = csv.writer(f1)
    for i in list1:
        if i == list1[0]:
            header = input("enter city name: ")
            i.append(header)
        else:
            temp = input("enter temp: ")
            i.append(temp)
        obj1.writerow(i)

print("******************************")
with open("temp_csv", "a+", newline="") as f2:
    obj2 = csv.writer(f2)
    total, avg = 0, 0
    c = len(list1[0])-1
    list2 = []
    l = len(list1)
    list2.append("avg temp")
    for j in range(1, c):
        for i in range(1, l):
            total = total + int(list1[i][j])
        avg = total / (l - 1)
        list2.append(str(round(avg)))
        total = 0
    obj2.writerow(list2)
    f2.seek(0)
    obj2_read = csv.reader(f2)
    for i in obj2_read:
        print(i)




