## This Code Made By Mohammad Fikri Nur Syahbani

class PersegiPanjang :

    #variabel biasa

    counter = 0

    #constructor

    def __init__(self, p, l) :
        #object variabel / instance

        self.panjang = p
        self.lebar = l

#Encapsulation
    #Setter

    def ubahPanjang(self, p) :
        self.panjang = p

    def ubahLebar(self,l) :
        self.lebar = l
#-- End Encapsulation

    def hitungLuas(self) :
        return self.panjang * self.lebar

    def hitungKeliling(self) :
        return 2 * (self.panjang + self.lebar)

    def cetakLuas(self) :
        print(f'Luas Persegi Panjang\t\t: {self.hitungLuas()}')

    def cetakKeliling(self) :
        print(f'Keliling Persegi Panjang\t: {self.hitungKeliling()}')

objekPP1 = PersegiPanjang(8, 8)

objekPP2 = PersegiPanjang(9, 9)

objekPP3 = PersegiPanjang(7, 7)

objekPP1.cetakLuas()

objekPP1.cetakKeliling()

objekPP1.counter = 10