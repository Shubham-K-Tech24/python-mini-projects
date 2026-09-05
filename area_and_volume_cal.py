#Banner Section: 

def design_1():
    print("~~" * 58)

design_1()
print("Area and Volume Calculator".center(115).upper())
design_1()
print(" welcome to area and volume calculator ".center(20).title())
design_1()
print("==" * 58)
#Shape Chart display:
def design_2():
    print("==" * 58)
    
print("Shape chart ".upper().center(115))
design_2()
print("  Shapes:".upper().ljust(57),"|".ljust(25),"Numbers:".upper())
design_2()
Shapes=["Circle","Rectangle","Square","Triangle","Cylinder","Cone","Sphere","Cube","Cuboid","Hemisphere","Hollow Sphere","Solid Sphere","Hollow Cone","Solid Cone"]

for i, j in enumerate(Shapes, 1):
    print("  "*4,f"{j}".ljust(48),"|".ljust(28),i)
    design_2()

#Input and main Logic section:
def result():
    print("  "*24,"-"*5 + "Result" +"-"*5 )

while True:
    design_1()
    shape_num=int(input("Enter the Shape number according to given chart above : ".ljust(10)))
    design_1()

#Circle:
    if ( shape_num == 1): 
        print("You enter shape is : ".ljust(5),Shapes[0])
        radius_1=float(input("Enter the radius in meters : ".ljust(30)))
        area_1= 3.142*(radius_1)**2 
        result()
        print(" "*4,f"The area of {Shapes[0]} is {area_1} m*2")
        print(" "*4,f"The {Shapes[0]} does not have any volume")
#Rectangle:
    elif ( shape_num == 2 ):
        print("You enter shape is : ".ljust(5),Shapes[1])
        l=float(input("Enter the length in meters :".ljust(30)))
        b=float(input("Enter the breadth in meters :".ljust(30)))
        area_2=l*b
        result()
        print(" "*4,f"The area of {Shapes[1]} is {area_2} m*2")
        print(" "*4,f"The {Shapes[1]} does not have any volume")
#Square:
    elif ( shape_num== 3):
        print("You enter shape is : ".ljust(5),Shapes[2])
        side=float(input("Enter the side in meters :".ljust(30)))
        area_3=side**2
        result()
        print(" "*4,f"The area of {Shapes[2]} is {area_3} m*2")
        print(" "*4,f"The {Shapes[2]} does not have any volume")
#Triangle:
    elif ( shape_num==4 ):
        print("You enter shape is : ".ljust(5),Shapes[3])
        base_1=float(input("Enter the base in meters :".ljust(30)))
        height=float(input("Enter the height in meters :".ljust(30)))
        area_4=0.5*base_1*height
        result()
        print(" "*4,f"The area of {Shapes[3]} is {area_4} m*2")
        print(" "*4,f"The {Shapes[3]} does not have any volume")
#Cylinder:
    elif ( shape_num==5 ):
        print("You enter shape is : ".ljust(5),Shapes[4])
        radius_2=float(input("Enter the radius in meters :".ljust(30)))
        height_1=float(input("Enter the height in meters :".ljust(30)))
        area_5=2*3.142*radius_2*(radius_2+height_1)
        vol_1=3.142*(radius_2**2)*height_1
        result()
        print(" "*4,f"The area of {Shapes[4]} is {area_5} m*2")
        print(" "*4,f"The Volume of {Shapes[4]} is {vol_1} m*3")
#Cone:
    elif ( shape_num==6 ):
        print("You enter shape is : ".ljust(5),Shapes[5])
        slant_height_1=float(input("Enter the slant height in meters :".ljust(30)))
        perpendicular_height_1=float(input("Enter the perpendicular height in meters :".ljust(30)))
        radius_3=float(input("Enter the radius in meters :".ljust(30)))
        area_6=3.142*radius_3*(radius_3+slant_height_1)
        vol_2=(1/3)*3.14*(radius_3**2)*perpendicular_height_1
        result()
        print(" "*4,f"The area of {Shapes[5]} is {area_6} m*2")
        print(" "*4,f"The Volume of {Shapes[5]} is {vol_2} m*3")
#Sphere:
    elif ( shape_num==7 ):
        print("You enter shape is : ".ljust(5),Shapes[6])
        radius_4=float(input("Enter the radius in meters : ".ljust(30)))
        area_7= 4*3.142*(radius_4**2)
        vol_3= (4/3)*3.142*(radius_4**3)
        result()
        print(" "*4,f"The area of {Shapes[6]} is {area_7} m*2")
        print(" "*4,f"The Volume of {Shapes[6]} is {vol_3} m*3")
