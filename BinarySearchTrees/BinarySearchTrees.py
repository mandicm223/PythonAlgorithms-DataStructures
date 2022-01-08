from jovian.pythondsa import evaluate_test_case, evaluate_test_cases

'''
QUESTION: As a senior backend engineer at Jovian,
you are tasked with developing a fast in-memory data structure to manage profile information (username, name and email) for 100 million users.
It should allow the following operations to be performed efficiently:

1. Insert the profile information for a new user.
2. Find the profile information of a user, given their username
3. Update the profile information of a user, given their usrname
4. List all the users of the platform, sorted by username

You can assume that usernames are unique.
'''

'''
Input
The key inputs to our data structure are user profiles, which contain the username, name and email of a user.

A Python class would be a great way to represent the information for a user. 
A class is a blueprint for creating objects. Everything in Python is an object belonging to some class.

'''
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

'''


Here's what's happening above (conceptually):


Python creates an empty object of the type user and stores in the variable user2
Python then invokes the function User.___init__ with the arguments user2, "john", "John Doe" and "john@doe.com"
As the __init__ function is executed, the properties username, name and email are set on the object user2




Output
We can also express our desired data structure as a Python class UserDatabase with four methods: insert, find, update and list_all.


class UserDatabase:
    def insert(self, user):
        pass

    def find(self, username):
        pass

    def update(self, user):
        pass

    def list(self):
        pass
'''   

'''
2. Come up with some example inputs & outputs.
Let's create some sample user profiles that we can use to test our functions once we implement them.
'''

aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]


'''
1.Insert:
Inserting into an empty database of users
Trying to insert a user with a username that already exists
Inserting a user with a username that does not exist
Inserting User into full database

2.Find:
Finding user by the username
Trying to find user by username that does not exist
Trying to find user in empty databse

3.Update:
Updating user info given the username
Trying to update user info given the username that does not exist
Trying to update username to already existing username

4.List:
Listing all users in database
Trying to list all users but database is empty
'''

'''
3. Come up with a correct solution. State it in plain English.

Here's a simple and easy solution to the problem: we store the User objects in a list sorted by usernames.

The various functions can be implemented as follows:

1. Insert: Loop through the list and add the new user at a position that keeps the list sorted.
2. Find: Loop through the list and find the user object with the username matching the query.
3. Update: Loop through the list, find the user object matching the query and update the details
4. List: Return the list of user objects.
'''


'''
4. Implement the solution and test it using example inputs.

The code for implementing the above solution is also fairly straightfoward.


class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):
        i = 0
        while i < len(self.users):
            # Find the first username greater than the new user's username
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):
        return self.users


database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)

user1 = database.find('siddhant')
#print(user1)

database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))
user3 = database.find('siddhant')
#print(user3)

full_list = database.list_all
print(full_list)

'''

'''
5. Analyze the algorithm's complexity and identify inefficiencies

The operations insert, find, update involves iterating over a list of users,
in the worst case, they may take up to N iterations to return a result, where N is the total number of users.
list_all however, simply returns the existing internal list of users.

Thus, the time complexities of the various operations are:

Insert: O(N)
Find: O(N)
Update: O(N)
List: O(1)
Exercise: Verify that the space complexity of each operation is O(1).

Is this good enough?
To get a sense how long each function might take if there are 100 million users on the platform,
we can simply run an for or while loop on 10 million numbers.

'''

'''
6. Apply the right technique to overcome the inefficiency

We can limit the number of iterations required for common operations like find,
insert and update by organizing our data in the following structure, called a BINARY TREE:

It's called a tree because it vaguely like an inverted tree trunk with branches.

The word "binary" indicates that each "node" in the tree can have at most 2 children (left or right).
Nodes can have 0, 1 or 2 children. Nodes that do not have any children are sometimes also called "leaves".
The single node at the top is called the "root" node, and it typically where operations like search, insertion etc. begin.


For our use case, we require the binary tree to have some additional properties:

1. Keys and Values: Each node of the tree stores a key (a username) and a value (a User object).
A binary tree where nodes have both a key and a value is often referred to as a map or treemap (because it maps keys to values).

2. Binary Search Tree: The left subtree of any node only contains nodes with keys that are lexicographically smaller than the node's key,
and the right subtree of any node only contains nodes with keys that lexicographically larger than the node's key.
A tree that satisfies this property is called a binary search trees,
and it's easy to locate a specific key by traversing a single path down from the root note.

3. Balanced Tree: The tree is balanced i.e. it does not skew too heavily to one side or the other.
The left and right subtrees of any node shouldn't differ in height/depth by more than 1 level.

'''


