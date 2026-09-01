#Banner section:

print("~~"*66,"\n")
print("even or odd number analyzer".center(120).title(),"\n")
print("~~"*66)

#input section:

print("--"*66)
numbers=[]
num_entered= input("Enter the numbers to analyze : ")
for j in num_entered.split(","):
    numbers.append(int(j))

#Main logic & result section:

print("--"*66)
for i in numbers:
    if (i%2) == 0:
        print(f"The given number {i} is even")
        print("--"*66)
       
    else:
        print(f"The given number {i} is odd")
        print("--"*66)
   
#Ending section:

print("~~"*66,"\n")
print("thankyou,visit again".center(120).title(),"\n")      
print("~~"*66,"\n")     
      
      