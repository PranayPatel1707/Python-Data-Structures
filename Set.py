# 20CE098, Pranay Patel

# a. Write a Python program to add member(s) in a set and clear a set

a = {1.0, "Hello", (1, 2, 3)}
print("Before adding element :- ", a)
a.add(500)  # add function is used to add an element
print("After adding element :- ", a)
a.clear()  # clear method removes all elements from set
print("After clearing set :- ", a)
print()

# b. Write a Python program to remove an item from a set if it is present in the set.

s = {1, 3, 5, 7, 9, 11, 13, 15}
print("Initial set : ", s)
item = int(input("Enter item to be removed : "))

# discard method removes the given item from set if present and if not present it does nothing
s.discard(item)
print("After removing item : ", s)
# we can also use remove method for same
# difference bet remove and discard is that if element is not present remove gives error while discard does nothing
print()

# c. Write a Python program to create an intersection, Union, difference of sets.

n1 = {1, 3, 5, 7, 9, 11, 20, 30, 40, 50}
n2 = {2, 4, 6, 8, 10, 20, 30, 40, 50}

print("Set 1 : ", n1)
print("Set 2 : ", n2)

print("Intersection of sets : ", n1.intersection(n2))
print("Union of sets : ", n1.union(n2))
print("Difference of sets : ", n1.difference(n2))
print()

# d. Write a Python program to find maximum and the minimum value in a set.

num = {7, 2, 15, 20, 1, 50}
print("Set : ", num)
print("Maximum value in given set : ", max(num))  # returns element with maximum value
print("Minimum value in given set : ", min(num))  # returns element with minimum value
print()

# e. Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
l = ["Kolkata", "Melbourne", "Toronto", "Cape Town", "Kolkata", "Kolkata"]  # list
t = ("Kolkata", "Moscow", "London", "Stockholm", "Toronto", "Kolkata")  # tuple
d = {1: "Kolkata", 2: "Chicago", 3: "Madrid", 4: "Paris", 5: "Barcelona", 6: "Toronto", 7: "Toronto"}  # dictionary

print(l)
print(t)
print(d)

d_to_lst = list(d.values())
# converting list, tuple and dictionary(values) into set
# so that using intersection method of set we can find the common elements in l, t and d
s1 = set(l)
s2 = set(t)
s3 = set(d.values())

inter1 = s1.intersection(s2)
inter2 = inter1.intersection(s3)

lst = list(inter2)
c1 = []  # to count no. of occurrences in l
c2 = []  # to count no. of occurrences in t
c3 = []  # to count no. of occurrences in d
i = 0
while i < len(lst):
    c1.append(l.count(lst[i]))
    c2.append(t.count(lst[i]))
    c3.append(d_to_lst.count(lst[i]))
    i = i+1

print("Most common cities and their number of occurrences in list, tuple and dictionary are as follows")
print()
j = 0
print("         list  tuple  dict")
while j < len(lst):
    print(lst[j], "  ", c1[j], "   ", c2[j], "   ", c3[j])
    j = j+1
print()



