#Banner Section:

print("~*"*59,"\n")
print("welcome to login interface".upper().center(120),"\n")
print("~*"*59)
print("Please enter your information according to the given instructions:".title())
print("~*"*59)
print("--"*59)

#Input section:

name_Frist=str(input("Enter your First name : ".ljust(30)))
print("--"*59)
name_Mid=str(input("Enter your Middle name : ".ljust(30)))
print("--"*59)
name_last=str(input("Enter your Last name : ".ljust(30)))
print("--"*59)
contact=(input("Enter your Contact number : ".ljust(30)))

#Number validation:

if (contact.isdigit and len(contact)==10):
     pass
   
    
else:
     print("Contact number feeded is invlid".upper())

print("--"*59)
email=input("Enter your E-mail address : ".ljust(30))

#E-mail validation:

if (email.count("@")==1 and email.endswith(".com") and not email.startswith("@")):
     pass
else:
     print("E-mail address feeded is invlid".upper())

print("--"*59)
password=input("Set your password that should contain atleast 8 characters including upper&lower cases : ".ljust(30))
#Password validation:

if (len(password)>=8 and password != password.lower() and password != password.upper()):
       pass
else:
     print("Please enter password according to insturctions".upper())
print("--"*59,"\n")
print("  "*20,"Please Check your information and enter the password".upper(),"\n")
print("--"*59,"\n")
print("your full name is :".title().ljust(20),f"{name_Frist} {name_Mid} {name_last}".title())
print("your contact number is :".title().ljust(20),f"{contact}")
print("your e-mail address is :".title().ljust(20),f"{email.lower}")
confirm=input("Enter yuor password : ".ljust(20))

#Password coniformation:

if (confirm==password):
     print("--"*59)
     print("  "*20,"Congraulations you have Successfully Logined".center(120).title())
     print("--"*59)
else:
     print("sorry,your login is failed".upper().center(150))