'''
Height of a Binary Tree
The number of levels in a tree is called its height.
As you can tell from the picture above, each level of a tree contains twice as many nodes as the previous level.

For a tree of height k, here's a list of the number of nodes at each level:

Level 0: 1

Level 1: 2

Level 2: 4 i.e. 2^2

Level 3: 8 i.e. 2^3

...

Level k-1: 2^(k-1)

If the total number of nodes in the tree is N, then it follows that

N = 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1)
We can simplify this equation by adding 1 on each side:

N + 1 = 1 + 1 + 2^1 + 2^2 + 2^3 + ... + 2^(k-1) 

N + 1 = 2^1 + 2^1 + 2^2+ 2^3 + ... + 2^(k-1) 

N + 1 = = 2^2 + 2^2 + 2^3 + ... + 2^(k-1)

N + 1 = = 2^3 + 2^3 + ... + 2^(k-1)

...

N + 1 = 2^(k-1) + 2^(k-1)

N + 1 = 2^k

k = log(N + 1) <= log(N) + 1 
Thus, to store N records we require a balanced binary search tree (BST) of height no larger than log(N) + 1. 
This is a very useful property, in combination with the fact that nodes are arranged in a way that makes it easy to find a specific key
by following a single path down from the root.

As we'll see soon, the insert,
find and update operations in a balanced BST have time complexity O(log N)
since they all involve traversing a single path down from the root of the tree.
'''


'''
IMPLEMENTAION OF BINARY TREE


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

tree_tupple = ((1,3,None) , 2 , ((None, 3, 4) , 5 , (6,7,8))) 

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = parse_tuple(data[0])
            node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree = parse_tuple(tree_tupple)

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)

display_keys(tree, ' ')    



TRAVERSING OF BINARY TREE ===============================================================================================================


# Inorder traversal

def inorder(node):
    if node is None:
        return []
    return(inorder(node.left) + [node.key] + inorder(node.right))


# preorder traversal

def preorder(node):
    if node is None:
        return []
    return([node.key] + preorder(node.left) + preorder(node.right))


# postorder traversal

def postorder(node):
    if node is None:
        return []
    return(postorder(node.left) + postorder(node.right) + [node.key])


# height of a tree

def height_of_a_tree(node):
    if node is None:
        return 0
    return 1 + max(height_of_a_tree(node.right) , height_of_a_tree(node.left))


# size of a tree

def size_of_a_tree(node):
    if node is None:
        return 0
    return 1 + size_of_a_tree(node.right) + size_of_a_tree(node.left)

print(inorder(tree))
print(preorder(tree))
print(postorder(tree))
print(height_of_a_tree(tree))
print(size_of_a_tree(tree))
'''

'''
As a final step, let's compile all the functions we've written so far as methods withing the TreeNode class itself. 
Encapsulation of data and functionality within the same class is a good programming practice.
'''

class TreeNode:
    def __init__(self, key, left=None , right=None):
        self.key = key
        self.left = left
        self.right = right
    
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.right) , TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) , TreeNode.size(self.right)
    
    def inorder(self):
        if self is None:
            return []
        return (TreeNode.inorder(self.left) , [self.key] , TreeNode.inorder(self.right))

    def preored(self):
        if self is None:
            return []
        return ( [self.key] , TreeNode.preored(self.left) , TreeNode.preored(self.right))

    def postorder(self):
        if self is None:
            return []
        return (TreeNode.postorder(self.left) ,TreeNode.postorder(self.right) ,[self.key] )
    
    @staticmethod
    def parse_tuple(self , data):
        if data is None:
            node = None
        elif isinstance(data , tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = self.parse_tuple(data[0])
            node.right = self.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node
    
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left),  self.key, TreeNode.to_tuple(self.right)

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node is a leaf 
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        self.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        self.display_keys(self.left,space, level+1)

