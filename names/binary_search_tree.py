"""
Binary search trees are a value structure that enforce an ordering over
the value they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of value in the tree.
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# don't allow duplicates
# order = []


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BSTNode(value)
        if self.value:
            if value >= self.value:
                if self.right is None:
                    self.right = node
                else:
                    self.right.insert(value)
            elif value < self.value:
                if self.left is None:
                    self.left = node
                else:
                    self.left.insert(value)
        else:
            self.value = value

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target > self.value:
            if self.right is None:
                return False
            return self.right.contains(target)
        elif target < self.value:
            if self.left is None:
                return False
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # base case:
        # check if left or right exist
        if node.left is None and node.right is None:
            print(node.value)
        elif node.left is None and node.right:
            print(node.value)
            self.in_order_print(node.right)
        elif node.left and node.right is None:
            self.in_order_print(node.left)
            print(node.value)
        elif node.left and node.right:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)
        while len(queue) > 0:

            node = queue.pop(0)
            print(node.value)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)



    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node:
            print(node.value)
            self.dft_print(node.left)    
            self.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):

        if node:
            print(node.value)
            self.dft_print(node.left)    
            self.dft_print(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node:
            self.dft_print(node.left)                
            self.dft_print(node.right)
            print(node.value) 