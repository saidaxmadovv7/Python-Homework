##-------------------------------
##-------------------------------





#Create and Access List Elements
a=['Cherry','Melon','Grapes','Banana','Apple']



last=a.pop(3)
print(last)
print(a)


#Concatenate Two Lists
a=[1,2,3,4]
b =[5,6,7,8]
num3=a+b
print(num3)

#Extract Elements from a List
#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [1, 2, 3, 4, 5]
extracted = [numbers[0], numbers[len(numbers) // 2], numbers[-1]]
print(extracted)



#Convert List to Tuple
movie=['Inception', 'Interstellar', 'The Dark Knight']
movie_tuple= type(tuple(movie))
print(movie_tuple)



#Check Element in a List
#Given a list of cities, check if "Paris" is in the list and print the result.
cities=['New York', 'Los Angeles', 'Chicago', 'Paris', 'Jiddah']
print(cities)
print("Paris" in cities)


#Duplicate a List Without Using Loops
duplicated_numbers = numbers * 2
print(duplicated_numbers)

#Swap First and Last Elements of a List
#Given a list of numbers, swap the first and last elements.
numbers = [1, 2, 3, 4, 5]
numbers[0], numbers[-1] = numbers[-1], numbers[0]
print(numbers)



#Slice a Tuple
numbers = tuple(range(1, 11))
print(numbers[3:7])



#Count Occurrences in a List
colors = ['red', 'blue', 'green', 'blue', 'yellow', 'blue']
blue_count = colors.count('blue')
print(blue_count)

# Find the Index of an Element in a Tuple
animals = ('cat', 'dog', 'lion', 'tiger')
lion_index = animals.index('lion')
print(lion_index)



 #Merge Two Tuples
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
merged_tuple = tuple1 + tuple2
print(merged_tuple)



#Find the Length of a List and Tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
print(len(my_list))
print(len(my_tuple))



#Convert Tuple to List
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(my_list)





#Find Maximum and Minimum in a Tuple

numbers = (1, 2, 3, 4, 5)
print(max(numbers))
print(min(numbers))




#Reverse a Tuple
words = ('apple', 'banana', 'pinapple')
reversed_words = words[::-1]
print(reversed_words)
