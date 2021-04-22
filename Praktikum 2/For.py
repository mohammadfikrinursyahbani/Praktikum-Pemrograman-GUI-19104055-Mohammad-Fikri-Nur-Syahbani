# This Code Made By Mohammad Fikri Nur Syahbani

#Menggunakan variabel
angka = 10

#Param 1 : Max
for i in range(angka) :
    print("Angka ke : ")
    print(i)

#Param 2 : Min, Max (sifat increment)
for i in range(angka, 20) :
    print("Angka ke :")
    print (i)

#Param 3 : Min, Max, Lompatan + (sifat increment)
#Param 3 : Max, Min, Lompatan - (sifat decrement)
for i in range(angka, 1, -1) :
    print("Angka ke : ")
    print(i)

array = [1,2,3,4]

for i in array :
    print (i, end = '')