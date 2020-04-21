class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent

    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt

    def delete(self, data):
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                if parent.left is Node:
                    parent.left = None
                elif parent.right is Node:
                    parent.right = None
                del node
            elif children_count == 1:
                if node.left:
                    n = node.left
                elif node.right:
                    n = node.right
                if parent.left is node:
                    parent.left = n
                elif parent.right is node:
                    parent.right = n
                del node
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                node.data = successor.data
                if parent.left == successor:
                    parent.left = successor.right
                elif parent.right == successor:
                    parent.right = successor.right

    def compare_trees(self, node):
        if node is None:
            return False
        if self.data != node.data:
            return False
        res = True
        if self.left is None:
            if node.left:
                return False
        else:
            res = self.left.compare_trees(node.left)

        if self.right is None:
            if node.right:
                return False
        else:
            res = self.right.compare_trees(node.right)
        return res

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.data
        if self.left:
            self.right.print_tree()

    def preorder(self):
        if self is not None:
            print self.data,
            preorder(self.left)
            preorder(self.right)

    def inorder(self):
        if self is not None:
            inorder(self.left)
            print self.data,
            inorder(self.right)

    def postorder(self):
        if self is not None:
            postorder(self.left)
            postorder(self.right)
            print self.data,

    def levelorder(self, more=None):
        if self is not None:
            if more is None:
                more = []
            more += [self.left, self.right]
            print self.data,
        if more:
            levelorder(more[0], more[1:])
