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

convertKilometerToMiles()