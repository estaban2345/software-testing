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
    node2 = Node(4)
    assert stree.root.key == node2.key
    assert result == None

    result = stree.insert(5)
    print(   ) #== Node(4)

    #stree.splay(4)
    #assert stree.header.left == None
    #assert stree.header.right == None

	#assert stree.splay(5) == None

    #assert not stree.splay(4)
    #assert stree.root.left == None



    #return stree.root.key
print (test())