#Cube:
    elif ( shape_num==8 ):
        print("You enter shape is : ".ljust(5),Shapes[7])
        side_1=float(input("Enter the side in meters : ".ljust(30)))
        area_8= 6*(side_1**2)
        vol_4= side_1**3
        result()
        print(" "*4,f"The area of {Shapes[7]} is {area_8} m*2")
        print(" "*4,f"The Volume of {Shapes[7]} is {vol_4} m*3")
#Cuboid:
    elif( shape_num==9 ):
        print("You enter shape is : ".ljust(5),Shapes[8])
        l_1=float(input("Enter the length in meters : ".ljust(30)))
        b_2=float(input("Enter the breadth in meters : ".ljust(30)))
        height_2=float(input("Enter the height in meters : ".ljust(30)))
        area_9=2*((l_1*b_2)+(b_2*height_2)+(l_1*height_2))
        vol_5=l_1*b_2*height_2
        result()
        print(" "*4,f"The  Total surface area of {Shapes[8]} is {area_9} m*2")
        print(" "*4,f"The Volume of {Shapes[8]} is {vol_5} m*3")
#Hemisphere:
    elif( shape_num==10 ):
        print("You enter shape is : ".ljust(5),Shapes[9])
        radius_5=float(input("Enter the radius in meters : ".ljust(30)))
        area_10=3*3.142*(radius_5**2)
        vol_6=(2/3)*3.142*(radius_5**3)
        print(" "*4,f"The  Total surface area of {Shapes[9]} is {area_10} m*2")
        print(" "*4,f"The Volume of {Shapes[9]} is {vol_6} m*3")
#Hollow Sphere:
    elif( shape_num==11 ):
        print("You enter shape is : ".ljust(5),Shapes[10])
        i_radius_1=float(input("Enter the inner radius in meters : ".ljust(30)))
        o_radius_1=float(input("Enter the outer radius in meters : ".ljust(30)))
        area_11=4*3.142*((o_radius_1**2) + (i_radius_1**2))
        vol_7=(4/3)*3.142*((o_radius_1**3)-(i_radius_1**3))
        print(" "*4,f"The  Total surface area of {Shapes[10]} is {area_11} m*2")
        print(" "*4,f"The Volume of {Shapes[10]} is {vol_7} m*3")                  

#Solid Sphere:
    elif(shape_num==12 ):
        print("You enter shape is : ".ljust(5),Shapes[11])
        i_radius_2=float(input("Enter the inner radius in meters : ".ljust(30)))
        o_radius_2=float(input("Enter the outer radius in meters : ".ljust(30)))
        area_12=4*3.142*(o_radius_2**2)
        vol_8=(4/3)*3.142*((o_radius_2**3)-(i_radius_2**3))
        print(" "*4,f"The  Total surface area of {Shapes[11]} is {area_12} m*2")
        print(" "*4,f"The Volume of {Shapes[11]} is {vol_8} m*3")
        
#Hollow Cone:
    elif(shape_num==13 ):
       print("You enter shape is : ".ljust(5),Shapes[12])
       slant_height_2=float(input("Enter the slant height in meters :".ljust(30)))
       perpendicular_height_2=float(input("Enter the perpendicular height in meters :".ljust(30)))
       i_radius_3=float(input("Enter the inner radius in meters : ".ljust(30)))
       o_radius_3=float(input("Enter the outer radius in meters : ".ljust(30)))
       area_13=3.142*slant_height_2*((o_radius_3) + (i_radius_3))
       vol_9=(1/3)*3.142*perpendicular_height_2*((o_radius_3**2)-(i_radius_3**2))
       print(" "*4,f"The  Total  curved surface area of {Shapes[12]} is {area_13} m*2")
       print(" "*4,f"The Volume of {Shapes[12]} is {vol_9} m*3")
          
#Solid Cone:
    elif(shape_num==14 ):
        print("You enter shape is : ".ljust(5),Shapes[13])
        print("You enter shape is : ".ljust(5),Shapes[12])
        slant_height_3=float(input("Enter the slant height in meters :".ljust(30)))
        perpendicular_height_3=float(input("Enter the perpendicular height in meters :".ljust(30)))
        radius_14=float(input("Enter the radius in meters :".ljust(30)))
        area_14=3.142*radius_14*(radius_14+slant_height_3)
        vol_10=(1/3)*3.142*((radius_14**3)+ (perpendicular_height_3))
        print(" "*4,f"The  Total surface area of {Shapes[13]} is {area_14} m*2")
        print(" "*4,f"The Volume of {Shapes[13]} is {vol_10} m*3")
    else:
        print("Invlid")
    design_1()   
    again=input("   Do you want to check any other shape? (yes/no): ")
    design_1()
    
#for another shape :

    if again.lower() == "yes":
        continue

    elif again.lower() == "no":
         print( "~~" * 58,"\n")
         print("-----Thank you!,Visit again----- ".center(115),"\n")
         print( "~~" * 58,"\n" )
    break 
    