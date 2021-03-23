class BinarySearchTree:
    """
    BinarySearchTree is a class that provides easy implementation of binary search tree through the dictionary.
    """
    tree = {}


    def __init__(self, root):
        self.tree['root'] = root
        self.tree[root] = {'left': None, 'right': None, 'root': None}

    def addNode(self, x):
        """
        Function addNode adds node into the binary search tree dictionary
        :rtype: None
        """
        if len(self.tree) == 0:
            self.tree['root'] = x
            self.tree[x] = {'left': None, 'right': None, 'root': None}
            return
        node = self.tree['root']
        while node:
            root = node
            if node == x:
                return
            elif node > x:
                side = 'left'
                node = self.tree[node]['left']
            else:
                side = 'right'
                node = self.tree[node]['right']
        self.tree[root][side] = x
        self.tree[x] = {'left': None, 'right': None, 'root': root}
        return

    def nodeExistence(self, x):
        """
        Function nodeExistense checks existence of node in BinarySearchTree object.
        :returns: boolean: True when node exists, False when node doesn't exist.
        """
        if len(self.tree) == 0:
            return False
        node = self.tree['root']
        while node:
            root = node
            if node == x:
                return True
            elif node > x:
                node = self.tree[node]['left']
            else:
                node = self.tree[node]['right']
        return False

    def inOrder(self, node='root'):
        """
        Function inOrder prints tree traversals in Inorder format.
        :param node: node of tree
        """
        if node == 'root':
            self.inOrder(self.tree[node])
        elif node != None:
            self.inOrder(self.tree[node]['right'])
            print(node)
            self.inOrder(self.tree[node]['right'])

    def toDictionary(self):
        """
        Function toDictionary returns the tree dictionary.
        :return: dictionary object
        """
        return self.tree

    def hasLeftChild(self, node):
        """
        Function hasLeftChild checks whether the node has left child.
        :param node: tree node
        :return: boolean
        """
        if self.tree[node]['left'] is not None:
            return True
        return False

    def hasRightChild(self, node):
        """
        Function hasRightChild checks whether the node has right child.
        :param node: tree node
        :return: boolean
        """
        if self.tree[node]['right'] is not None:
            return True
        return False

    def isLeftChild(self, node):
        """
        Function isLeftChild checks whether the node is left child of its parent.
        :param node: tree node
        :return: boolean
        """
        if self.tree[self.tree[node]['root']]['left'] == node:
            return True
        return False

    def isRightChild(self, node):
        """
        Function isRightChild checks whether the node is left child of its parent.
        :param node: tree node
        :return: boolean
        """
        if self.tree[self.tree[node]['root']]['right'] == node:
            return True
        return False

    def isRoot(self, node):
        """
        Function isRoot checks whether the node is root of the tree.
        :param node: tree node
        :return: boolean
        """
        if self.tree[node]['root'] == None:
            return True
        return False

    def isLeaf(self, node):
        """
        Function isLeaf checks whether the node is leaf of the tree.
        :param node: tree node
        :return: boolean
        """
        if self.tree[node]["left"] == None and self.tree[node]['right'] == None and self.tree[node]['root'] != None:
            return True
        return False

    def hasAnyChildren(self, node):
        """
        Function hasAnyChildren checks whether the node has at least one child.
        :param node: tree node
        :return: boolean
        """
        if self.tree[node]['left'] != None or self.tree[node]['right'] != None:
            return True
        return False

    def hasBothChildren(self, node):
        """
        Function hasBothChildren checks whether the node has both children.
        :param node: tree node
        :return: boolean
        """
        if self.tree[node]['left'] != None and self.tree[node]['right'] != None:
            return True
        return False

    def removeNode(self, value, parent=tree['root']):
        """
        Function removeNode removes one of the nodes in the tree.
        :param value: tree node value
        :return: boolean
        """
        left_v = self.tree[parent]['left']
        right_v = self.tree[parent]['right']
        if value < parent:
            if left_v is not None:
                self.removeNode(value, parent=left_v)
        elif value > parent:
            if right_v is not None:
                self.removeNode(value, parent=right_v)
        else:
            if left_v is not None and right_v is not None:
                next_val_node = min(left_v, right_v)
                next_el = self.tree[next_val_node]['']




if __name__ == "__main__":
    from pprint import pprint

    tree = BinarySearchTree(5)
    tree.addNode(3)
    tree.addNode(8)
    tree.addNode(3)
    tree.addNode(4)
    pprint(tree.toDictionary())
    print('6 in tree', tree.nodeExistence(6))
    print('8 in tree', tree.nodeExistence(8))
    tree.inOrder()
