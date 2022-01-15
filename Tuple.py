# 20CE098, Pranay Patel

# a. Write a Python program to create a tuple with different data types.

t1 = ("football", True, 7.77, 3)  # a tuple with different data types
print("Tuple with different data types : ", t1)
print()

# b. Write a Python program to create a tuple with numbers and print one item.

indices = (1,40,23,67,77,58,99,91,15,30)
print(indices)
print("item at 7th index : ", indices[7])
print("item at 2nd index : ", indices[2])
print("item at 5th index : ", indices[5])
print()

# c. Write a Python program to add an item in a tuple.

series = ("Friends", "The Big Bang Theory", "Game Of Thrones")
print("Before : ", series)
#tuples are immutable, so you can not add new elements
#using merge of tuples with the + operator you can add an element and it will create a new tuple
series = series + ("The Vampire Diaries",)
print("After : ", series)
print()

# d. Write a Python program to convert a tuple to a string.

intro = ("My", "name", "is", "Pranay")
print(intro, " ", type(intro))

string = ""
string = ' '.join(intro)  # The join() method takes all items in an iterable and joins them into one string
print(string, " ", type(string))
print()

# e. Write a Python program to find the length of a tuple.

tup = ("tuple", False, 3.2, 1, "Charusat", True, 17)
print(tup)
print("Length of tuple : ", len(tup))


