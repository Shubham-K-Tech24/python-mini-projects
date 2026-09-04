#Banner section:

def design():
    print("~"*128,"\n")
design()
print("pasword system inteface".center(115).upper(),'\n')
design()

password="Cyber@123" #Reference password
#Main logic and loop section:

while True:
    print("-"*128)
    password_1=input("Enter the correct password :".center(30).ljust(50))
    print("-"*128)
    if (password_1==password): #for correct password: 
        design()
        print("Congratulations! you have entered correct password".title().center(115),"\n")
        design()
        break
    else:
        design() #for incorrect password:
        print("Sorry! you have entered password incoorect , please try again".title().center(115),"\n")
        design()
        continue
