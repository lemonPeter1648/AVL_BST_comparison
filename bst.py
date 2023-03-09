printing_space = 8

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def search(self,root, key) -> bool:
        """returns information if value is in tree"""
        if key == root.key:
            return True
        elif key < root.key:
            if root.left:
                return self.search(root.left, key)
            else:
                return False
        elif key > root.key:
            if root.right:
                return self.search(root.right, key)
            else:
                return False

    @staticmethod
    def printTree(root, space):
        if (root == None) :
            return
        space += printing_space
        Node.printTree(root.right, space)
        print()
        for i in range(printing_space, space):
            print(end = " ")
        print(root.key)
        Node.printTree(root.left, space)

def inorder(root):
    """prints sorted elements of tree"""
    if root is not None:
        inorder(root.left)
        print(str(root.key) + "->", end=' ')
        inorder(root.right)

def insert(node, key):
    """puts an element in proper position, in tree"""
    if node is None:
        return Node(key)
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def minValueNode(node) -> int:
    """returns minimal value in given node(needed during deleting)"""
    current = node
    while(current.left is not None):
        current = current.left
    return current

def deleteNode(root, key):
    """removes given value from tree"""
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root



if __name__ == "__main__":
    elements_list = [8, 3, 1, 6, 7, 10, 14, 4, 12, 9]
    root = None
    for element in elements_list:
        root = insert(root, element)
    print(f"10 in tree: {root.search(root, 10)}")
    print(f"51 in tree: {root.search(root, 51)}")
    print("Tree: ")
    Node.printTree(root, 0)
    print("\nDelete 10")
    root = deleteNode(root, 10)
    print(f"10 in tree: {root.search(root, 10)}")
    print("Tree: ")
    Node.printTree(root, 0)