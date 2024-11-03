#implementing binary tree class from scratch
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

#initialize and allocate memory for tree nodes
firstNode = Node(2)
secondNode = Node(3)
thirdNode = Node(4)
fourthNode = Node(5)

#Connect the nodes
firstNode.left = secondNode
firstNode.right = thirdNode
secondNode.left = fourthNode

#Depth first search DFS
#In-Order DFS: Left, Root, Right
def inOrderDFS(node):
    if node is None:
        return
    inOrderDFS(node.left)
    print(node.data, end=" ")
    inOrderDFS(node.right)

#Pre-Order DFS: Root, Left, Right
def preOrderDFS(node):
    if node is None:
        return
    print(node.data, end= " ")
    preOrderDFS(node.left)
    preOrderDFS(node.right)

#Post-Order DFS: Left, Right, Node
def postOrderDFS(node):
    if node is None:
        return
    postOrderDFS(node.left)
    postOrderDFS(node.right)
    print(node.data, end=" ")

#Breadth First Search
def bfs(root):
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.data, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


if __name__ == "__main__":
    print("In-order DFS: ", end='')
    inOrderDFS(firstNode)
    print("\nPre-order DFS: ", end='')
    preOrderDFS(firstNode)
    print("\nPost-order DFS: ", end='')
    postOrderDFS(firstNode)
    print("\nLevel order: ", end='')
    bfs(firstNode)
    print("")

