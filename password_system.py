#Banner section:
print("~"*130,"\n")
print("pasword system inteface".center(115).upper(),'\n')
print("~"*130,"\n")

password="Cyber@123" #Reference password
#Main logic and loop section:

while True:
    print("-"*130)
    password_1=input("Enter the correct password :".center(30).ljust(50))
    print("-"*130)
    if (password_1==password): #for correct password: 
        print("~"*130,"\n")
        print("Congratulations! you have entered correct password".title().center(115),"\n")
        print("~"*130,"\n")
        break
    else:
        print("~"*130,"\n") #for incorrect password:
        print("Sorry! you have entered password incoorect , please try again".title().center(115),"\n")
        print("~"*130,"\n")
        continue
