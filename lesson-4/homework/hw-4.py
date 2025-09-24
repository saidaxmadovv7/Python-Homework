##----------------
##----------------
#Dictionary Exercises

#1. Sort a Dictionary by Value




my_dict = {"a": 3, "b": 1, "c": 4, "d": 2}
# Ascending (o‘sish tartibida)
asc = dict(sorted(my_dict.items(), key=lambda x: x[1]))

# Descending (kamayish tartibida)
desc = dict(sorted(my_dict.items(), key=lambda x: x[1], reverse=True))

asc
desc


#2. Add a Key to a Dictionary


#Sample Dictionary:
raqamlar = {0: 10, 1: 20}
# Yangi kalit va qiymat qo'shamiz
raqamlar[2] = 30

raqamlar


#3. Concatenate Multiple Dictionaries


#Sample Dictionaries:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

umumiy = {**dic1, **dic2, **dic3}
umumiy


#4. Generate a Dictionary with Squares


#Sample Dictionary (n = 5):
raqamlar = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
n = 5
raqamlar = {x: x*x for x in range(1, n+1)}
raqamlar


#5. Dictionary of Squares (1 to 15)


#Expected Output:
#raqamlar = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

raqamlar = {i: i*i for i in range(1, 16)}
print(raqamlar)





#Set Exercises

#1. Create a Set


my_set = {1, 2, 3, 4, 5}
print(my_set)


#2. Iterate Over a Set


my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)


#3. Add Member(s) to a Set


my_set = {1, 2, 3}
my_set.add(4)         # Bitta element qo'shish
my_set.update([5, 6]) # Bir nechta element qo'shish

print(my_set)


#4. Remove Item(s) from a Set


my_set = {1, 2, 3, 4, 5}
my_set.remove(3)      # 3 ni o'chiradi
my_set.discard(6)     # 6  bo'lmasa  ham xatolik chiqarmaydi
my_set.pop()          # Tasodifiy element o'chiriladi

print(my_set)


#5. Remove an Item if Present in the Set


my_set = {1, 2, 3, 4, 5}
item = 3

if item in my_set:
    my_set.remove(item)

print(my_set)
