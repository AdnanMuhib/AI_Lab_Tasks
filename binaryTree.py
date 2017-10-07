class Node:
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.data = val

def binary_insert(root, node):
    if root is None:
        root = node
    else:
        if root.data > node.data:
            if root.l_child is None:
                root.l_child = node
            else:
                binary_insert(root.l_child, node)
        else:
            if root.r_child is None:
                root.r_child = node
            else:
                binary_insert(root.r_child, node)

def in_order_print(root):
    if not root:
        return
    in_order_print(root.l_child)
    print root.data
    in_order_print(root.r_child)

def pre_order_print(root):
    if not root:
        return        
    print root.data
    pre_order_print(root.l_child)
    pre_order_print(root.r_child)
    
def find_node (root, node_to_find, path, level):
    if (root == None):
        return False, path
    if (root.data == node_to_find):
        print("True", str(path), level)
        return True, path,level
    path.append(root.data)
    level += 1
    if(node_to_find > root.data):
        find_node(root.r_child, node_to_find, path, level)
    if(node_to_find <  root.data):
        find_node(root.l_child, node_to_find, path, level)
    #path.append(root.data)

def main():
    arr = [3, 5, 7, 2, 1, 8, 6, 11]
    root = Node(arr[0])
    for i in range(1,len(arr)):
        binary_insert(root,Node(arr[i]))
        pass
    node = input("Enter A node to find: ")
    path = []
    level = 0
    a  = find_node(root, node, path, level)
    print(a)
    # if( output[0] == True):
    #     print("True" , output[1])
    # else:
    #     print("not found")
    # print "in order:"
    # in_order_print(root)
    # print "pre order"
    # pre_order_print(root)


if __name__ == '__main__':
    main()