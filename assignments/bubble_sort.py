a = []
i = int(input("enter the no of elements: "))
while i != 0:
    x = int(input("enter next element: "))
    a.append(x)
    i-=1

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] < a[j]:
            print("swapped step: " + str(a[i]) + " " + str(a[j]))
            a[i], a[j] = a[j], a[i]
        else:
            print("unswapped step: " + str(a[i]) + " " + str(a[j]))
    print(a)
            
