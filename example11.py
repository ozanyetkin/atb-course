from time import perf_counter
from math import sqrt, gcd

t1_start = perf_counter()

"""
series = range(2, 50000)
asal_sayilar = []
for num in series:
    asal = True
    for n in range(2, num):
        if num % n == 0:
            asal = False
            break
    
    if asal == True:
        # print(f"{num} bir asal sayidir")
        asal_sayilar.append(num)
    else:
        # print(f"{num} bir asal sayi degildir")
        pass

print(asal_sayilar)
"""
a_number = 50000 ** 2 + 1

if a_number > 1:
    if gcd(2, a_number) > 1:
        print("bu sayi cifttir")
    else:
        prime_list = [3]
        asal = True
        for i in prime_list:
            if i > sqrt(a_number):
                break
            if gcd(a_number, i) > 1:
                asal = False
                break
            cift_list = [2]
            advoc = i + 2
            for c in cift_list:
                if c % 2 == 0:
                    asal_advoc = True
                    for j in prime_list:
                        if j > sqrt(advoc):
                            break
                        if gcd(j, advoc) > 1:
                            asal_advoc = False
                            break
                    if asal_advoc:
                        prime_list.append(advoc)
                        break
                    else:
                        advoc = advoc + 2
                    cift_list.append(c)
    if asal:
        print("bu sayi asaldir")
    else:
        print("bu sayi asal degildir")
else:
    print("bu sayi asal olamaz")

print(prime_list)

t1_stop = perf_counter()
print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)
