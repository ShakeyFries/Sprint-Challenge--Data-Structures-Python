import time


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# first run time
# runtime: 12.615012168884277 seconds

# importing binary search tree as I remember being told it was a faster way to search.

# implement bst somehow?
import sys
sys.path.append('src/bst.py')
from bst import BSTNode


bst = BSTNode(names_1[0])

# insert names_into binary search tree
for name in names_1:
    bst.insert(name)

# now try to filter out duplicates?
for name in names_2:
    if bst.contains(name):
        duplicates.append(name)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# Improved run time!
# runtime: 0.23639607429504395 seconds

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  There are are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
