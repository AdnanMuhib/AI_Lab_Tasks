
class Node:
    def __init__(self, val):
        self.val = val
        self.left_child = None
        self.right_child = None
    
    def get(self):
        return self.val
    
    def set(self, val):
        self.val = val
        
    def get_children(self):
        children = []
        if(self.left_child != None):
            children.append(self.left_child)
        if(self.right_child != None):
            children.append(self.right_child)
        return children
        
class BST:
    def __init__(self):
        self.root = None

    def set_root(self, val):
        self.root = Node(val)

    def insert(self, val):
        if(self.root is None):
            self.set_root(val)
        else:
            self.insert_node(self.root, val)

    def insert_node(self, current_node, val):
        if(val <= current_node.val):
            if(current_node.left_child):
                self.insert_node(current_node.left_child, val)
            else:
                current_node.left_child = Node(val)
        elif(val > current_node.val):
            if(current_node.right_child):
                self.insert_node(current_node.right_child, val)
            else:
                current_node.right_child = Node(val)

    def find(self, val):
        return self.find_node(self.root, val)

    def find_node(self, current_node, val):
        if(current_node is None):
            return False
        elif(val == current_node.val):
            return True
        elif(val < current_node.val):
            return self.find_node(current_node.left_child, val)
        else:
        	return self.find_node(current_node.right_child, val)

def main():
	
if __name__ == '__main__':
	main()