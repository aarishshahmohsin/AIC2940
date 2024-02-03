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

def delete_max_heap(heap, value):
    global n
    if value not in heap:
        print("value not present")
        return
    index = heap.index(value)
    heap[index], heap[n-1] = heap[n-1], heap[index]
    heap.pop()
    n = len(heap)
    heapify(heap, n, index)


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
        value = int(input("Enter value to delete: "))
        delete_max_heap(max_heap, value)
    elif choice == 3:
        print(max_heap)
    else:
        break


min_heap = []

def min_heapify(arr, n, i):
    if i == 0:
        return  # Root element has no parent

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

for i in range(len(max_heap)):
    if (max_heap[i] != min_heap[i]):
        print("elem different at index {}".format(i))