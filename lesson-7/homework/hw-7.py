##------------
##------------
#Problems
#1. is_prime(n) funksiyasi

#is_prime(n) funksiyasini hosil qiling (n > 0). Agar n soni tub bo'lsa True, aks holda False qiymat qaytarsin.

is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Misollar
print(is_prime(4))  # False
print(is_prime(7))  # True

#2. digit_sum(k) funksiyasi

#digit_sum(k) funksiyasini yozing, u k sonining raqamlari yig'indisini hisoblaydi.

digit_sum = lambda k: sum(int(x) for x in str(abs(k)))

# Misollar
print(digit_sum(123))   # 6
print(digit_sum(345))  # 15




#3. Ikki sonning darajalari

#Berilgan N sonidan oshmaydigan barcha 2 ning darajalarini (ya'ni, 2**k shaklidagi sonlarni) chop etuvchi funksiyani yozing.


def powers_of_two(N):
    k = 1
    while 2**k <= N:
        print(2**k, end=" ")
        k += 1

#Misol
powers_of_two(10)   # 2 4 8
