class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BTree:
    def __init__(self):
        self.root = Node(15)

    def newNode(self, key, node):
        if node.left == None:
            node.left = Node(key)
        elif node.right == None:
            node.right = Node(key)
        else:
            print("Unable to add new node")

    def preorder(self, root):
        if root != None:
            print(root.key, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

    def postorder(self, root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end=' ')

tree = BTree()
tree.newNode(1, tree.root)
tree.newNode(37, tree.root)
tree.newNode(61, tree.root.left)
tree.newNode(26, tree.root.left)
tree.newNode(59, tree.root.right)
tree.newNode(48, tree.root.right)
print("Preorder :", end=' ')
tree.preorder(tree.root)
print("\nInorder :", end=' ')
tree.inorder(tree.root)
print("\nPostorder :", end=' ')
tree.postorder(tree.root)
