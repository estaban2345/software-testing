from pro_set_2 import *

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
    assert stree.splay(5) == None
    assert stree.header.left == None
    assert stree.header.right == None

    #stree.splay(4)
    #assert stree.header.left == None
    #assert stree.header.right == None

	#assert stree.splay(5) == None

    #assert not stree.splay(4)
    #assert stree.root.left == None



    #return stree.root.key
print (test())
