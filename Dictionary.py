# 20CE098, Pranay Patel

# a. Write a Python script to check whether a given key already exists in a dictionary.

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}  # dictionary
print(dic)
key = int(input("Enter the key : "))
# Here user enters the key he/she wants to check, whether it exists in our dictionary
if key in dic:
      print("Key already exists in dictionary")
else:
      print("The given key doesn't exist in dictionary")
print()

# b. Write a Python script to merge two Python dictionaries.

city1 = {1: "Mumbai", 2: "Sydney", 3: "New York", 4: "Moscow"}  # 1st dictionary
city2 = {5: "London", 6: "Auckland", 7: "Paris"}  # 2nd dictionary
print("city1 :- ", city1)
print("city2 :- ", city2)

city1.update(city2)  # elements of city2 are added at the end of city1
print("After merging the 2 dictionaries :- ", city1)
print()

# c. Write a Python program to sum all the items in a dictionary.

dictionary = {1: 10, 2: 3, 5: 7, 10: 17}
print(dictionary)
add = 0  # initialising add with 0
# dictionary.values returns value stored in dic and using for loop we are saving that value in i
for i in dictionary.values():
    add = add + i
print("Sum of all items in dictionary is : ", add)
print()

# d. Write a Python script to add a key to a dictionary.

numbers = {1: "one", 2: "two", 3: "three", 4: "four"}

print("Dictionary before adding a key : ", numbers)

numbers.update({5: "five"})  # update function is used to add a new key to an existing dictionary
print("Dictionary after adding a key : ", numbers)
print()

# e. Write a Python script to concatenate following dictionaries to create a new one.

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

new_dic = dic1.copy()  # a new dictionary named dic4 is created and values of dic1 are copied in new_dic
new_dic.update(dic2)  # elements of dic2 are added at the end of new_dic
new_dic.update(dic3)  # elements of dic3 are added at the end of new_dic
print("dic1 :- ", dic1)
print("dic2 :- ", dic2)
print("dic3 :- ", dic3)
print("New dictionary :- ", new_dic)
print()
