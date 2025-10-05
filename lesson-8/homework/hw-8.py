##----------------------------------------
##----------------------------------------
#Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.
try:
    # Foydalanuvchidan son kiritishni so‘raymiz
    son = int(input("Biror son kiriting: "))
    natija = son / 0  # Nolga bo‘linmoqda
    print("Natija:", natija)
except ZeroDivisionError:
    print("Xatolik: Nolga bo‘lish mumkin emas!")


#Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
try:
    # Foydalanuvchidan butun son kiritishni so‘raymiz
    user_input = input("Iltimos, butun son kiriting: ")
    
    # Kiritilgan qiymatni butun songa o‘tkazamiz
    number = int(user_input)
    
    # Agar xato bo‘lmasa, kiritilgan sonni chiqaramiz
    print("Siz kiritgan son:", number)

except ValueError:
    # Agar butun son kiritilmasa, xato haqida xabar beramiz
    print("Xatolik: Siz butun son kiritmadingiz!")




#Write a Python program that opens a file and handles a FileNotFoundError exception if the file does not exist.

import os

try:
    # Fayl mavjudligini tekshiramiz, agar mavjud bo'lmasa, uni yaratamiz
    if not os.path.exists(file_name):
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write("")  # Bo'sh fayl yaratamiz

    # Faylni ochamiz
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl mazmuni:\n", content)
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
finally:
    print("Dastur tugadi.")






#Write a Python program that prompts the user to input two numbers and raises a TypeError exception if the inputs are not numerical.

try:
    # Foydalanuvchidan ikkita son kiritishni so‘raymiz
    num1 = input("Birinchi sonni kiriting: ")
    num2 = input("Ikkinchi sonni kiriting: ")
    
    # Kiritilgan qiymatlarni float turiga o‘tkazamiz
    number1 = float(num1)
    number2 = float(num2)
    
    # Agar xato bo‘lmasa, kiritilgan sonlarni chiqaramiz
    print("Siz kiritgan sonlar:", number1, "va", number2)

except ValueError:
    # Agar kiritilgan qiymatlar son bo‘lmasa, xato haqida xabar beramiz
    print("Xatolik: Iltimos, raqamli qiymat kiriting!")
finally:
    print("Dastur tugadi.")




#Write a Python program that opens a file and handles a PermissionError exception if there is a permission issue.

try:
    # Foydalanuvchidan fayl nomini kiritishni so‘raymiz
    file_name = input("Iltimos, ochmoqchi bo‘lgan fayl nomini kiriting: ")
    
    # Faylni ochamiz
    with open(file_name, 'r') as file:
        content = file.read()
        print("Fayl mazmuni:\n", content)
except PermissionError:
    # Agar faylga ruxsat berilmasa, xato haqida xabar beramiz
    print("Xatolik: Faylga ruxsat berilmagan!")
finally:
    print("Dastur tugadi.")





#Write a Python program that executes an operation on a list and handles an IndexError exception if the index is out of range.

try:
    # Ro'yxat yaratamiz
    my_list = [10, 20, 30, 40, 50]
    
    # Foydalanuvchidan indeks kiritishni so‘raymiz
    index = int(input("Ro'yxatdan element olish uchun indeksni kiriting (0-4): "))
    
    # Kiritilgan indeks bo‘yicha elementni olamiz
    element = my_list[index]
    print("Ro'yxatdagi element:", element)
except IndexError:
    # Agar indeks doiradan tashqarida bo'lsa, xato haqida xabar beramiz
    print("Xatolik: Indeks doiradan tashqarida!")
finally:
    print("Dastur tugadi.")




#Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

try:
    # Foydalanuvchidan son kiritishni so‘raymiz
    number = int(input("Iltimos, biror son kiriting: "))
    print("Siz kiritgan son:", number)
except KeyboardInterrupt:
    # Agar foydalanuvchi kiritishni bekor qilsa, xato haqida xabar beramiz
    print("\nXatolik: Kiritish bekor qilindi!")
