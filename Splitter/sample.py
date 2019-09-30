list1 = []
list2 = []
m = int(input("Enter size"))
for i in range(0,m):
    element = int(input("Enter element"))
    list1.append(element)
list2.append(list1[0]+list1[1])
for i in range(1,m-1):
    list2.append(list1[i-1]+list1[i+1])
list2.append(list1[m-2]+list1[m-1])
print(list2)