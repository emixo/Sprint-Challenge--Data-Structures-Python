import time

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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
            return node

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

    def in_order_print(self, node):
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

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
first_name = BSTNode(names_1[0])
for i in names_1:
    if i != names_1[0]:
        first_name.insert(i)

for i in names_2:
    if first_name.contains(i):
        duplicates.append(i)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
