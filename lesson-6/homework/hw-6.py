##--------
##--------


#1. Modify String with Underscores
#Given a string txt, insert an underscore (_) after every third character. If a character is a vowel or already has an underscore after it, shift the underscore placement to the next character. No underscore should be added at the end.

#Examples
#Input: hello Output: hel_lo

#Input: assalom Output: ass_alom

#Input: abcabcabcdeabcdefabcdefg Output: abc_abcab_cdeab_cdef_abcd_efg

def insert_underscore(txt):
    vowels = "aeiouAEIOU"
    result = []
    i = 0
    count = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1
        # Underscore qo'yish sharti
        if count == 3 and i != len(txt) - 1:
            # Agar hozirgi yoki keyingi harf unli yoki keyingi harf '_' bo'lsa, keyinga suriladi
            shift = 0
            while (i + 1 + shift < len(txt)) and (txt[i + 1 + shift] in vowels or (i + 1 + shift < len(txt) and txt[i + 1 + shift] == '_')):
                shift += 1
            if i + 1 + shift < len(txt):
                result.append('_')
            count = 0
            i += shift
        i += 1
    return ''.join(result)

# Test
print(insert_underscore("hello"))         # hel_lo
print(insert_underscore("assalom"))       # ass_alom
print(insert_underscore("abcabcabcdeabcdefabcdefg")) # abc_abcab_cdeab_cdef_abcd_efg




#2. Integer Squares Exercise
#Task
#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i where 0 <= i < n, print i^2.

#Example Input
#5
#Example Output
#0
#1
#4
#9
#16
#Input Format
#The first and only line contains the integer, n.

#Constraints
#1 <= n <= 20
#Output Format
#Print n lines, one corresponding to each i^2 where 0 <= i < n.


# 2. Integer Squares Exercise

n = int(input())
for i in range(n):
    print(i ** 2)


#3. Loop-Based Exercises
#Exercise 1: Print first 10 natural numbers using a while loop
#Exercise 2: Print the following pattern
#1
#1 2
#1 2 3
#1 2 3 4
#1 2 3 4 5
#Exercise 3: Calculate sum of all numbers from 1 to a given number
#Example:

#Enter number 10
#Sum is: 55


# Exercise 1: Print first 10 natural numbers using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print the following pattern
for row in range(1, 6):
    for num in range(1, row + 1):
        print(num, end=" ")
    print()

# Exercise 3: Calculate sum of all numbers from 1 to a given number
n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)




#Exercise 4: Print multiplication table of a given number

# Exercise 4: Print multiplication table of a given number

num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num * i)



#Exercise 5: Display numbers from a list using a loop
#Given:

#numbers = [12, 75, 150, 180, 145, 525, 50]
#Expected Output:

#75
#150
#145


numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i > 50 and i <= 150 and i % 5 == 0:
        print(i)




#Exercise 6: Count the total number of digits in a number
#Example:

#75869
#Output: 5

user_number = int(input("Enter a number: "))

# Sonni matnga aylantirib, uzunligini olamiz
count = len(str(user_number))

print("Total digits:", count)





#Exercise 7: Print reverse number pattern
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1



n = 5  

for row in range(n, 0, -1):  
    for num in range(row, 0, -1):   
        print(num, end=" ")
    print()   






#Exercise 8: Print list in reverse order using a loop
#Given:

#list1 = [10, 20, 30, 40, 50]


list1 = [10, 20, 30, 40, 50]

for i in range(len(list1) - 1, -1, -1):
    print(list1[i])





#Exercise 9: Display numbers from -10 to -1 using a for loop


for i in range(-10, 0):
    print(i)




#Exercise 10: Display message “Done” after successful loop execution
#Example:

#0
#1
#2
#3
#4
#Done!

for i in range(5):
    print(i)
print("Done!")




#Exercise 11: Print all prime numbers within a range
#Example:

#Prime numbers between 25 and 50:
#29
#31
#37
#41
#43
#47


start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")


for num in range(start, end + 1):
    if num > 1: 
        is_prime = True
        for i in range(2, num):  
            if num % i == 0: 
                is_prime = False
                break
        if is_prime:
            print(num)



#Exercise 12: Display Fibonacci series up to 10 terms
#Example:

#Fibonacci sequence:
#0  1  1  2  3  5  8  13  21  34


n = 10  
a, b = 0, 1

print("Fibonacci sequence:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b





#Exercise 13: Find the factorial of a given number
#Example:

#5! = 120


num = int(input("Son kiriting: "))
factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"{num}! = {factorial}")





#4. Return Uncommon Elements of Lists
#Task
#Return the elements that are not common between two lists. The order of elements does not matter.

#Examples
#Input: list1 = [1, 1, 2], list2 = [2, 3, 4]
#Output: [1, 1, 3, 4]

#Input: list1 = [1, 2, 3], list2 = [4, 5, 6]
#Output: [1, 2, 3, 4, 5, 6]

#Input: list1 = [1, 1, 2, 3, 4, 2], list2 = [1, 3, 4, 5]
#Output: [2, 2, 5]



def uncommon_elements(list1, list2):
    result = []

    # list1 ichidan list2 da yo'q elementlarni olish
    for i in list1:
        if i not in list2:
            result.append(i)

    # list2 ichidan list1 da yo'q elementlarni olish
    for j in list2:
        if j not in list1:
            result.append(j)

    return result


# Test qilamiz
print(uncommon_elements([1, 1, 2], [2, 3, 4]))       # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))       # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  # [2, 2, 5]
