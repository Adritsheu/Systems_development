# Problem 2

class BSTNode:

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return f'BSTNode({self.key}, {self.val}, {self.size})' + \
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
    
    #private function: clients will not use this
    def _put(self, node, key, val):
        #node.key is where we are currently
        #first 
        if node == None:
            return BSTNode(key,val)  #creating the first instance of a node to compare
        else:
            if node.key < key:
                # RHS: node.right = current version
                #LHS: setting node.right to the new version which is coming out 
                #We are rewriting each time
            
                node.right = self._put(node.right,key,val)
                
            
            elif node.key > key:
                node.left = self._put(node.left,key,val)
                
            
            elif node.key == key:
                node.val = val
            node.size = 1 + self._size(node.left) + self._size(node.right)
        return node
        

    def _get(self, node, key):
        if node is not None:
            if node.key > key:
                return self._get(node.left, key)

            elif node.key < key:
                return self._get(node.right, key)

            elif node.key == key:
                return node.val
        elif node == None:
            raise KeyError("Node doesn't exist")

    @staticmethod
    def _size(node):
        return node.size if node else 0


#test case
greektoroman = BSTTable()
greektoroman.put('Athena',    'Minerva')
greektoroman.put('Eros',      'Cupid')
greektoroman.put('Aphrodite', 'Venus')
# greektoroman.put('Aphrodite', 'Adriana')
# greektoroman.put('Eros', 'Adriana')
print(greektoroman)
print(greektoroman.get('Eros'))