#This code made by Mohammad Fikri Nur Syahbani

#Try..except...
try :
    a = int(input('masukan nilai a : '))
    b = int(input('masukan nilai b : '))
    c = a/b
    print(f"{a} / {b} = {c}")

except ZeroDivisionError as e :
    print('Error : tidak boleh bagi 0')

#Try..except..finally...
f = ''

try : 
  f = open('contoh.txt', 'r')
  lines = f.readlines()
  for line in lines : 
    print(line, end='\n')

except IOError as e :
  print('Error : File Hilang')

finally :
  if f :
    f.close()