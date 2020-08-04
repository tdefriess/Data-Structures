"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):        
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        if target < self.value and self.left is not None:
            return self.left.contains(target)
        if target > self.value and self.right is not None:
            return self.right.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.left is not None:
            self.left.for_each(fn)

        # I placed callback function here to make this for_each function
        # conform to an In Order traversal
        fn(self.value)

        if self.right is not None:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        node.for_each(print)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        node_list = []
        node_list.append(node)

        while len(node_list) != 0:
            current_node = node_list.pop(0)
            print(current_node.value)
            if current_node.left is not None:
                node_list.append(current_node.left)
            if current_node.right is not None:
                node_list.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        node_list = []
        node_list.append(node)

        while len(node_list) != 0:
            current_node = node_list.pop(-1)
            print(current_node.value)
            if current_node.left is not None:
                node_list.append(current_node.left)
            if current_node.right is not None:
                node_list.append(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left is not None:
            self.pre_order_dft(node.left)
        if node.right is not None:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left is not None:
            self.post_order_dft(node.left)
        if node.right is not None:
            self.post_order_dft(node.right)
        print(node.value)
