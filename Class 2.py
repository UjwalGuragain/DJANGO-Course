#Control flow if, elif, else

# a = int(input("Enter a number:"))

# if a%2==0:
#     print(f"{a} is an even number.")
# else:
#     print(f"{a} is an odd number.")

#RESULT PRINTINGG

math = int(input("Enter marks of math:"))
if math<=100 and math>=0:
    physics = int(input("Enter marks of physics:"))
    if physics<=100 and physics>=0:
        chemistry = int(input("Enter marks of chemistry:"))
        if chemistry<=100 and chemistry>=0:
            computer = int(input("Enter marks of computer:"))
            if computer<=100 and computer>=0:
                biology = int(input("Enter marks of biology:"))
                if biology<=100 and biology>=0:
                    print("Your Result is displayed below:")
else:
    print("Please enter valid marks")


Total_Marks = 500

Total_obtained_marks = math + physics + chemistry + computer + biology

percentage = (Total_obtained_marks / Total_Marks)*100
print("Total Obtained Marks:", Total_obtained_marks)
print("Obtained Percentage : ",percentage)

if (math or physics or chemistry or computer or biology) <50:
    print("Grade Obtained : F ,You have failed!!")
elif percentage>90 and percentage<=100:
    print("Grade Obtained : A")
elif percentage>80 and percentage<=90:
    print("Grade Obtained : B")
elif percentage>70 and percentage<=80:
    print("Grade Obtained : C")
elif percentage>60 and percentage<=70:
    print("Grade Obtained : D")
elif percentage>50 and percentage<=60:
    print("Grade Obtained : E")
else:
    print("Grade Obtained : F ,You have failed!!")


#Gameeeeeeeeeeeeeeeeeeeee

# Name = input("Say your name:").upper
# position = input("You have three ways, Where do you want to go? LEFT RIGHT STRAIGHT:").upper()
# if position == "STRAIGHT":
#     print(f"Congrats {Name}, You have reached the pond.")

#     position2 = input("Now you have to cross the pond, Will you SWIM or wait for the BOAT to help you?:").upper()

#     if position2 == "SWIM":
#         print(f"Congrats {Name}, You have reached the Palace.")
        
#         position3 = input("You have 4 door ahead, Which door you want to enter? FIRST, SECOND, THIRD or FOURTH:").upper()
        
#         if position3 == "THIRD":
#             print(f"Congrats {Name}, You have found the hidden treasure. YOU WON!!!")
#         elif position3 == "FIRST" or position3 == "SECOND" or position3 == "FOURTH":
#             print(f"{Name} You are eaten by the Black Mamba, You LOSE!!!")
#         else :
#             print(f"Please enter the correct option!!")

#     elif position2 == "BOAT":
#         print("The boat is never gonna come, You LOSE!!!")
#     else :
#         print(f"Please enter the correct option!!")

# elif position == "LEFT" or position == "RIGHT":
#     print(f"You LOSE {Name}!!!")
# else:
#     print(f"Please enter the correct option!!")







#vegchaumin full lai 100 half lai 50rs andddddd eggchaumin full lai 130 half lai 80
#chaumin khane?umm kun khane?kati khane?