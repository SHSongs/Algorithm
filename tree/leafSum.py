from tree import Node

root = Node(10)

root.left = Node(2)
root.right = Node(4)
root.left.left = Node(6)
root.left.right = Node(1)

hasTargetSum = False


def dfs(node, v, target):
    global hasTargetSum

    if hasTargetSum is True:
        return

    if node:
        # print(node.data)
        dfs(node.left, v + node.data, target)
        dfs(node.right, v + node.data, target)
    else:
        if target == v:
            hasTargetSum = True


def hasPathSum(target):
    global hasTargetSum
    hasTargetSum = False
    dfs(root, 0, target)
    return hasTargetSum


print(hasPathSum(12) is False)
print(hasPathSum(13) is True)
print(hasPathSum(18) is True)
print(hasPathSum(14) is True)
print(hasPathSum(1) is False)
print(hasPathSum(2) is False)
