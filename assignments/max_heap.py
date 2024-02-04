max_heap = []

def heapify(arr, n, i):
    if i == 0:
        return  # Root element has no parent

    parent = (i - 1) // 2
    if arr[i] > arr[parent]:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify(arr, n, parent)

def insert_max_heap(heap, value):
    global n 
    if value in heap:
        print("value already exists")
        return
    heap.append(value)
    n = len(heap)
    heapify(heap, n, n-1)

def delete_max_heap(heap):
    global n
    heap[0], heap[n-1] = heap[n-1], heap[0]
    heap.pop()
    n = len(heap)
    heapify(heap, n, 0)


while True: 
    print("1. Insert")
    print("2. Delete")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        value = int(input("Enter value to insert: "))
        insert_max_heap(max_heap, value)
    elif choice == 2:
        delete_max_heap(max_heap)
    elif choice == 3:
        print(max_heap)
    else:
        break


min_heap = []

def min_heapify(arr, n, i):
    if i == 0:
        return  

    parent = (i - 1) // 2
    if arr[i] < arr[parent]:
        arr[i], arr[parent] = arr[parent], arr[i]
        heapify(arr, n, parent)

def insert_min_heap(heap, value):
    global n 
    if value in heap:
        print("value already exists")
        return
    heap.append(value)
    n = len(heap)
    min_heapify(heap, n, n-1)

for i in max_heap:
    insert_min_heap(min_heap, i)

print("max heap: ")
print(max_heap)
print("min heap: ")
print(min_heap)

dif = 0
same = 0

for i in range(len(max_heap)):
    if (max_heap[i] != min_heap[i]):
        print("elem different at index {}".format(i))
        dif += 1
    else: 
        same += 1

print("different elements: ", dif)
print("same elements: ", same)