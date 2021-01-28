import csv

with open("a1.csv", "a+", newline="")as f1:
    obj_csv = csv.writer(f1)
    while True:
        stdId = input("enter student id:")
        name = input("enter name:")
        std_cls = input("enter student class")
        obj_csv.writerow([stdId, name, std_cls])
        ch = input("Enter another record (Y/N): ")
        if ch.lower() == "n" or ch.lower() == "no":
            break
    f1.seek(0)
    obj_read_csv = csv.reader(f1)
    for i in obj_read_csv:
        print(i)
