#Creating class for tree structure
class Node:
    #class constructore
    def __init__(self, data):
        self.data = data
        self.left = None        #Initially empty
        self.right = None       #Initially empty

#Defining each Nodes
root = Node(0)
A = Node(1)
B = Node(2)
C = Node(3)
D = Node(4)
E = Node(5)

#Making connections
root.left = A       #Assigns A to root as left child
root.right = B      #Assigns B to root as right chid
A.left = C          #Assigns C to A as left child
B.left = D          #Assigns D to B as left child
B.right = E         #Assigns E to B as right child