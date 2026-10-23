class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def height(n):
    return n.height if n else 0


def balance(n):
    return height(n.left) - height(n.right) if n else 0


def right_rotate(y):
    x = y.left
    t = x.right
    x.right = y
    y.left = t
    y.height = 1 + max(height(y.left), height(y.right))
    x.height = 1 + max(height(x.left), height(x.right))
    return x


def left_rotate(x):
    y = x.right
    t = y.left
    y.left = x
    x.right = t
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))
    return y


def insert(root, key):
    if root is None:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root

    root.height = 1 + max(height(root.left), height(root.right))
    bf = balance(root)

    if bf > 1 and key < root.left.key:  # LL
        return right_rotate(root)
    if bf < -1 and key > root.right.key:  # RR
        return left_rotate(root)
    if bf > 1 and key > root.left.key:  # LR
        root.left = left_rotate(root.left)
        return right_rotate(root)
    if bf < -1 and key < root.right.key:  # RL
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)


root = None
keys = list(map(int, input("Enter keys: ").split()))

for key in keys:
    root = insert(root, key)

print("Preorder:")
preorder(root)
print("\nInorder:")
inorder(root)
print("\nRoot:", root.key if root else None)
print("Height:", height(root))
