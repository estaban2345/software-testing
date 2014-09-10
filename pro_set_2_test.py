from pro_set_2 import *

# Write test code in this function to achieve
# full statement coverage on the SplayTree class.

def test():
    nodo = Node(3)
    assert nodo.key == 3
    assert nodo.left == None
    assert nodo.right == None
	
    assert nodo.equals(nodo)

    stree = SplayTree()
    
    assert stree.isEmpty()
    assert stree.root == None
    assert stree.header.key == None
    
    #assert stree.splay(4) == None
    result = stree.insert(5)
    assert result == None
    assert stree.root.key == 5
    assert stree.header.left == None
    assert stree.header.right == None
    
    result = stree.insert(4)
    assert stree.root != None
    nodo1 = Node(5)
    assert stree.root.right.key == nodo1.key
    assert stree.root.right != None
    assert type(stree.root.right) == type(nodo)
    node2 = Node(4)
    assert stree.root.key == node2.key
    assert result == None
    
    print( "root",stree.root.left, stree.root.key, stree.root.right.key )
    
    result = stree.insert(5)
    print("header",stree.header.left, stree.header.key, stree.header.right.key)
    result = stree.insert(5)
    assert result == None
    assert type(stree.header.right) == type(nodo)
    assert stree.header.right.key == 4
    
    #print( stree.root.key  )
    print("header",stree.header.left, stree.header.key, stree.header.right.key)
    result = stree.insert(6)
    assert stree.root.right == None
    assert type(stree.root.left) == type(nodo)
    assert stree.root.left.key == 5
    assert type(stree.header.right) == type(nodo)
    assert stree.header.right.key == 4
    
    #print(  stree.root.key,stree.root.right, stree.root.left.key )
    print("header",stree.header.left, stree.header.key, stree.header.right.key)
    result = stree.remove(5)
    assert stree.root.left == None
    assert type(stree.root.right) == type(nodo)
    assert stree.root.key == 4
    assert stree.root.right.key == 6
	
    print("header",stree.header.left, stree.header.key, stree.header.right)
	#print(  stree.root.left, stree.root,stree.root.right )

    result = stree.remove(4)

    #result = stree.remove(6)

    #print(  stree.root )


print (test() == None)
