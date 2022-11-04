import random
import sys
import time

def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
# kecepatan mengetik
        time.sleep(random.random() * 0.1)


def turn(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
# kecepatan mengetik
        time.sleep(random.random() * 1)


def loading(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
# kecepatan mengetik
        time.sleep(random.random() * 1.7)
        
turn('PROGRAM TURN ON....')
mengetik('MEMUAT DATA.....')
loading('........')        
mengetik('-----SELAMAT DATANG DI PROGRAM PENGUBAH SUHU-----\n\n*************************\n* program by: @fasuyaaa *\n*************************\n')

user = input('Masukkan nama: ')

mengetik("\nSelamat datang "+user+". Silahkan pilih satuan suhu yang ingin diubah\n")

ulangi = "yes"

while ulangi == "yes" or ulangi == "y":
    mengetik("----------SATUAN SUHU----------\n\n1. Celsius")
    mengetik("2. Fahrenheit")
    mengetik("3. Reaumur")
    mengetik("4. Kelvin\n\n-------------------------------")
    masuk = int(input("Pilih Satuan (1/2/3/4): "))

    if masuk == 1:
        mengetik("-----Celsius-----\n\n1. Celsius ke Fahrenheit")
        mengetik("2. Celsius ke Reamur")
        mengetik("3. Celsius ke Kelvin\n\n-------------------------------")
        pilih = int (input("Pilih metode (1/2/3): "))
        
        if pilih == 1:
            celsius = float(input("Masukkan derajat Celsius: "))
            fahrenheit = (celsius * 1.8) + 32
            print(celsius," derajat Celsius sama dengan ",fahrenheit," derajat Fahrenheit\n-------------------------------")
            
        elif pilih == 2:
            celsius = float(input("Masukkan derajat Celsius: "))
            reamur = (celsius * 4/5) 
            print(celsius," derajat Celsius sama dengan ",reamur," derajat Reamur\n-------------------------------")

        elif pilih == 3:
            celsius = float(input("Masukkan derajat Celsius: "))
            kelvin = (celsius + 273)
            print(celsius," derajat Celsius sama dengan ",kelvin," derajat Kelvin\n-------------------------------")

        else:
            print("\n##############################\n# Masukkan input yang benar! #\n##############################\n")
            ulangi = "yes"

    elif masuk == 2:
        mengetik("-----Fahrenheit-----\n\n1. Fahrenheit ke Celsius")
        mengetik("2. Fahrenheit ke Reamur")
        mengetik("3. Fahrenheit ke Kelvin\n\n-------------------------------")
        pilih = int (input("Pilih metode (1/2/3): "))
        
        if pilih == 1:
            fahrenheit = float(input("Masukkan derajat Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(fahrenheit," derajat Fahrenheit sama dengan ",celsius," derajat Celsius\n-------------------------------")
            
        elif pilih == 2:
            fahrenheit = float(input("Masukkan derajat Fahrenheit: "))
            reamur = (fahrenheit - 32) * 4/9
            print(fahrenheit," derajat Fahrenheit sama dengan ",reamur," derajat Reamur\n-------------------------------")

        elif pilih == 3:
            fahrenheit = float(input("Masukkan derajat Fahrenheit: "))
            kelvin = (fahrenheit - 32) * 5/9 + 273
            print(fahrenheit," derajat Fahrenheit sama dengan ",kelvin," derajat Kelvin\n-------------------------------")

        else:
            print("\n##############################\n# Masukkan input yang benar! #\n##############################\n")
            ulangi = "yes"

    elif masuk == 3:
        mengetik("-----Reamur-----\n\n1. Reamur ke Celsius")
        mengetik("2. Reamur ke Fahrenheit")
        mengetik("3. Reamur ke Kelvin\n\n-------------------------------")
        pilih = int (input("Pilih metode (1/2/3): "))
        
        if pilih == 1:
            reamur = float(input("Masukkan derajat Reamur: "))
            celsius = (reamur * 5/4) 
            print(reamur," derajat Reamur sama dengan ",celsius," derajat Celsius\n-------------------------------")
            
        elif pilih == 2:
            reamur = float(input("Masukkan derajat Reamur: "))
            fahrenheit = (reamur * 9/4) + 32
            print(reamur," derajat Reamur sama dengan ",fahrenheit," derajat Fahrenheit\n-------------------------------")

        elif pilih == 3:
            reamur = float(input("Masukkan derajat Reamur: "))
            kelvin = (reamur * 5/4) + 273
            print(reamur," derajat Reamur sama dengan ",kelvin," derajat Kelvin\n-------------------------------")

        else:
            print("\n##############################\n# Masukkan input yang benar! #\n##############################\n")
            ulangi = "yes"

    elif masuk == 4:
        mengetik("-----Kelvin-----\n\n1. Kelvin ke Celsius")
        mengetik("2. Kelvin ke Fahrenheit")
        mengetik("3. Kelvin ke Reamur\n\n-------------------------------")
        pilih = int (input("Pilih metode (1/2/3): "))
        
        if pilih == 1:
            kelvin = float(input("Masukkan derajat Kelvin: "))
            celsius = (kelvin - 273) 
            print(kelvin," derajat Kelvin sama dengan ",celsius," derajat Celsius\n-------------------------------")
            
        elif pilih == 2:
            kelvin = float(input("Masukkan derajat Kelvin: "))
            fahrenheit = (kelvin - 273) * 9/5 + 32
            print(kelvin," derajat Kelvin sama dengan ",fahrenheit," derajat Fahrenheit\n-------------------------------")

        elif pilih == 3:
            kelvin = float(input("Masukkan derajat Kelvin: "))
            reamur = (kelvin - 273) * 4/5
            print(kelvin," derajat Kelvin sama dengan ",reamur," derajat Reamur\n-------------------------------")

        else:
            print("\n##############################\n# Masukkan input yang benar! #\n##############################\n")
            ulangi = "yes"

    else:
            print("\n##############################\n# Masukkan input yang benar! #\n##############################\n")
            ulangi = "yes"

    ulangi = input("Ulangi? y/n: ")
    ulangi.lower()