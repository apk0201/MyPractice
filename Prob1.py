k = int(input("enter num: "))
num = int(input("Enter a value to create a list: "))
list1 = []
for i in range(num):
    n = int(input("enter number in each index of list: "))
    list1.append(n)
print(list1)
for i in range(len(list1)):
    for j in range(1, len(list1)):
        if list1[i] + list1[j] == k:
            print("true")
        else:
            print("false")