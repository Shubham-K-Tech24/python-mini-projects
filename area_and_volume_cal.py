#Banner Section:

print("~~" * 58)
print("Area and Volume Calculator".center(115).upper())
print("~~" * 58)
print(" welcome to area & volume calculator ".center(20).title())
print("~~" * 58)
print("==" * 58)
#Shape Chart display:

print("Shape chart ".upper().center(115))
print("==" * 58)
print("  Shapes:".upper().ljust(57),"|".ljust(25),"Numbers:".upper())
print("==" * 58)
Shapes=["Circle","Rectangle","Square","Triangle","Cylinder","Cone","Sphere","Cube"]

for i, j in enumerate(Shapes, 1):
    print("  "*4,f"{j}".ljust(48),"|".ljust(28),i)
    print( " ","==" * 57,"\n" )

#Input and main Logic section:

while True:
    print( "~~" * 60 )
    shape_num=int(input("Enter the Shape number according to given chart above : ".ljust(10)))
    print( "~~" * 60 )

#Circle:
    if ( shape_num == 1): 
        print("You enter shape is : ".ljust(5),Shapes[0])
        radius_1=float(input("Enter the radius in meters : ".ljust(30)))
        area_1= 3.142*(radius_1)**2 
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[0]} is {area_1} m*2")
        print(" "*4,f"The {Shapes[0]} does not have any volume")
#Rectangle:
    elif ( shape_num == 2 ):
        print("You enter shape is : ".ljust(5),Shapes[1])
        l=float(input("Enter the length in meters :".ljust(30)))
        b=float(input("Enter the breadth in meters :".ljust(30)))
        area_2=l*b
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[1]} is {area_2} m*2")
        print(" "*4,f"The {Shapes[1]} does not have any volume")
#Square:
    elif ( shape_num== 3):
        print("You enter shape is : ".ljust(5),Shapes[2])
        side=float(input("Enter the side in meters :".ljust(30)))
        area_3=side**2
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[2]} is {area_3} m*2")
        print(" "*4,f"The {Shapes[2]} does not have any volume")
#Triangle:
    elif ( shape_num==4 ):
        print("You enter shape is : ".ljust(5),Shapes[3])
        base_1=float(input("Enter the base in meters :".ljust(30)))
        height=float(input("Enter the height in meters :".ljust(30)))
        area_4=0.5*base_1*height
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[3]} is {area_4} m*2")
        print(" "*4,f"The {Shapes[3]} does not have any volume")
#Cylinder:
    elif ( shape_num==5 ):
        print("You enter shape is : ".ljust(5),Shapes[4])
        radius_2=float(input("Enter the radius in meters :".ljust(30)))
        height_1=float(input("Enter the height in meters :".ljust(30)))
        area_5=2*3.142*radius_2*(radius_2+height_1)
        vol_1=3.142*(radius_2**2)*height_1
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[4]} is {area_5} m*2")
        print(" "*4,f"The Volume of {Shapes[4]} is {area_5} m*3")
#Cone:
    elif ( shape_num==6 ):
        print("You enter shape is : ".ljust(5),Shapes[5])
        slant_height=float(input("Enter the slant height in meters :".ljust(30)))
        perpendicular_height=float(input("Enter the perpendicular height in meters :".ljust(30)))
        radius_3=float(input("Enter the radius in meters :".ljust(30)))
        area_6=3.142*radius_3*(radius_3+slant_height)
        vol_2=0.34*3.14*(radius_3**2)*perpendicular_height
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[5]} is {area_6} m*2")
        print(" "*4,f"The Volume of {Shapes[5]} is {area_6} m*3")
#Sphere:
    elif ( shape_num==7 ):
        print("You enter shape is : ".ljust(5),Shapes[6])
        radius_4=float(input("Enter the radius in meters : ".ljust(30)))
        area_7= 4*3.142*(radius_4**2)
        vol_3= (4/3)*3.142*(radius_4**3)
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[6]} is {area_7} m*2")
        print(" "*4,f"The Volume of {Shapes[6]} is {area_7} m*3")
#Cube:
    elif ( shape_num==8 ):
        print("You enter shape is : ".ljust(5),Shapes[7])
        side_1=float(input("Enter the side in meters : ".ljust(30)))
        area_8= 6*(side_1**2)
        vol_4= side_1**3
        print("  "*24,"-"*5 + "Result" +"-"*5 )
        print(" "*4,f"The area of {Shapes[7]} is {area_8} m*2")
        print(" "*4,f"The Volume of {Shapes[7]} is {area_8} m*3")

    else:
         print("Invlid")
    print( "~~" * 60)     
    again=input("   Do you want to check any other shape? (yes/no): ")
    print("~~" * 60)
#for another shape :

    if again.lower() == "yes":
        continue

    elif again.lower() == "no":
         print( "~~" * 60,"\n")
         print("-----Thank you!,Visit again----- ".center(115),"\n")
         print( "~~" * 60,"\n" )
    break    
