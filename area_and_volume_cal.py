
print("*" + "~~" * 58 + "*")
print("| " + "Area and Volume Calculator".center(115).upper() + "|")
print("*" + "~~" * 58 + "*")
print(" welcome to area & volume calculator ".center(20).title())
print("*" + "~~" * 58 + "*")
print("*" + "==" * 58 + "*")
print("Shape chart ".upper().center(115))
print("*" + "==" * 58 + "*")
print("  Shapes:".upper().ljust(57),"|".ljust(25),"Numbers:".upper())
print("*" + "==" * 58 + "*")
Shapes=["Circle","Rectangle","Square","Triangle","Cylinder","Cone","Sphere","Cube"]

for i, j in enumerate(Shapes, 1):
    print("  "*4,f"{j}".ljust(48),"|".ljust(28),i)
    print( " ","==" * 57,"\n" )

while True:
    print( "~~" * 60 )
    shape_num=int(input("Enter the Shape number according to given chart above : ".ljust(10)))
    print( "~~" * 60 )


    if ( shape_num == 1):
        radius_1=float(input("Enter the radius in meters : ".ljust(30)))
        area_1= 3.142*(radius_1)**2 
        print(" "*4,f"The area of {Shapes[0]} is {area_1} m*2")
        print(" "*4,f"The {Shapes[0]} does not have any volume")

    elif ( shape_num == 2 ):
        l=float(input("Enter the length in meters :".ljust(30)))
        b=float(input("Enter the breadth in meters :".ljust(30)))
        area_2=l*b
        print(" "*4,f"The area of {Shapes[1]} is {area_2} m*2")
        print(" "*4,f"The {Shapes[1]} does not have any volume")

    elif ( shape_num== 3):
        side=float(input("Enter the side in meters :".ljust(30)))
        area_3=side**2
        print(" "*4,f"The area of {Shapes[2]} is {area_3} m*2")
        print(" "*4,f"The {Shapes[2]} does not have any volume")

    elif ( shape_num==4 ):
        base_1=float(input("Enter the base in meters :".ljust(30)))
        height=float(input("Enter the height in meters :".ljust(30)))
        area_4=0.5*base_1*height
        print(" "*4,f"The area of {Shapes[3]} is {area_4} m*2")
        print(" "*4,f"The {Shapes[3]} does not have any volume")

    elif ( shape_num==5 ):
        radius_2=float(input("Enter the radius in meters :".ljust(30)))
        height_1=float(input("Enter the height in meters :".ljust(30)))
        area_5=2*3.142*radius_2*(radius_2+height_1)
        vol_1=3.142*(radius_2**2)*height_1
        print(" "*4,f"The area of {Shapes[4]} is {area_5} m*2")
        print(" "*4,f"The Volume of {Shapes[4]} is {area_5} m*3")

    elif ( shape_num==6 ):
        slant_height=float(input("Enter the slant height in meters :".ljust(30)))
        perpendicular_height=float(input("Enter the perpendicular height in meters :".ljust(30)))
        radius_3=float(input("Enter the radius in meters :".ljust(30)))
        area_6=3.142*radius_3*(radius_3+slant_height)
        vol_2=0.34*3.14*(radius_3**2)*perpendicular_height
        print(" "*4,f"The area of {Shapes[5]} is {area_6} m*2")
        print(" "*4,f"The Volume of {Shapes[5]} is {area_6} m*3")

    elif ( shape_num==7 ):
        pass

    elif ( shape_num==8 ):
        pass
    else:
         print("Invlid")
         
    again=input("\nDo you want to check any other shape? (yes/no): ")
    if again.lower() == "yes":
        continue

    elif again.lower() == "no":
         print("Thank you!")
    break
        
        

    