finally:
    print("Dastur tugadi.")





#Write a Python program that executes division and handles an ArithmeticError exception if there is an arithmetic error.

try:
    # Foydalanuvchidan ikkita son kiritishni so‘raymiz
    numerator = float(input("Bo'luvchini kiriting: "))
    denominator = float(input("Bo'luvchini kiriting: "))
    
    # Bo'linishni amalga oshiramiz
    result = numerator / denominator
    print("Natija:", result)
except ArithmeticError:
    # Agar arifmetik xato bo'lsa, xato haqida xabar beramiz
    print("Xatolik: Arifmetik xato!")
finally:
    print("Dastur tugadi.") 





#Write a Python program that opens a file and handles a UnicodeDecodeError exception if there is an encoding issue.

try:
    # Foydalanuvchidan fayl nomini kiritishni so‘raymiz
    file_name = input("Iltimos, ochmoqchi bo‘lgan fayl nomini kiriting: ")
    
    # Faylni ochamiz
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl mazmuni:\n", content)
except UnicodeDecodeError:
    # Agar kodlash bilan bog'liq xato bo'lsa, xato haqida xabar beramiz
    print("Xatolik: Faylni o'qishda kodlash xatosi!")
finally:
    print("Dastur tugadi.")




#Write a Python program that executes a list operation and handles an AttributeError exception if the attribute does not exist.

try:
    # Ro'yxat yaratamiz
    my_list = [1, 2, 3, 4, 5]
    
    # Ro'yxatga yangi element qo'shamiz
    my_list.append(6)
    print("Ro'yxatga yangi element qo'shildi:", my_list)
    
    # Noto'g'ri atributga murojaat qilamiz
    my_list.non_existent_method()
except AttributeError:
    # Agar atribut mavjud bo'lmasa, xato haqida xabar beramiz
    print("Xatolik: Noto'g'ri atribut!")
finally:
    print("Dastur tugadi.")





#Write a Python program to read an entire text file.

try:
    # Foydalanuvchidan fayl nomini kiritishni so‘raymiz
    file_name = input("Iltimos, o'qimoqchi bo‘lgan fayl nomini kiriting: ")
    
    # Faylni ochamiz va uning mazmunini o‘qiymiz
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl mazmuni:\n", content)
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
except Exception as e:
    # Boshqa xatolarni ushlaymiz
    print("Xatolik:", e)
finally:
    print("Dastur tugadi.")





#Write a Python program to read first n lines of a file.

try:
    # Foydalanuvchidan fayl nomini va o'qiladigan qatorlar sonini kiritishni so‘raymiz
    file_name = input("Iltimos, o'qimoqchi bo‘lgan fayl nomini kiriting: ")
    n = int(input("Nechta qator o'qishni xohlaysiz? "))
    
    # Faylni ochamiz va uning birinchi n qatorini o‘qiymiz
    with open(file_name, 'r', encoding='utf-8') as file:
        for i in range(n):
            line = file.readline()
            if not line:
                break  # Agar fayl tugasa, chiqamiz
            print(line.strip())
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
except Exception as e:
    # Boshqa xatolarni ushlaymiz
    print("Xatolik:", e)
finally:
    print("Dastur tugadi.")





#Write a Python program to append text to a file and display the text.

try:
    # Foydalanuvchidan fayl nomini va qo'shiladigan matnni kiritishni so‘raymiz
    file_name = input("Iltimos, matn qo'shmoqchi bo‘lgan fayl nomini kiriting: ")
    text_to_append = input("Qo'shmoqchi bo‘lgan matnni kiriting: ")
    
    # Faylga matn qo'shamiz
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(text_to_append + '\n')
    
    # Faylni qayta ochib, uning mazmunini o‘qiymiz va chiqaramiz
    with open(file_name, 'r', encoding='utf-8') as file:
        content = file.read()
        print("Fayl yangilangan mazmuni:\n", content)
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
except Exception as e:
    # Boshqa xatolarni ushlaymiz
    print("Xatolik:", e)
