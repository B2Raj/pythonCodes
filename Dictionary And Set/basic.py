""" Dictionary are used to store data values in key:value pairs. They are unordered, mutable(changeable) and
don't allow duplicate keys  """

# They are build_in data types


print("List of information: ")
dict={"name":"B2", "course":"UG", "sub":"CS"}
print(dict)
print(type(dict))


info={"Name":"Bittu","Place":"Patna","Village":"Bihta", "Age":
      17, "DOB":"17th May","isAdult":True, "subject":{"python","C++"}, "topic":("Dict","Tuple","List")}
print(info)
print(type(dict))
# we can also get individually access of keys
print(info["Name"])
print(info["DOB"])
print(info["Village"])

# We can also assign or update the keys
info["Name"]="B2"
print(info)

# We can also add new key in dictionary

info["Surname"]="Raj"
print(info)


# We can also create NULL dictionary

null_dict={}
print(null_dict)
# After creating null dictionary, we can add key value in it
null_dict["Name"]="Bittu Raj"
null_dict["Course"]="BSc"
null_dict["Roll"]=35084
print(null_dict)


# We can make NESTED dictionary, like dictionary in dictonary

student={"Name":"Bittu Raj",
         "Subject":{"phy","maths","computer","evs","GK","Biology"},
         "Roll No.":35084,"course":"BSc", "Marks":{"phy":78,"maths":78,"computer":45,
        "evs":79,"GK":89,"Biology":89}}
print(student)
print(student["Subject"])
print(student["Marks"])
print(student["Marks"],["Biology"])


        # Some Dictionary functions in dictionary
# myDict.key()  returns all keys
# myDict.values() returns all value
# myDict.items()  returns all (keys,value) pairs as tuples
# myDict.get("key")  returns the key according to value
# myDict.update(newDict)  inserts the specified items to the dictionary


mySelf={"Name":"B2","Class":"Graduatioon","Roll":35084}
print("myself:",mySelf)
print(mySelf.keys())
print(mySelf.values())
print(mySelf.items())
print(mySelf.get("Class"))
mySelf.update({"Sub":"computer"})
print(mySelf)