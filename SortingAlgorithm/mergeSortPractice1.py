'''
Custom Comparison Functions
Let's return to our original problem statement now.

QUESTION 1: You're working on a new feature on Jovian called "Top Notebooks of the Week". 
Write a function to sort a list of notebooks in decreasing order of likes. 
Keep in mind that up to millions of notebooks can be created every week, so your function needs to be as efficient as possible.
'''

class Notebook:
    def __init__(self, title, username, likes):
        self.title, self.username, self.likes = title, username, likes
        
    def __repr__(self):
        return 'Notebook <"{}/{}", {} likes>'.format(self.username, self.title, self.likes)

nb0 = Notebook('pytorch-basics', 'aakashns', 373)
nb1 = Notebook('linear-regression', 'siddhant', 532)
nb2 = Notebook('logistic-regression', 'vikas', 31)
nb3 = Notebook('feedforward-nn', 'sonaksh', 94)
nb4 = Notebook('cifar10-cnn', 'biraj', 2)
nb5 = Notebook('cifar10-resnet', 'tanya', 29)
nb6 = Notebook('anime-gans', 'hemanth', 80)
nb7 = Notebook('python-fundamentals', 'vishal', 136)
nb8 = Notebook('python-functions', 'aakashns', 74)
nb9 = Notebook('python-numpy', 'siddhant', 92)

notebooks = [nb0, nb1, nb2, nb3, nb4, nb5,nb6, nb7, nb8, nb9]

def compare_likes(a, b):
    if a.likes > b.likes:
        return 'lower'
    elif a.likes < b.likes:
        return 'greater'
    else:
        return 'equal'

def default_compare(a , b):
    if a < b:
        return 'lesser'
    elif a > b:
        return 'higher'
    else:
        return 'equal'

def merge_sort(obj , compare):
    if len(obj) < 2:
        return obj
    
    mid = len(obj) // 2
    return  merge(merge_sort(obj[:mid] , compare) , merge_sort(obj[mid:] , compare) , compare)

def merge(left , right , compare):
    i , j , merged = 0 , 0 , []

    while i < len(left) and j < len(right):
        result = compare(left[i] , right[j])
        if result == 'lower' or result == 'equal':
            merged.append(left[i])
            i += 1
        elif result == 'greater':
            merged.append(right[j])
            j += 1
    return merged + left[i:] + right[j:]

sorted_notebooks = merge_sort(notebooks, compare_likes)
print(sorted_notebooks)            
          
    