class TreeNode:
    def __init__(self, newItem, left, right):
        self.item = newItem
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None

    def search(self, x) -> TreeNode:
        return __searchItem(self.__root, x)

    def __searchItem(self, tNode:TreeNode, x) -> TreeNode:
        if (tNode == None):
            return None
        elif (x == tNode.item):
            return tNode
        elif (x<tNode.item):
            return self.__searchItem(tNode.left, x)
        else:
            return self.__searchItem(tNode.right, x)

    def insert(self, newItem):
        self.__root = self.__insertItem(self.__root, newItem)

    def __insertItem(self, tNode:TreeNode, newItem) -> TreeNode:
        if(tNode == None):
            tNode = TreeNode(newItem, None, None)
        elif (newItem < tNode.item):
            tNode.left = self.__insertItem(tNode.left, newItem)
        else:
            tNode.right = self.__insertItem(tNode.right, newItem)
        return tNode

    def delete(self,x):
        self.__root = self.__deleteItem(self.__root, x)
    
    def __deleteItem(self, tNode:TreeNode, x) -> TreeNode:
        if(tNode == None):
            return None
        