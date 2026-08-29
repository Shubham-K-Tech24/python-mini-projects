#Banner section:

print("~*~*"*29, "\n")
print("Age Calculator tool".upper().center(120),"\n")
print("~*~*"*29)

#Welcome section:

print("welcome to age calculator ".capitalize())
print("~*~*"*29)
print("please fill your information below".title())
print("~*~*"*29)

#Input section:

print("----"*29)
name=input("Enter your name : ".ljust(10).title())
print("----"*29)
Current_year=input("Enter the current year going on ? : ".ljust(10).title()) 
print("----"*29)
Birth_year=input("Enter your birth year ? : ".ljust(10).title())
print("----"*29)

#Calculation section:

Current_year=int(Current_year)
Birth_year=int(Birth_year)
Current_age=  (Current_year)-(Birth_year)

#Output section:

print("~*~*"*29,"\n")
print("  "*2,f"{name.title()} as per to the given information , you were born in year {Birth_year} and currently in {Current_year} you are {Current_age} years old ","\n")
print("~*~*"*29,"\n")

#Apperication / thanking section:

print("Thankyou , Visit again".upper().center(120),"\n")
print("~*~*"*29,"\n")