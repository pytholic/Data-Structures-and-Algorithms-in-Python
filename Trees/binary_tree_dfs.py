class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, "")[:-1]  # passing empty string initially
        elif traversal_type == 'inorder':
            return self.inorder_print(tree.root, "")[:-1]
        elif traversal_type == 'post':
            return self.post_print(tree.root, "")[:-1]
        else:
            print("Traversal type '{}' is not supported.".format(str(traversal_type)))

    def preorder_print(self, start, traversal):
        """
        Helper method - use this to create a 
        recursive print solution.
        Root->Left->Right
        """
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
        
    def inorder_print(self, start, traversal):
        """
        Left->Root->Right
        """
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
        
    def post_print(self, start, traversal):
        """
        Left->Right->Root
        """
        if start:
            traversal = self.post_print(start.left, traversal)
            traversal = self.post_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def search(self, traversal_type, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
                
        if traversal_type == 'preorder':
            return self.preorder_search(self.root, find_val)
        elif traversal_type == 'inorder':
            return self.inorder_search(self.root, find_val)
        elif traversal_type == 'postorder':
            return self.postorder_search(self.root, find_val)
        else:
            print("Search type not supported!")


    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False
    
    def inorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start.left:
            return self.inorder_search(start.left, find_val)
        elif start:
            if start.value == find_val:
                return True
        else:
            return self.inorder_search(start.right, find_val)
        return False
    
    def postorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start.left:
            return self.inorder_search(start.left, find_val)
        elif start.right:
            return self.inorder_search(start.right, find_val)
        else:
            if start:
                if start.value == find_val:
                    return True
        return False
        
    def postorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if start:
            if start.value == find_val:
                return True
            else:
                return self.postorder_search(start.left, find_val) or self.postorder_search(start.right, find_val)
        return False
    
# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(find_val=4, traversal_type="postorder")
# Should be False
print tree.search(find_val=6, traversal_type="postorder")

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree('preorder')
# Should be 4-2-5-1-3
# print tree.print_tree('inorder')
# Should be 4-5-2-1-3
# print tree.print_tree('post')