class TreeNode:
    def __init__(self,value):
        self.__value = value
        self.__left = None
        self.__right = None
    
    def left(self,node):
        self.__left = node
    
    def right(self,node):
        self.__right = node

    def getLeft(self):
        return self.__left
    
    def getRight(self):
        return self.__right
    
    def getValue(self):
        return self.__value

class Tree:
    def __init__(self):
        self.__root = None
    
    def addNode(self,value):
        if self.__root == None:
            self.__root = TreeNode(value)
        else:
            self.placeNode(self.__root,value)

    def addNodeObject(self,node):
        if self.__root == None:
            self.__root = node
        else:
            self.placeNodeObject(self.__root,node)

    def placeNodeObject(self,top,node):
        value = node.getvalue()
        if value<top.getValue():
            if top.getLeft() == None:
                top.left(TreeNode(value))
                return
            else:
                self.placeNode(top.getLeft(),node)
        elif value>top.getValue():
            if top.getRight() == None:
                top.right(TreeNode(value))
                return
            else:
                self.placeNode(top.getRight(),node)


    def placeNode(self,top,value):
        if value<top.getValue():
            if top.getLeft() == None:
                top.left(TreeNode(value))
                return
            else:
                self.placeNode(top.getLeft(),value)
        elif value>top.getValue():
            if top.getRight() == None:
                top.right(TreeNode(value))
                return
            else:
                self.placeNode(top.getRight(),value)
    def PreOrderPrintTree(self,root=None,first = True,array=[]):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            array.append(root.getValue())
            
            self.PreOrderPrintTree(root.getLeft(),False,array)
            
            self.PreOrderPrintTree(root.getRight(),False,array)    
        return array
    def InOrderPrintTree(self,root=None,first = True,array=[]):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            
            self.InOrderPrintTree(root.getLeft(),False,array)
            array.append(root.getValue())
            
            self.InOrderPrintTree(root.getRight(),False,array)  
        return array
    def PostOrderPrintTree(self,root=None,first = True,array=[]):
        
        if root == None and first:
            root = self.__root
        
        if root != None:
            
            self.PostOrderPrintTree(root.getLeft(),False,array)
            
            self.PostOrderPrintTree(root.getRight(),False,array)     
            array.append(root.getValue())  
              
        return array
    def getLevel(self,target,root="head",level=0):
        if root == "head":
            root = self.__root

        if root is None:
            return -1


        if root.getValue() == target:
            return level


        leftLevel = self.getLevel(target,root.getLeft(),  level + 1)
        if leftLevel != -1:
            return leftLevel

        return self.getLevel(target,root.getRight(),  level + 1)

    def printTree(self):
        root = self.__root
        if root is None:
            print("<empty tree>")
            return

        def recurse(node, prefix="", is_left=True):
            if node is None:
                return
            
            # Print node
            connector = "├── " if is_left else "└── "
            print(prefix + connector + str(node.getValue()))

            # Determine next prefixes
            new_prefix = prefix + ("│   " if is_left else "    ")

            left = node.getLeft()
            right = node.getRight()

            # Print children
            if left or right:
                if left:
                    recurse(left, new_prefix, True)
                else:
                    print(new_prefix + "├── <None>")

                if right:
                    recurse(right, new_prefix, False)
                else:
                    print(new_prefix + "└── <None>")

        # Root printed without connector
        print(str(root.getValue()))
        
        left = root.getLeft()
        right = root.getRight()

        if left:
            recurse(left, "", True)
        if right:
            recurse(right, "", False)

    def getNode(self,value,root = None,first = True):
        if root == None and first:
            root = self.__root
        
        if root != None:
            
            if root.getValue() == value:
                return root
            self.getNode(value,root.getLeft(),False)
            if root.getLeft().getValue() == value:
                return root.getLeft()
            self.getNode(value,root.getRight(),False)    
            if root.getRight().getValue() == value:
                return root.getRight()
    
    def depth(self,root = "None"):
        if root == "None":
            root = self.__root
        if root is None:
            return -1

        ldepth = self.depth(root.getLeft())
        rdepth = self.depth(root.getRight())

        return max(ldepth, rdepth) + 1

    def remove(self,value):
        self.__root, removed = self.__remove_node(self.__root, value)
        return removed

    def __remove_node(self, node, value):
        if node is None:
            return None, False

        if value < node.getValue():
            updated_left, removed = self.__remove_node(node.getLeft(), value)
            node.left(updated_left)
            return node, removed

        if value > node.getValue():
            updated_right, removed = self.__remove_node(node.getRight(), value)
            node.right(updated_right)
            return node, removed

        # Node found: 0 or 1 child
        if node.getLeft() is None:
            return node.getRight(), True
        if node.getRight() is None:
            return node.getLeft(), True

        # Node with 2 children: replace with inorder successor
        successor_parent = node
        successor = node.getRight()

        while successor.getLeft() is not None:
            successor_parent = successor
            successor = successor.getLeft()

        # Remove successor from its old location
        if successor_parent != node:
            successor_parent.left(successor.getRight())
            successor.right(node.getRight())

        successor.left(node.getLeft())
        return successor, True
