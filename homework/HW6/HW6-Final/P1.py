class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left, self.right = None, None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val})' + \
               '\n|\n|-(L)->' + '\n|      '.join(str(self.left ).split('\n')) + \
               '\n|\n|-(R)->' + '\n|      '.join(str(self.right).split('\n'))


class BSTTable:
    def __init__(self):
        self._root = None

    def __str__(self):
        return str(self._root)

    def __len__(self):
        return self._size(self._root)

    def put(self, key, val):
        self._root = self._put(self._root, key, val)

    def get(self, key):
        return self._get(self._root, key)

    def _put(self, node, key, val):
        if not node: 
            return BSTNode(key, val)
        if   key < node.key:
            node.left  = self._put(node.left,  key, val)
        elif key > node.key:
            node.right = self._put(node.right, key, val)
        else:
            node.val = val
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _get(self, node, key):
        if not node:
            raise KeyError(f'key not found: {key}')
        if key < node.key:
            return self._get(node.left,  key)
        elif key > node.key:
            return self._get(node.right, key)
        else:
            return node.val

    @staticmethod
    def _size(node):
        return node.size if node else 0
    
    def _removemin(self, node):
        if node.left == None:
            return node.right  # want to switch with the right if there is no left
        
        node.left = self._removemin(node.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node
    
    def remove(self, key):
        self._root = self._remove(self._root, key)

    def _remove(self, node, key):
        # TODO: Should return a subtree whose root is <node> but without
        #       the node whose key is <key>
        if not node:
            raise KeyError(f"There is no node with key: {key}")
        
        if key < node.key:
            node.left = self._remove(node.left,  key)
    
        elif key > node.key:
            node.right = self._remove(node.right, key)
        elif key == node.key: 
            if node.left == None and node.right == None: 
                return None 
            elif node.left != None and node.right != None: # two kids
            # find the minimum on that bigger or right side
                node_temp = self._min(node.right) # saving the min node
                node.right = self._removemin(node.right)
                node.key = node_temp.key
                node.val = node_temp.val
                
            elif node.left != None and node.right == None: # one child on left
                node = node.left
            elif node.left == None and node.right != None:
                node = node.right

                
        # update size 
        node.size = 1 + self._size(node.left) + self._size(node.right)   
        return node 
    
    def _min(self, node):
        if node.left != None:
            node.left = self._min(self, node.left)
        return node
         
               
        
from enum import Enum

class DFSTraversalTypes(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class DFSTraversal():
    def __init__(self, tree: BSTTable, traversalType: DFSTraversalTypes):
        # TODO: implement
        self.tree = tree
        self.traversalType = traversalType
        self.nodelist = [] # inorder to store the nodes
        
        # different cases for the different traversal types
        if self.traversalType == DFSTraversalTypes.PREORDER:
            self.preorder(tree)
        if self.traversalType == DFSTraversalTypes.INORDER:
            self.inorder(tree)
        if self.traversalType == DFSTraversalTypes.POSTORDER:
            self.postorder(tree)

    def __iter__(self):
        return self

    def __next__(self):
        # checking the list & giving each value in the list 
        if len(self.nodelist) == 0: 
            raise StopIteration
            
        # return the top item
        return self.nodelist.pop(0)
        

    def inorder(self, bst: BSTTable):
        def _traversal(bst: BSTNode): # need to look at individual nodes
            if bst == None: # go until the end
                return #return nothing 
            #order: left, visit current, go right
            _traversal(bst.left) # go left
            self.nodelist.append(bst) # visit current node
            _traversal(bst.right) # go right
                
        if len(bst) > 0: 
            _traversal(bst._root) # this is to start from the root

    def preorder(self, bst: BSTTable):
        def _traversal(bst: BSTNode): 
            if bst == None: 
                return 
            #order: visit current, left, right
            self.nodelist.append(bst) 
            _traversal(bst.left)
            _traversal(bst.right)
                
        if len(bst) > 0: 
            _traversal(bst._root) 
    
    
    def postorder(self, bst: BSTTable):
        def _traversal(bst: BSTNode): 
            if bst == None: 
                return 
            #order, left, right, visit current
            _traversal(bst.left) 
            _traversal(bst.right)
            self.nodelist.append(bst) 
                
        if len(bst) > 0: 
            _traversal(bst._root)


if __name__ == "__main__":
    tree = BSTTable()
    tree.put(0, 'd')
    tree.put(2, 'c')
    tree.put(5, 'a')
    tree.put(1, 'b')


    print("Problem 1A Min Remove function:----------------------- \n")
    print(tree._root, "\n")
    print("Tree after minremoval:----------------- \n")
    print(tree._removemin(tree._root), "\n")


    print("Problem 1B Remove function:----------------------- \n")
    print(tree, "\n")
    print("Tree after Removal of key 1:----------------- \n")
    tree.remove(1)
    print(tree, "\n")
    #tree.remove(10)
    print("With remove 10, we get an attribute error because the key does not exist \n")
    
    print("Problem 1c Traverse:----------------------- \n")
    input_array = [(4, 'a'), (9, 'c'), (2, 'f'), (3, 'z'), (11, 'i'), (8, 'r')]
    bst = BSTTable()
    for key, val in input_array:
        bst.put(key, val)
    
    traversal = DFSTraversal(bst, DFSTraversalTypes.INORDER)
    print("Inorder:")
    for node in traversal:
        print(str(node.key) + ', ' + node.val)
    print("\n")
        
    traversal = DFSTraversal(bst, DFSTraversalTypes.PREORDER)
    print("Preorder:")
    for node in traversal:
        print(str(node.key) + ', ' + node.val)
    print("\n")
        
    traversal = DFSTraversal(bst, DFSTraversalTypes.POSTORDER)
    print("Postorder:")
    for node in traversal:
        print(str(node.key) + ', ' + node.val)
    print("\n")

