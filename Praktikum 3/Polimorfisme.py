## This Code Made By Mohammad Fikri Nur Syahbani

from abc import ABCMeta,abstractmethod

# kelas abstract

class DuaDimensi(metaclass=ABCMeta):
    @abstractmethod
    def luas(self):
        pass

# kelas segi empat turunan dari kelas DuaDimensi

class SegiEmpat(DuaDimensi):
    def __init__(self, p, l):
        self.panjang = p
        self.lebar = l

    # implementasi metode luas()

    def luas(self):
        return self.panjang * self.lebar

# kelas segitiga turunan dari kelas DuaDimensi

class Segitiga(DuaDimensi):
    def __init__(self, a, t):
        self.alas = a
        self.tinggi = t

    # implementasi metode luas()

    def luas(self):
        return (self.alas * self.tinggi) / 2

# kelas lingkaran turunan dari kelas DuaDimensi

class Lingkaran(DuaDimensi):
    def __init__(self, r):
        self.jari2 = r
    
    # implementasi metode luas()

    def luas(self):
        import math
        return math.pi * (self.jari2 ** 2)

# memmbuat list kosong

mylist = []

# add object ke dalam mylist

mylist.append(SegiEmpat(8,6))
mylist.append(Segitiga(2,5))
mylist.append(Lingkaran(7))

for obj in mylist:  

	if not issubclass(obj.__class__, DuaDimensi):  

		raise TypeError('objek harus turunan dari DuaDimensi') 

	if isinstance(obj,SegiEmpat):  

		print('Luas Segi empat = ', end='')  

	elif isinstance(obj, Segitiga):  

		print('Luas Segitiga = ', end='')  

	else:  

		print('Luas Lingkaran = ', end='')  

	print(obj.luas()) 
