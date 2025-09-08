"""
This is converter
"""

#This converts celcius to fahrenheit
def convertCtoF():
    c = float(input("Ievadi C:"))
    F = (C * 9/5) + 32
    print(F)

#This converts kilometers to miles
def convertKilometerToMiles():
    kms = float(input("Ievadi ātttālumu:"))
    if kms > 0:
        miles = round(kms/1.6)
        print("Rezultāts ir:", miles)
    else:
        print("Vērtība nederīga")

#This converts euros to usd
def convertEuroToUsd():
    euro = input("Ievadi eiro:")
    if euro > 0:
        usd = euro*1.17
        print("Rezultāts ir:", usd)
    else:
        print("Vērtība nederīga")

#This converts square meters to hectares
def convertArea():
    square_m = int(input("Ievadi ātttālumu:"))
    ha = square_m / 10000
    print(square_m, "kvadrātmetri ir", ha, "kvadrātmetri")

convertArea()