finally:
    print("Dastur tugadi.")






  #Write a Python program to read last n lines of a file.

try:
    # Foydalanuvchidan fayl nomini va o'qiladigan qatorlar sonini kiritishni so‘raymiz
    file_name = input("Iltimos, o'qimoqchi bo‘lgan fayl nomini kiriting: ")
    n = int(input("Nechta oxirgi qatorni o'qishni xohlaysiz? "))
    
    # Faylni ochamiz va uning barcha qatorlarini o‘qiymiz
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
        # Oxirgi n qatorni chiqaramiz
        for line in lines[-n:]:
            print(line.strip())
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
except Exception as e:
    # Boshqa xatolarni ushlaymiz
    print("Xatolik:", e)
finally:
    print("Dastur tugadi.")






#Write a Python program to read a file line by line and store it into a list.

try:
    # Foydalanuvchidan fayl nomini kiritishni so‘raymiz
    file_name = input("Iltimos, o'qimoqchi bo‘lgan fayl nomini kiriting: ")
    
    # Faylni ochamiz va uning qatorlarini ro'yxatga saqlaymiz
    with open(file_name, 'r', encoding='utf-8') as file:
        lines_list = file.readlines()
        
    # Ro'yxatni chiqaramiz
    print("Fayldagi qatorlar ro'yxati:")
    for line in lines_list:
        print(line.strip())
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
except Exception as e:
    # Boshqa xatolarni ushlaymiz
    print("Xatolik:", e)
finally:
    print("Dastur tugadi.")





#Write a Python program to read a file line by line and store it into a variable.

try:
    # Foydalanuvchidan fayl nomini kiritishni so‘raymiz
    file_name = input("Iltimos, o'qimoqchi bo‘lgan fayl nomini kiriting: ")
    
    # Faylni ochamiz va uning qatorlarini bitta o'zgaruvchiga saqlaymiz
    with open(file_name, 'r', encoding='utf-8') as file:
        lines_variable = file.read()
        
    # O'zgaruvchini chiqaramiz
    print("Fayldagi barcha qatorlar:")
    print(lines_variable)
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
except Exception as e:
    # Boshqa xatolarni ushlaymiz
    print("Xatolik:", e)
finally:
    print("Dastur tugadi.")





#Write a Python program to read a file line by line and store it into an array.

try:
    # Foydalanuvchidan fayl nomini kiritishni so‘raymiz
    file_name = input("Iltimos, o'qimoqchi bo‘lgan fayl nomini kiriting: ")
    
    # Faylni ochamiz va uning qatorlarini massivga saqlaymiz
    with open(file_name, 'r', encoding='utf-8') as file:
        lines_array = file.readlines()
        
    # Massivni chiqaramiz
    print("Fayldagi qatorlar massivi:")
    for line in lines_array:
        print(line.strip())
except FileNotFoundError:
    # Agar fayl topilmasa, xato haqida xabar beramiz
    print("Xatolik: Fayl topilmadi!")
except Exception as e:
    # Boshqa xatolarni ushlaymiz
    print("Xatolik:", e)
finally:
    print("Dastur tugadi.")





#Write a Python program to find the longest words.

def find_longest_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
            max_length = max(len(word) for word in words)
            longest_words = [word for word in words if len(word) == max_length]
            return longest_words
    except FileNotFoundError:
        # Agar fayl topilmasa, xato haqida xabar beramiz
        print("Xatolik: Fayl topilmadi!")
    except Exception as e:
        # Boshqa xatolarni ushlaymiz
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

find_longest_words("example.txt")




#Write a Python program to count the number of lines in a text file.

def count_lines_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            return len(lines)
    except FileNotFoundError:
        # Agar fayl topilmasa, xato haqida xabar beramiz
        print("Xatolik: Fayl topilmadi!")
    except Exception as e:
        # Boshqa xatolarni ushlaymiz
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

count_lines_in_file("example.txt")



#Write a Python program to count the frequency of words in a file.

