## list2.pop()
# del(list2[1])
# list2.remove("aaryan")
# print(list2)

# for i in list2:
#     if i == "aaryan":
#         print(i)

# list1.append(list2)
# print(list1)

#list adding

# list1.extend(list2)
# list3 = list1 + list2
# print(list3)


# listx = []

# x = int(input("How many names you want to add?:"))

# for i in range (x):
#     name = input(f"Enter {i + 1}th name:")
#     listx.append(name)
#     # listx.extend(name)
# print(listx)

# typecasting------->

# list1 = [1,2,3,4,5,6,7,8,9]
# list2 = ["ujwal", "yujal", "aaryan", "aayush"]
# tuple1 = tuple(list1)
# print(tuple1)

# set1 = set(list2)
# print(set1)

# TUPLESSSSSSSSSSSSSSSSSSSSS------------>()

# tuple2 = ("ujwal", "yujal", "aaryan", "aayush")
# print(tuple2[2])
# listz = list(tuple2)
# listz.append("Binayak")
# tuplez = tuple(listz)
# print(tuplez)

#SETTTTTTTTTTT------------->{}

# set2 = {"ujwal", "yujal", "aaryan", "aayush"}
# set2.add("binayak")    #Adding data into set
# set2.remove("aayush")  #Removing data from set
# print(set2)



#Dictionary------------->{}

dict1 = {"Name" : "Ujwal", "Age" : 20}

# print(dict1.keys())    #Prints keys of dictionary
# print(dict1.values())  #Prints values of dictionary

# print(dict1["Name"]) #To print a specific value using keys

dict1["Gender"] = "Male"  #Adding data in dictionary

# dict1.popitem() #deletes last item of the dictionary

# dict1.pop("Name") #deletes data accoring to the keys

# del(dict1["Age"]) #deletes data accoring to the keys

dict1.clear   #Clear outs values but the keys remains intact

dict2 = dict1.copy   #Copies the dictionary just like list.copy()
print(dict1)