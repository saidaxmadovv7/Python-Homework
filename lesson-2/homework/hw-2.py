

##1. Age Calculator
##Write a Python program to ask for a user's name and year of birth, then calculate and display their age.

#foydalanuvchidan ism va yoshini so'rash
ism = input("Ismingizni kiriting:")
yil = int(input("Tug'ilgan yilingizni kiriting:"))

#hozirgi yilni olish uchun datatime kutubxonasidan foydalanamiz
import datetime
hozirgi_yil = datetime.datetime.now().year

# yoshni hisoblaymiz
yosh = hozirgi_yil - yil

# natijani chiqaramiz
print(f"Salom, {ism}! Siz {yosh} yoshdasiz.")



##2. Extract Car Names
##Extract car names from the following text:

txt = 'LMaasleitbtui'
txt = txt[1::2]
print(txt)


##3. Extract Car Names
##Extract car names from the following text:

txt = 'MsaatmiazD'
txt = txt[1::2]
print(txt)


##4. Extract Residence Area
##Extract the residence area from the following text:

txt = "I'am John. I am from London"
txt = txt[txt.index("from")+5:]
print(txt)


##5. Reverse String
##Write a Python program that takes a user input string and prints it in reverse order.

matn = input("Matn kiriting:")
teskari_matn = matn[::-1]
print(teskari_matn)

##6. Count Vowels
##Write a Python program that counts the number of vowels in a given string.

matn = input("Matn kiriting:")
unli_harf = "aeiouAEIOU"
sanoq = 0
for harf in matn:
    if harf in unli_harf:
        sanoq += 1
print(f"Matnda {sanoq} ta unli harf bor.")


##7. Find Maximum Value
##Write a Python program that takes a list of numbers as input and prints the maximum value.

raqamlar = [input("Raqam kiriting::")]
raqamlar1 = raqamlar.max
print(raqamlar1)


##8. Check Palindrome
##Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).

# Palliandromni tekshiruvchi dastur
matn = input("Soz yokida raqam kiriting: ") #anna

# Matnni teskari tartibda olamiz

teskari = matn[::-1]

# Solishtirish
if matn == teskari:
    print("Bu so'z Palliandrom!")
else:
    print("Bu so'z Palliandrom emas!")


##9. Extract Email Domain
##Write a Python program that extracts and prints the domain from an email address provided by the user.
email = input("Email manzilingizni kiriting: ")
domen = email.split('@')[-1]
print(f"Sizning domeningiz: {domen}")

##10. Generate Random Password
##Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string
def generate_password(length):
    if length < 6:
        return "Parol uzunligi kamida 6 ta bo'lishi kerak."
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
length = int(input("Parol uzunligini kiriting (kamida 6 ta): "))
print("Yaratilgan parool:", generate_password(length))