def word_frequency(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            words = file.read().split()
            frequency = {}
            for word in words:
                word = word.lower()  # Kichik harflarga o'tkazamiz
                if word in frequency:
                    frequency[word] += 1
                else:
                    frequency[word] = 1
            return frequency
    except FileNotFoundError:
        # Agar fayl topilmasa, xato haqida xabar beramiz
        print("Xatolik: Fayl topilmadi!")
    except Exception as e:
        # Boshqa xatolarni ushlaymiz
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

word_frequency("example.txt")





#Write a Python program to get the file size of a plain file.

import os

def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        # Agar fayl topilmasa, xato haqida xabar beramiz
        print("Xatolik: Fayl topilmadi!")
    except Exception as e:
        # Boshqa xatolarni ushlaymiz
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

file_size = get_file_size("example.txt")
if file_size is not None:
    print("Fayl hajmi:", file_size, "bayt")




#Write a Python program to write a list to a file.

def write_list_to_file(file_path, data_list):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(f"{item}\n")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

write_list_to_file("output.txt", ["Hello, world!", "Python is great!", "File handling is fun!"])





#Write a Python program to copy the contents of a file to another file.

import shutil

def copy_file_contents(source_file, destination_file):
    try:
        shutil.copyfile(source_file, destination_file)
        print("Fayl muvaffaqiyatli nusxalandi.")
    except FileNotFoundError:
        print("Xatolik: Manba fayl topilmadi!")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

copy_file_contents("example.txt", "copy_of_example.txt")






#Write a Python program to combine each line from the first file with the corresponding line in the second file.

def combine_files(file1, file2, output_file):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2, open(output_file, 'w', encoding='utf-8') as out:
            for line1, line2 in zip(f1, f2):
                out.write(f"{line1.strip()} {line2.strip()}\n")
        print("Fayllar muvaffaqiyatli birlashtirildi.")
    except FileNotFoundError as e:
        print(f"Xatolik: {e}")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

combine_files("file1.txt", "file2.txt", "combined_output.txt")






#Write a Python program to read a random line from a file.

import random

def read_random_line(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            if lines:
                return random.choice(lines).strip()
            else:
                print("Fayl bo'sh.")
    except FileNotFoundError:
        print("Xatolik: Fayl topilmadi!")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

random_line = read_random_line("example.txt")
if random_line:
    print("Tasodifiy qator:", random_line)





#Write a Python program to assess if a file is closed or not.

def is_file_closed(file_path):
    try:
        file = open(file_path, 'r', encoding='utf-8')
        print("Fayl ochiq:", not file.closed)
    except Exception as e:
        print("Xatolik:", e)
    finally:
        if 'file' in locals():
            file.close()
            print("Fayl yopildi.")
        print("Dastur tugadi.")

is_file_closed("example.txt")





#Write a Python program to remove newline characters from a file.

def remove_newline_characters(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            content = content.replace("\n", "")
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

remove_newline_characters("example.txt")





#Write a Python program that takes a text file as input and returns the number of words in a given text file.

def count_words_in_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

word_count = count_words_in_file("example.txt")
if word_count is not None:
    print("So'zlar soni:", word_count)





#Write a Python program to extract characters from various text files and put them into a list.

def extract_characters_to_list(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            characters_list = list(content)
            return characters_list
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

characters = extract_characters_to_list("example.txt")
if characters is not None:
    print("Belgilangan belgilar ro'yxati:", characters)
find_longest_words("example.txt")




#Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.

import string
import os

def generate_text_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(f"Bu {letter} fayli.")
    print("Fayllar yaratildi.")

generate_text_files()



#Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.

import string

def create_alphabet_file(file_path, letters_per_line):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for i in range(0, 26, letters_per_line):
                line = string.ascii_uppercase[i:i + letters_per_line]
                file.write(line + "\n")
    except Exception as e:
        print("Xatolik:", e)
    finally:
        print("Dastur tugadi.")

create_alphabet_file("alphabet.txt", 5)
