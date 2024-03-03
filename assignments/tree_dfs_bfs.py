class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def dfs(root):
    if root:
        print(root.val, end=' ')
        dfs(root.left)
        dfs(root.right)

def bfs(root):
    if root is None:
        return 
    
    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = None

while True:
    print("1. Insert, 2. DFS, 3. BFS, 4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        val = int(input("Enter value to insert: "))
        if root is None:
            root = Node(val)
        else:
            root = insert(root, val)
    elif choice == 2:
        dfs(root)
        print()  
    elif choice == 3:
        bfs(root)
        print() 
    elif choice == 4:
        break
    else:
        print("Invalid choice")
