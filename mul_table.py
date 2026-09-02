#Banner section:
print("~~~"*43,"\n")
print("multiplication table generator".center(115).title(),"\n")
print("~~~"*43)
#Intake section:
while True:
    mul_num=int(input("Enter the number for table generation : ".ljust(30)))
    till=int(input("Enter the number till were the table to be generated : ".ljust(30)))
    print("~~~"*43)
    print("table:".center(50).upper())
    print("~~~"*43)
#main logic section:
    for i in range(1,(till+1)):
        print(" "*30,mul_num,"x",i,"=",(mul_num*i))
        print("---"*43)
    print("~~~"*43)
    again=input("Do you want to find table of any another number? (yes/no) : ".ljust(10))
    print("~~~"*43)
#Again repeating loop / ending section:
    if ( again.lower() == "yes"):
        continue
    elif ( again.lower() == "no" ):
        print("~~~"*43,"\n")
        print("-----thankyou for visiting-----".center(115).title(),"\n")
        print("~~~"*43,"\n")
        break